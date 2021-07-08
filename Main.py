import sys
class Individual:
    def __init__(self, values, score) -> None:
        self.values = values
        self.score = score
    

from numpy import random
class Population:
    def __init__(self, SIZE, problem) -> None:
       self.SIZE = SIZE
       self.individuals = []
       self.fitnessFunction = problem.fitnessFunction
       self.limits = problem.limits
       self.constraints = problem.constraints

       for x in range(SIZE):
           values = []
           for i in range(problem.dimension):
               values.append(random.uniform(problem.limits[i][0],problem.limits[i][0]))
           self.individuals.append(Individual(values, problem.fitnessFunction(values)))

    def selection(self):    
        pass
    
    def listPopulation(self):
        for individual in self.individuals:
            print(individual.position)


from numpy import square
class Problem:
    def __init__(self, dimension) -> None:
        self.dimension = dimension
        self.limits = []
        for i in range(dimension):
            self.limits.append([-5,5])

    def fitnessFunction(self, values):
        return sum(square(values))

    def constraints(self, values):
        return None

problema = Problem(4)
print(problema.fitnessFunction([2.0,1.0,4.0,3.0]))
