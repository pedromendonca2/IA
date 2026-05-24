import numpy as np
import matplotlib.pyplot as plt

N_GENES = 30
SIZE_POPULACAO = 100
N_GERACOES = 1000
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.6

def fitness(individuo):
    summation_1 = np.sum(individuo ** 2)
    summation_2 = np.sum(np.cos(2*np.pi*individuo))

    result = -20 * np.exp(-0.2 * (summation_1 / N_GENES) ** 0.5) - np.exp(summation_2 / N_GENES) + 20 + np.e

    return result

def init_populacao():
    return np.random.uniform(-32, 32, size=(SIZE_POPULACAO, N_GENES)) # Ackley function

def mutation(pop):
    popi = []
    Ir1 = min(pop, key=fitness)

    for _ in range(SIZE_POPULACAO):
        Ir2 = pop[np.random.randint(SIZE_POPULACAO)]
        Ir3 = pop[np.random.randint(SIZE_POPULACAO)]

        V = Ir1 + MUTATION_RATE*(Ir2 - Ir3)

        popi.append(np.clip(V, -32, 32))

    return np.array(popi)

def crossover(pop, popi):
    popii = np.copy(pop)

    for i in range(SIZE_POPULACAO):
        for j in range(N_GENES):

            if np.random.rand() <= CROSSOVER_RATE:
                popii[i, j] = popi[i, j]
            else:
                popii[i, j] = pop[i, j]

    return popii

def selection(pop, popii):
    popb = np.copy(pop)

    for i in range(SIZE_POPULACAO):
        if fitness(popii[i]) < fitness(pop[i]):
            popb[i] = popii[i]
        else:
            popb[i] = pop[i]

    return popb

def run():
    pop = init_populacao()
    historico = []

    for _ in range(N_GERACOES):
        popi = mutation(pop)
        popii = crossover(pop, popi)
        popb = selection(pop, popii)
        pop = popb

        fitness_geracao = [fitness(ind) for ind in pop]
        historico.append(min(fitness_geracao))

    plt.plot(historico)
    plt.title("Evolução da Evolução Diferencial (Função Ackley)")
    plt.xlabel("Geração")
    plt.ylabel("Melhor Fitness")
    # plt.show()
    plt.savefig('evolucao.png')

    melhor_ind = min(pop, key=fitness)
    print(f"Melhor índice: {melhor_ind}\nMelhor fitness: {fitness(melhor_ind)}")

run()