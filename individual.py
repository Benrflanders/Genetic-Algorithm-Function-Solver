import os
import random
import math

#a single individual to be used as part of a population
class individual:


    def __init__(self, fitness_function, gene = None):
        self.fitness = 0
        self.function = fitness_function
        #generate a random gene of size 2, each index of the gene is between 0 and 100

        self.gene = random.sample(range(0,1000), 2) #[x, y]
        self.gene_length = 2    
        self.update_fitness()

        
        #n0 = (n1 * x) + (n2 * y)
    def get_gene(self):
        return self.gene

    def set_gene(self, gene):
        self.gene = gene

    #function: n = ax + by + cz + ... 
    def update_fitness(self): 
        self.fitness = 0

        predicted_sum = 0
        actual_sum = self.function[0] #'n'
        index = 1 #'a'
        for variable in self.gene: #variable is each gene ex: gene[0] is 10, then x = 10
            predicted_sum += (variable * self.function[index])
            index += 1
        #print("Predicted Sum:", predicted_sum)
        self.fitness = math.fabs(actual_sum - predicted_sum) #get the difference between the actual value and predicted value
        self.fitness = (1/(self.fitness + 1)) * 100
        #try and minimize this value

    def get_fitness(self):
        self.update_fitness()
        return self.fitness