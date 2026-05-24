import random
import math


def funcao_lucro(sol):
    """
    Função objetivo: calcula o lucro total com base na quantidade de cada produto.
    Produto A: R$ 30 por unidade
    Produto B: R$ 50 por unidade
    Produto C: R$ 40 por unidade

    A função recebe uma tupla (xA, xB, xC) representando a quantidade de cada produto e retorna o lucro total.
    """
    xA, xB, xC = sol
    return 30*xA + 50*xB + 40*xC


def verifica_restricoes(sol):
    """
    Verifica se a solução atende às restrições do problema.
    Restrições:
    1. Horas de máquina: 2xA + 4xB + 3xC <= 100
    2. Matéria-prima: 3xA + 2xB + 4xC <= 90
    3. Quantidade de produtos não pode ser negativa (xA, xB, xC >= 0)

    A função recebe uma tupla (xA, xB, xC) e retorna True se a solução for válida, ou False caso contrário.
    """
    xA, xB, xC = sol

    if min(sol) < 0:
        return False

    horas_maquina = 2*xA + 4*xB + 3*xC
    materia_prima = 3*xA + 2*xB + 4*xC

    return horas_maquina <= 100 and materia_prima <= 90


# -----------------------------
# Vizinho Aleatório
# -----------------------------
def vizinho_aleatorio(sol):
    """
    Gera um vizinho aleatório da solução atual, alterando a quantidade de um produto em +1 ou -1.
    A função recebe uma tupla (xA, xB, xC) e retorna uma nova tupla representando um vizinho válido. O processo continua até que
    um vizinho válido seja encontrado.
    """
    while True:
        nova = list(sol)

        i = random.randint(0, 2)
        delta = random.choice([-1, 1])

        nova[i] += delta

        if verifica_restricoes(nova):
            return tuple(nova)


def simulated_annealing():
    """
    Implementa o algoritmo de Simulated Annealing para encontrar a melhor solução para o problema de otimização.
    A função inicia com uma solução inicial (0, 0, 0) e iterativamente gera vizinhos, aceitando soluções piores com uma certa probabilidade.
    O processo continua até que a temperatura atinja um valor mínimo.
    """
    atual = (0, 0, 0)
    melhor = atual

    T = 100.0 # Temperatura inicial
    T_min = 0.01 # Temperatura mínima
    alpha = 0.95 # Taxa de resfriamento (cooling rate)

    while T > T_min:
        candidato = vizinho_aleatorio(atual)

        delta = funcao_lucro(candidato) - funcao_lucro(atual)

        if delta > 0:
            atual = candidato
        else:
            prob = math.exp(delta / T)

            if random.random() < prob:
                atual = candidato

        if funcao_lucro(atual) > funcao_lucro(melhor):
            melhor = atual

        T *= alpha

    return melhor



if __name__ == "__main__":

    solucao = simulated_annealing()

    print("Melhor solução encontrada:")
    print(f"Produto A: {solucao[0]}")
    print(f"Produto B: {solucao[1]}")
    print(f"Produto C: {solucao[2]}")
    print(f"Lucro: R$ {funcao_lucro(solucao)}")