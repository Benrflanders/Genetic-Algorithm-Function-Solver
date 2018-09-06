import random

import population
import individual

class genetic_algorithm:
    #initialise population with random candidate solutions;
    #evaluate each candidate
    def __init__(self, fitness_function):
        self.fitness_function = fitness_function
        self.population = population.population(self.fitness_function)
        print(self.fitness_function)
        self.evaluate()
        print(self.population) #print out the population for now
        #print(self.population.most_fit()) #print out the most fit member of the population

    def evaluate(self):
        self.iteration = 0
        while(True):
            self.iteration += 1
            print("iteration: ", self.iteration)
            self.population.update_fitness()
            #pops two parents from the population pool
            self.parent_selection_1 = self.population.select_parent()
            self.parent_selection_2 = self.population.select_parent()

            #generate an offspring from the two selected parents
            self.offspring = self.recombine(self.parent_selection_1, self.parent_selection_2)
            #self.offspring = self.population.mutate(self.offspring)

            #select two members to re-enter the population
            self.survivor_selection()
            #check if termination conditions are met
            if(self.check_termination()):
                print("BREAKING!")
                break #finish evaluation loop

            
    #recombination and mutation algorithms
    def recombine(self, parent_1, parent_2):
        gene = []
        
        #randomly choose which parent will give each chromosome
        for chromosome_index in range(0,len(parent_1.get_gene())):
            if(random.randint(0,1) == 0):
                gene.append(parent_1.get_gene()[chromosome_index])
            else:
                gene.append(parent_2.get_gene()[chromosome_index])

        #n-point mutation
        for chromosome in gene:
            if(random.randint(0, 10) < 2):
                chromosome += random.randint(-10, 10)

        offspring = individual.individual(self.fitness_function)
        offspring.set_gene(gene)

        return offspring
    '''
    survivor_selection determines which currently selected parent will survive,
    and adds the current offspring into the population
    '''
    def survivor_selection(self):
        if(self.parent_selection_1.fitness > self.parent_selection_2.fitness):
            self.population.population_list.append(self.parent_selection_1)
        else:
            self.population.population_list.append(self.parent_selection_2)

        self.population.population_list.append(self.offspring)
        
        #clear out all three objects for later use
        self.parent_selection_1 = None
        self.parent_selection_2 = None
        self.offspring = None

    #check for compeltion based on fitness levels of the population
    def check_termination(self):
        curr_max_fitness = self.population.get_best_member().get_fitness()

        for member in self.population.population_list:
            if member.get_fitness() == 100:
                print("YOU DONE IT!")
                print(member.get_gene())
                #print(self.get_best_individual())
                return True
            if self.iteration == 100000:
                print("CANCELING...")
                print("Best individual: ", self.population.get_best_member().get_gene())
                return True
        print("Max fitness: ", curr_max_fitness)
        return False

    #get the fitness of a single member of the population
    def fitness(self):
        #self.max_fitness = ...
        #keep track of the current maximum fitness for use with the termination function
        self.population.update_fitness()
        return 0

    def get_best_individual(self):
        return self.population.get_best_member()