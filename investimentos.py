
import random


def funcao_lucro(sol):
    xA, xB, xC, xD = sol
    return 50*xA - 1.2*xA*xA + 45*xB - 1.0*xB*xB + 40*xC - 0.8*xC*xC + 55*xD - 1.5*xD*xD


def verifica_restricoes(sol):
    xA, xB, xC, xD = sol

    if min(sol) < 0:
        return False

    horas_mensais = 2*xA + 1*xB + 3*xC + 2*xD
    investimento_max = xC + xD
    bucket_max = xA + xB + xC + xD

    return investimento_max <= 25 and bucket_max <= 50 and horas_mensais <= 80


def gerar_vizinhos(sol):
    """
    Gera vizinhos da solução atual, alterando a quantidade de cada produto em +1 ou -1.
    A função recebe uma tupla (xA, xB, xC) e retorna uma lista de tuplas representando os vizinhos válidos.
    Observe que os vizinhos gerados devem atender às restrições do problema, ou seja, devem ser soluções válidas.
    """
    vizinhos = []

    for i in range(4):
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
    
    atual = (0, 0, 0, 0)

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
    print(f"Produto D: {solucao[3]}")
    print(f"Lucro Máximo: R$ {funcao_lucro(solucao)}")