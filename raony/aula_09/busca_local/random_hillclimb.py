import numpy as np
import time

K = 1000

"""
    Algoritmo feito seguindo as instruções do matéria da aula 09: algoritmos de busca
    O exemplo do algoritmo é feito tendo em base o o exercício proposto ao final do slide
    
    As versões do hill climb:
        1. Random Restart: roda várias vezes com entradas aleatórias (IMPLEMENTADA NESTE ARQUIVO)
        2. Stochastic: escolhere um vizinho aleatório invés do vizinho com maior fitness
        3. Annealing: ajuste com temperatura para aceitar alguns valores piores probabilisticamente e fugir de máximos locais
        4. Hybrid: uso do algoritmo Simulated Annealing com o Hill Climb
"""
class HillClimb():
    def __init__(self, solucao_inicial = None):
        self.solucao_inicial = solucao_inicial
        
    def restricoes(self, solucao):
        A, B, C = solucao
        
        maximo_horas    = (A*2  + B*4  + C*3) <= 100
        maximo_recurso  = (A*3  + B*2  + C*4) <= 90
        variaveis       = (A >= 0) and (B >= 0) and (C >= 0)
        
        return maximo_horas and maximo_recurso and variaveis
    
    def fitness(self, solucao):
        if self.restricoes(solucao): return solucao[0]*30 + solucao[1]*50 + solucao[2]*40
        else: return 0
        
    def gera_vizinhos(self, solucao):
        vizinhos = []
        
        for i in range(len(solucao)):
            for inc in [-1, 1]:
                vizinho = list(solucao)
                vizinho[i] += inc
                
            if self.restricoes(vizinho): vizinhos.append(vizinho)
        return vizinhos
    
    def gera_solucao_inicial(self):
        while True:
            a = np.random.randint(0, 91)
            b = np.random.randint(0, 91)
            c = np.random.randint(0, 91)
            
            if self.restricoes((a,b,c,)): return (a,b,c)
    
    def run(self):
        atual = self.solucao_inicial
        if atual is None: atual = self.gera_solucao_inicial()
        
        while True:
            vizinhos = self.gera_vizinhos(atual)
            if len(vizinhos) <= 0: break
            
            melhor_vizinho = max(vizinhos, key=self.fitness)
            if self.fitness(melhor_vizinho) <= self.fitness(atual): break
            
            atual = melhor_vizinho
            
        return self.fitness(atual), atual
        
    def multiple_run(self):
        fitness, solucao = 0, None
        N = 100
        t0 = time.time()
        for _ in range(N):
            fitness_nova, solucao_nova = self.run()
            if fitness_nova > fitness:
                fitness, solucao = fitness_nova, solucao_nova
        t1 = time.time()
        print(f"Tempo de execução para {N} : {t1-t0:.2f}")
        print(f"Melhor solução: {fitness} : {solucao}")
            
def main():
    hillclimb = HillClimb()
    hillclimb.multiple_run()

if __name__ == '__main__':
    main()