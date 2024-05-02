import math
import statistics



@staticmethod
def get_distance(energies_a, energies_b, distance_metric):
    """calculates the distance between the objective function values of any two solution

    Args:
        energies_a (int): objective values for the a given solution a
        energies_b (int): objective values for the a given solution b
        distance_metric (str): only two permitted values 'manhattan' or 'euclidean'

    Raises:
        NotImplementedError: only manhattan or euclidean distance metric supported

    Returns:
        int: the distance between any pair of solutions
    """
    distance_metric = distance_metric.lower()
    if(distance_metric == 'manhattan'):
        return sum([abs(energies_a[i] - energies_b[i]) for i in range(len(energies_a))])
    elif(distance_metric == 'euclidean'):
        return math.prod([abs(energies_a[i] - energies_b[i]) for i in range(len(energies_a))])
    else:
        raise NotImplementedError ('please set distance_metric to manhattan or euclidean')
    

@staticmethod
def get_adaptive_scalarisation_weights(weights_and_energies, method = 'averages', distance_metric = 'euclidean'):
    """calcuates a set of scalarisation weights

    Args:
        weights_and_energies (dict {str, int}): dictionary containing the weights applied so far and the corresponding energy for each objective
        method (str, optional):  method to be used to derive scalarisation weights. Defaults to 'averages'.
        distance_metric (str, optional): method to be used to derive the gap between any pair of solutions. Defaults to 'euclidean'.

    Raises:
        NotImplementedError: only dichotomic or averages scalairsation method is supported

    Returns:
        tuple (float, float): scalarisation weights to be applied to the objectives
    """


    
    temp_weights_and_energies = dict(sorted(weights_and_energies.items(), key=lambda item: item[1][0], reverse=False))
    energy_keys = list(temp_weights_and_energies.keys())
    if(method.lower() == 'dichotomic'):
        a = tuple(weights_and_energies[energy_keys[0]])
        b =tuple(weights_and_energies[energy_keys[1]])
    elif (method.lower() == 'averages'):
        a = tuple(energy_keys[0])
        b = tuple(energy_keys[1])
    else:
        raise NotImplementedError
    largest_distances = get_distance(tuple(weights_and_energies[energy_keys[0]]), tuple(weights_and_energies[energy_keys[1]]), distance_metric)
    for i in range(1, len(energy_keys)-1):
        temp_a = tuple(weights_and_energies[energy_keys[i]])
        temp_b = tuple(weights_and_energies[energy_keys[i+1]])
        temp_distance = get_distance(temp_a, temp_b, distance_metric)
        if(temp_distance> largest_distances):
            largest_distances = temp_distance
            if(method.lower() == 'dichotomic'):
                a = temp_a
                b = temp_b
            elif(method.lower() == 'averages'):
                a = energy_keys[i]
                b = energy_keys[i+1]
    if(method.lower() == 'dichotomic'):
        lambda_1 = a[1] - b[1]
        lambda_2 = b[0] - a[0]
        sum_lambdas = lambda_1 + lambda_2
        weights = tuple([lambda_1/sum_lambdas,lambda_2/sum_lambdas ])
    elif(method.lower() == 'averages'):
        weights = tuple([statistics.mean([a[i], b[i]]) for i in range(len(a)) ])
    
    return weights


