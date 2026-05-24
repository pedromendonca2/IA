import numpy as np

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
    return np.random.uniform(-32, 32, size=(SIZE_POPULACAO, N_GERACOES))

def selection(popp):
    popi = []

    for _ in range(SIZE_POPULACAO):
        ind_a = popp[np.random.randint(SIZE_POPULACAO)]
        ind_b = popp[np.random.randint(SIZE_POPULACAO)]
        if fitness(ind_a) < fitness(ind_b):
            popi.append(ind_a)
        else:
            popi.append(ind_b)

    return popi

def crossover(popi):
    c1 = popi [ np.random.choice(popi) ]
    c2 = popi [ np.random.choice(popi) ]

    popii = []

    for _ in range(SIZE_POPULACAO):
        if np.random.rand() <= CROSSOVER_RATE:
            beta = np.random.randint(N_GENES)
            p1 = beta * c1 + (1 - beta) * c2
            p2 = (1 - beta) * c1 + beta * c2
        else:
            p1 = c1, p2 = c2

        popii.add(p1)
        popii.add(p2)

    return popii

def mutation(popii):
    poppp = np.copy(popii)

    for i in range(len(poppp)):
        if np.random.rand() <= MUTATION_RATE:
            alpha = np.random.randint(N_GENES)
            poppp[i] *= alpha

    return poppp


def run():
    popp = init_populacao()

    for _ in range(N_GERACOES):

        popi = selection(popp)

        popii = crossover(popi)

        poppp = mutation(popii)

        popp = poppp

    melhor_ind = min(popp, key=fitness)
    # print(melhor_ind)
    print(f"Melhor fitness: {fitness(melhor_ind)}")

run()