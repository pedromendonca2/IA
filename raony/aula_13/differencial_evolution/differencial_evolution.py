import numpy as np

N_GENES = N = 30
N_POPULACAO = 100
N_GERACOES = 4000

def fitness(individuo):
    somatorio1 = 1/N * np.sum(individuo**2)
    somatorio2 = 1/N * np.sum(np.cos(2 * np.pi * individuo))
    return -20 * np.exp(-0.2 * np.sqrt(somatorio1)) - np.exp(somatorio2) + 20 + np.e

def gera_populacao():
    return np.random.uniform(-32, 32, size=(N_POPULACAO, N_GENES))

def selecao(pop_crossover, pop_inicial):
    pop_intermediaria = np.zeros_like(pop_inicial)
    
    for i in range(N_POPULACAO):
        fitness_crossover = fitness(pop_crossover[i])
        fitness_original = fitness(pop_inicial[i])

        if fitness_crossover < fitness_original: pop_intermediaria[i] = pop_crossover[i]
        else:                                    pop_intermediaria[i] = pop_inicial[i]
        
    return pop_intermediaria

def crossover(pop_mutada, pop_inicial, txCrossover = 0.7):
    pop_intermediaria = np.zeros_like(pop_inicial)
    for i in range(N_POPULACAO):
        gene_obrigatorio = np.random.randint(N_GENES)
        for j in range(N_GENES):
            if np.random.rand() <= txCrossover or j == gene_obrigatorio: pop_intermediaria[i][j] = pop_mutada[i][j]
            else:                                                        pop_intermediaria[i][j] = pop_inicial[i][j]

    return pop_intermediaria

        
def mutacao(pop_inicial, txMutacao = 0.7):
    pop_intermediaria = np.zeros_like(pop_inicial)
    individuo_1 = min(pop_inicial, key=fitness)
    for i in range(N_POPULACAO):
        indices_possiveis = [idx for idx in range(N_POPULACAO) if idx != i]
        individuo_2_idx, individuo_3_idx = np.random.choice(indices_possiveis, 2, replace=False)
        individuo_2, individuo_3 = pop_inicial[individuo_2_idx], pop_inicial[individuo_3_idx]

        mutante = individuo_1 + txMutacao*(individuo_2 - individuo_3)
        pop_intermediaria[i] = np.clip(mutante, -32, 32)
    
    return pop_intermediaria

def run():
    pop_inicial = gera_populacao()
    
    for _ in range(N_GERACOES):
        pop_intermediaria_1 = mutacao(pop_inicial)
        pop_intermediaria_2 = crossover(pop_intermediaria_1, pop_inicial)
        pop_inicial = selecao(pop_intermediaria_2, pop_inicial)
        
    melhor_individuo = min(pop_inicial, key=fitness)
    print(fitness(melhor_individuo))
            
run()