import genetic_algorithm

#where the population will be processed and the main loop is contained


#initialise population with random candidate solutions

print("Enter a function to be solved: \n")
fitness_function = [1780, 17, -2] #n = ax + by
#function: [n, a, b]

ga = genetic_algorithm.genetic_algorithm(fitness_function)


#evaluate each candidate

#repeat until (termination condition is satifsfied ) DO

#select parents;
#recombine pairs of parents
#mutate the resulting offspring
#evaluate new candidates
#select individuals for the next generation
#OD
#END
