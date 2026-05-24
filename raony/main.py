import numpy as np
import math

V = np.array([2.5, 5,  7.5, 10,  12.5, 15, 17.5, 20,  22.5, 25]) / 1000 # vazao acumulada normalizada
C = np.array([20,  54, 98,  120, 34,   12, 88,   122, 33,   40]) # comprimento

D = np.array([150, 200, 250, 300, 400]) # diametro
P = np.array([65,  98,  150, 210, 340]) # preco

def q_max(d):
    n = 0.013
    a = math.pi * pow(d, 2)
    Rh = d/4
    s = 0.005
    return 1/n * a * pow(Rh, 2/3) * pow(s, 1/2)

def fitness(individuo):
    pass

def generic_algorithm(pop, crossover_tx, mutation_tx):
    pass

def main():
    pass

