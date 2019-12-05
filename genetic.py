import random
from product import Product
from individual import Individual

class GeneticAlgorithm:
    def __init__(self, size_population):
        self.size_population = size_population
        self.population = []
        self.generation = 0
        self.best_solution = None
        self.result = []
    
    def init_population(self, list_product, space_limit):
        for i in range(self.size_population):
            self.population.append(Individual(list_product, space_limit))
        self.best_solution = self.population[0]

    def sort_population(self):
        self.population = sorted(self.population, key = lambda ind: ind.score, reverse = True)
    
    def fit_population(self):
        for ind in self.population:
            ind.fitness()
    
    def best_individual(self, ind):
        if ind.score > self.best_solution.score:
            self.best_solution = ind
    
    def sum_score(self):
        s = 0
        for ind in self.population:
            s += ind.score
        return s
    
    def select_parent(self, sum_score):
        parent = -1
        draw = random.random() * sum_score
        s = 0
        i = 0
        while i < len(self.population) and s < draw:
            s += self.population[i].score
            parent += 1
            i += 1
        return parent

    def new_population(self, prob_mutation):
        s = self.sum_score()
        newpopulation = []
        for i in range(0, self.size_population, 2):
            p1_i = self.select_parent(s)
            p2_i = self.select_parent(s)
            son1, son2 = self.population[p1_i].crossover(self.population[p2_i])
            son1.mutation(prob_mutation)
            son2.mutation(prob_mutation)
            newpopulation.append(son1)
            newpopulation.append(son2)
            
        self.population = list(newpopulation)

    def solve(self, list_products, limit, num_generations, prob_mutation):
        self.init_population(list_products, limit)
        self.fit_population()
        self.sort_population()
        self.best_individual(self.population[0])
        self.result.append(self.best_solution.score)
        for i in range(num_generations):
            self.new_population(prob_mutation)
            self.fit_population()
            self.sort_population()
            self.best_individual(self.population[0])
            self.result.append(self.best_solution.score)
            self.print_generation()
        self.print_solution()

    def get_result(self):
        return self.result

    def print_generation(self):
        best = self.population[0]
        print('Generation: {} \n Chromosome: {} \n Score: {} \n Space: {}'.format(best.generation, best.chromosome, best.score, best.used_space))

    def print_solution(self):
        best = self.best_solution
        print('*'*20 + ' Best ' + '*'*20)
        print('Generation: {} \n Chromosome: {} \n Score: {} \n Space: {}'.format(best.generation, best.chromosome, best.score, best.used_space))
        for i, gene in enumerate(best.chromosome):
            if gene == '1':
                print(best.list_product[i].name)
    