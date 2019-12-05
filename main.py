import matplotlib.pyplot as pyplot
from product import Product
from genetic import GeneticAlgorithm


if __name__ == '__main__':
    list_products = []
    list_products.append(Product('Geladeira Dako', 0.751, 999.90))
    list_products.append(Product('Iphone 6', 0.0000899, 2911.12))
    list_products.append(Product('TV 55', 0.400, 4346.99))
    list_products.append(Product('TV 50', 0.290, 3999.90))
    list_products.append(Product('TV 42', 0.200, 2999.00))
    list_products.append(Product('Notebook Dell', 0.00350, 2499.90))
    list_products.append(Product('Ventilador Panasonic', 0.496, 199.90))
    list_products.append(Product('Microondas Eletrolux', 0.0424, 308.66))
    list_products.append(Product('Microondas LG', 0.0544, 429.90))
    list_products.append(Product('Microondas Panasonic', 0.0319, 299.29))
    list_products.append(Product('Geladeira Brastemp', 0.635, 849.00))
    list_products.append(Product('Geladeira Consul', 0.870, 1199.89))
    list_products.append(Product('Notebook Lenovo', 0.498, 1999.90))
    list_products.append(Product('Notebook Asus', 0.527, 3999.00))

    limit = 3
    size_population = 200
    prob_mutation = 0.01
    num_generations = 100

    ga = GeneticAlgorithm(size_population)
    ga.solve(list_products, limit, num_generations, prob_mutation)
    
    pyplot.plot(ga.get_result())
    pyplot.title('Improvment through generations')
    pyplot.show()