import numpy as np

def AnnealingHillClimb():
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