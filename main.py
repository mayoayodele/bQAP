import dimod
from Problem_mQAP import Problem_mQAP
from dwave.system import LeapHybridCQMSampler
import util
import numpy as np
import yaml



DEFAULT_CONFIG_FILE = "./config.yaml"




def main(config):
    with open(config, "r") as f:
        CONFIG = yaml.safe_load(f)


    time_limit = CONFIG['time-limit']
    n_weights = CONFIG['number-of-weights'] 
    scalarisation_method = CONFIG['scalarisation-method']
    problem_name =  CONFIG['problem-name'] 
    

    print(scalarisation_method, time_limit)
    
    path = 'Instances//' + problem_name 
    qap = Problem_mQAP(path)
    problem_size = qap.problem_size
    
    #two way one hote representation for the problem
    model = [[dimod.Binary( 'position' + str(j) + 'location' + str(i) ) for i in range(problem_size)] for j in range(problem_size)]
    
    if scalarisation_method.lower() == 'uniform':
        weight_list = np.linspace(0,1, n_weights)
    weights_and_energies = {}
    for k in range(n_weights):
        if scalarisation_method.lower() == 'uniform':
                weights = tuple([weight_list[k], 1-weight_list[k]])
        elif scalarisation_method.lower() in ['dichotomic', 'averages']:
            if(k < 2):
                #when k= 0, minimise the first objective only (i.e. weights = (1, 0)), when k=1, minimise the second objective only (i.e. weights = (0, 1))
                weights = tuple([(k+1)%2, k%2])
            else:
                #derive a set of weights based on the largest gap on the pareto front
                weights = util.get_adaptive_scalarisation_weights (weights_and_energies, method=scalarisation_method)
        else:
                raise NotImplementedError('Please set scalarisation_method to dichotomic, averages or uniform')


        cqm = dimod.ConstrainedQuadraticModel()

        for i in range(problem_size):
            cqm.add_constraint(sum(model[i])== 1, label=f'one_location_position_{i}')
            cqm.constraints[f'one_location_position_{i}'].lhs.mark_discrete()

        #calculate the energy for each objective
        objectives = qap.get_objective_function_permutation_matrix(model)
        #apply the scalarisation weights
        combined_objective = (weights[0] * objectives[0]) + (weights[1] * objectives[1])
        #set the combined objective as the objective function for the cqm
        cqm.set_objective(combined_objective)

        for j in range(problem_size):
            cqm.add_constraint((sum([model[i][j] for i in range(problem_size)]))  == 1, label = 'constraint_column' + str(j))
        
        sampler = LeapHybridCQMSampler() 


        sampleset = sampler.sample_cqm(cqm, time_limit=time_limit)  
        feasible_sampleset = sampleset.filter(lambda row: row.is_feasible)  
        solution = feasible_sampleset.first.sample
        
        #the best solution during each iteration is converted from two-way one-hot to permutation and stored in permutation_list_solution
        permutation_list_solution = [[solution[f'position{j}location{i}'] for i in range(problem_size)].index(1) for j in range(problem_size)]
        #the objective function of this solution is recalculated individually
        multiple_objectives = tuple(qap.get_objective_function_permutation_list(permutation_list_solution))
        #keeps a record of all aggregation weights used and the objective function
        weights_and_energies[weights] = multiple_objectives
        print('Weight', weights, 'Objectives', multiple_objectives, 'Solution', permutation_list_solution)
                
    print(weights_and_energies)

if __name__ == "__main__":
    main(DEFAULT_CONFIG_FILE)

