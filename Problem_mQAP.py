
import numpy as np

class Problem_mQAP:
    def __init__(self, path):
        """sets problem parameters from the problem file

        Args:
            path (string): path to the problem file
        """
        f = open(path, "r")
        file_content = f.read().splitlines()

        count = 0
        settings = file_content[count].split()
        self.problem_size = int(settings[2])
        self.n_objectives = int(settings[5])
        self.max_distance = int(settings[8])
        self.max_flow = int(settings[12])
        self.distance_matrix = np.zeros(shape = (self.problem_size, self.problem_size))
        self.flow_matrix = np.zeros(shape = (self.n_objectives, self.problem_size, self.problem_size))
        count = 1
        for i in range(count, self.problem_size+count):
            self.distance_matrix[i-count] = [int(_) for _ in  file_content[i].split()]

        for j in range(self.n_objectives):
            count +=  self.problem_size + 1
            for i in range(count, self.problem_size+count):
                self.flow_matrix[j,i-count] = [int(_) for _ in  file_content[i].split()]


    def get_objective_function_permutation_list(self, solution):
        """This function calculates the objective function of the problem

        Args:
            solution (List of int): A permutation list

        Returns:
            List of int: objective function values
        """
        objs = [sum([int(self.flow_matrix[k][i][j])*int(self.distance_matrix[solution[i]][solution[j]]) for j in range(self.problem_size) for i in range(self.problem_size)]) for k in range(self.n_objectives)]
        return objs


    def get_objective_function_permutation_matrix(self, solution):
        """This function calculates the objective function of the problem

        Args:
            solution (2D list of dimod.Binary): A permutation matrix representing the solution to the problem

        Returns:
            List of int: objective function values
        """
        objectives = []
        for k in range(self.n_objectives):
            sum_obj = 0
            for i in range(self.problem_size):
                for j in range(self.problem_size):
                    for pos_i in range(self.problem_size):
                        for pos_j in range(self.problem_size):
                            sum_obj += self.flow_matrix[k][i][j] * self.distance_matrix[pos_i][pos_j] * solution[i][pos_i] * solution[j][pos_j]
            objectives.append(sum_obj)
        return objectives
    



