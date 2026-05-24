
import random


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


def gerar_vizinhos(sol):
    """
    Gera vizinhos da solução atual, alterando a quantidade de cada produto em +1 ou -1.
    A função recebe uma tupla (xA, xB, xC) e retorna uma lista de tuplas representando os vizinhos válidos.
    Observe que os vizinhos gerados devem atender às restrições do problema, ou seja, devem ser soluções válidas.
    """
    vizinhos = []

    for i in range(3):
        for delta in [-1, 1]:
            nova = list(sol)
            nova[i] += delta

            if verifica_restricoes(nova):
                vizinhos.append(tuple(nova))

    return vizinhos


def hill_climbing():
    """
    Implementa o algoritmo de Hill Climbing para encontrar a melhor solução para o problema de otimização.
    A função inicia com uma solução inicial (0, 0, 0) e iterativamente gera vizinhos, escolhendo o melhor vizinho com base na função de lucro. 
    O processo continua até que não haja vizinhos melhores ou até que não haja mais vizinhos válidos para explorar.
    """
    
    atual = (0, 0, 0)

    while True:
        vizinhos = gerar_vizinhos(atual)

        if not vizinhos:
            break

        melhor = max(vizinhos, key=funcao_lucro)

        if funcao_lucro(melhor) <= funcao_lucro(atual):
            break

        atual = melhor

    return atual


if __name__ == "__main__":
    
    solucao = hill_climbing()

    print("Melhor plano de produção encontrado:")
    print(f"Produto A: {solucao[0]}")
    print(f"Produto B: {solucao[1]}")
    print(f"Produto C: {solucao[2]}")
    print(f"Lucro Máximo: R$ {funcao_lucro(solucao)}")