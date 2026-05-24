import numpy as np
import matplotlib.pyplot as plt

N_GENES = 30
SIZE_POPULACAO = 100
N_GERACOES = 1000
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.1

def fitness(individuo):
    summation_1 = np.sum(individuo ** 2)
    summation_2 = np.sum(np.cos(2*np.pi*individuo))

    result = -20 * np.exp(-0.2 * (summation_1 / N_GENES) ** 0.5) - np.exp(summation_2 / N_GENES) + 20 + np.e

    return result

def init_populacao():
    return np.random.uniform(-32, 32, size=(SIZE_POPULACAO, N_GENES)) # Ackley function

def selection(popp):
    popi = []

    for _ in range(SIZE_POPULACAO):
        ind_a = popp[np.random.randint(SIZE_POPULACAO)]
        ind_b = popp[np.random.randint(SIZE_POPULACAO)]
        if fitness(ind_a) < fitness(ind_b):
            popi.append(ind_a)
        else:
            popi.append(ind_b)

    return np.array(popi)

def crossover(popi):
    popii = []

    for _ in range(SIZE_POPULACAO // 2):
        c1 = popi[np.random.randint(SIZE_POPULACAO)]
        c2 = popi[np.random.randint(SIZE_POPULACAO)]

        if np.random.rand() <= CROSSOVER_RATE:
            beta = np.random.randint(N_GENES)
            p1 = np.concatenate([c1[:beta], c2[beta:]])
            p2 = np.concatenate([c2[:beta], c1[beta:]])
        else:
            p1, p2 = c1.copy(), c2.copy()

        popii.append(p1)
        popii.append(p2)

    return np.array(popii)

def mutation(popii):
    poppp = np.copy(popii)

    for i in range(SIZE_POPULACAO):
        if np.random.rand() <= MUTATION_RATE:
            alpha = np.random.normal(1, 0.1)
            poppp[i] *= alpha
            poppp[i] = np.clip(poppp[i], -32, 32) #serve pra não estourar, fica entre -32 e 32

    return poppp


def run():
    popp = init_populacao()
    historico = []

    for _ in range(N_GERACOES):
        popi = selection(popp)
        popii = crossover(popi)
        poppp = mutation(popii)
        popp = poppp

        fitness_geracao = [fitness(ind) for ind in popp]
        historico.append(min(fitness_geracao))

    plt.plot(historico)
    plt.title("Evolução do Algoritmo Genético (Função Ackley)")
    plt.xlabel("Geração")
    plt.ylabel("Melhor Fitness")
    # plt.show()
    plt.savefig('evolucao.png')

    melhor_ind = min(popp, key=fitness)
    print(f"Melhor índice: {melhor_ind}\nMelhor fitness: {fitness(melhor_ind)}")

run()