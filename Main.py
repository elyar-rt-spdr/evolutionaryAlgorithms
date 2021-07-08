class Individual:
    def __init__(self, position):
        self.position = position

import random

class Population:
    def __init__(self, SIZE):
       self.SIZE = SIZE
       self.individuals = []
       for i in range(SIZE):
           self.individuals.append(Individual(random.random()))
    
    def listPopulation(self):
        for individual in self.individuals:
            print(individual.position)

pop_1 = Population(10)
pop_1.listPopulation()