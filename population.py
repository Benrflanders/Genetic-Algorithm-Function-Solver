import individual
import random

class population:

    def __init__(self, fit_funct, population_size=100):
        self.population_size = population_size #set the population size
        self.population_list = []
        self.fitness_function = fit_funct
        self.generate_memebers()


    def generate_memebers(self):
        while(len(self.population_list) < self.population_size):
            indiv_to_add = individual.individual(self.fitness_function)
            self.add_member(indiv_to_add)
            print("current population size is: ", len(self.population_list))

    #add a new member to the population
    def add_member(self, member):
        self.population_list.append(member)

    #parent selection 
    def select_parent(self):
        #just randomly select two parents for now
        self.update_pop_size()
        return self.population_list.pop(random.randint(0, self.population_size-1))

    def update_fitness(self):
        for member in self.population_list:
            member.update_fitness()
    
    def update_pop_size(self):
        self.population_size = len(self.population_list)

    def get_best_member(self):
        best_member = None
        curr_max_fitness = 0
        for member in self.population_list:
            if member.get_fitness() > curr_max_fitness:
                best_member = member
        return best_member