import numpy as np

class StochasticHillClimb():
    
    
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
        
    def gera_solucao_inicial(self):
        while True:
            
            a = np.random.randint(0, 91)
            b = np.random.randint(0, 91)
            c = np.random.randint(0, 91)
            
            if self.restricoes((a,b,c,)): return (a,b,c)
            
    def gera_vizinhos(self, solucao):
        vizinhos = []
        for i in range(3):
            for inc in [-1, 1]:
                novo = list(solucao)
                novo[i] += inc
                
                if self.restricoes(novo): vizinhos.append(novo)
                
        return vizinhos
        
    def run(self):
        atual = self.solucao_inicial
        if atual is None: atual = self.gera_solucao_inicial()
        
        while True:
            vizinhos = self.gera_vizinhos(atual)
            vizinhos.sort(key=self.fitness)
            
            idx = np.random.randint(0, len(vizinhos)//2)
            avaliado = vizinhos[idx]
            
            if self.fitness(avaliado) <= self.fitness(atual): break
            
            atual = avaliado
            
        print(self.fitness(atual), atual)
    
    
def main():
    hillclimb = StochasticHillClimb()
    hillclimb.run()

if __name__ == '__main__':
    main()