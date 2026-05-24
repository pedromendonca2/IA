import numpy as np

N_GENES = N = 30
N_POPULACAO = 100
N_GERACOES = 1000

def fitness(individuo):
    somatorio1 = 1/N * np.sum(individuo**2)
    somatorio2 = 1/N * np.sum(np.cos(2 * np.pi * individuo))
    resultado = -20 * np.exp(-0.2 * np.sqrt(somatorio1)) - np.exp(somatorio2) + 20 + np.e

    return resultado

def gera_populacao():
    return np.random.uniform(-32, 32, size=(N_POPULACAO, N_GENES))

def selecao(pop_inicial):
    pop_intermediaria = []
    
    while len(pop_intermediaria) < N_POPULACAO:
        ind_1 = pop_inicial[ np.random.randint(N_POPULACAO) ]
        ind_2 = pop_inicial[ np.random.randint(N_POPULACAO) ]
        
        pop_intermediaria.append(ind_1) if fitness(ind_1) < fitness(ind_2) else pop_intermediaria.append(ind_2)
        
    return pop_intermediaria

def crossover(pop_inicial, txCrossover = 0.7):
    pop_intermediaria = []
    while len(pop_intermediaria) < N_POPULACAO:
        pai_1 = pop_inicial[ np.random.randint(N_POPULACAO) ]
        pai_2 = pop_inicial[ np.random.randint(N_POPULACAO) ]
        
        if np.random.rand() <= txCrossover:
            mid = np.random.randint(N_GENES)
            filho_1 = np.concatenate((pai_1[:mid], pai_2[mid:]))
            filho_2 = np.concatenate((pai_2[:mid], pai_1[mid:]))
            
            pop_intermediaria.append(filho_1)
            if len(pop_intermediaria) < N_POPULACAO: pop_intermediaria.append(filho_2)
            
        else:
            pop_intermediaria.append(pai_1)
            if len(pop_intermediaria) < N_POPULACAO: pop_intermediaria.append(pai_2)
        
    return pop_intermediaria

def mutacao(pop_inicial, txMutacao = 0.1):
    pop_intermediaria = np.copy(pop_inicial)
    for individuo in pop_intermediaria:
        for i in range(N_GENES):
            if np.random.rand() > txMutacao: continue
            
            individuo[i] += np.random.normal()
            individuo[i] = np.clip(individuo[i], -32, 32)
        
    return pop_intermediaria

def run():
    pop_inicial = gera_populacao()
    
    for _ in range(N_GERACOES):
        melhor_da_geracao = min(pop_inicial, key=fitness).copy()

        pop_intermediaria = selecao(pop_inicial)
        pop_intermediaria_2 = crossover(pop_intermediaria)
        pop_nova = mutacao(pop_intermediaria_2)

        pior_idx = max(range(N_POPULACAO), key=lambda i: fitness(pop_nova[i]))
        pop_nova[pior_idx] = melhor_da_geracao
        
        pop_inicial = pop_nova
        
    melhor_ind = min(pop_inicial, key=fitness)
    print(melhor_ind)
    print(fitness(melhor_ind))
    
run()