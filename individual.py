import random
from product import Product


class Individual:
    def __init__(self, list_product, space_limit, generation=0):        
        self.list_product = list_product
        self.space_limit = space_limit
        self.generation = generation
        self.score = 0
        self.used_space = 0
        self.chromosome = []

        for i in range(len(self.list_product)):
            if random.random() < 0.5:
                self.chromosome.append('0')
            else:
                self.chromosome.append('1')

    def fitness(self):
        score = 0
        sum_spaces = 0

        for i in range(len(self.chromosome)):
            if self.chromosome[i] == '1':
                score += self.list_product[i].value
                sum_spaces += self.list_product[i].space
        
        if sum_spaces > self.space_limit:
            score = 1
        
        self.score = score
        self.used_space = sum_spaces
    
    def crossover(self, other):
        cut = round(random.random() * (len(self.chromosome) - 1))
        chrom_son1 = other.chromosome[0:cut] + self.chromosome[cut:]
        chrom_son2 = self.chromosome[0:cut] + other.chromosome[cut:]

        sons = [Individual(self.list_product, self.space_limit, self.generation + 1),
                 Individual(self.list_product, self.space_limit, self.generation + 1)] 

        sons[0].chromosome = chrom_son1
        sons[1].chromosome = chrom_son2

        return sons[0], sons[1]

    def mutation(self, rate):
        for i in range(len(self.chromosome)):
            if random.random() < rate:
                self.chromosome[i] = '1' if self.chromosome[i] == '0' else '0'
