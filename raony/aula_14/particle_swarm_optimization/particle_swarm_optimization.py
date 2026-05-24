import numpy as np

N_POPULACAO = 100
N_GENES = N = 30
N_GERACOES = 1000

W = 0.6
C1 = C2 = 2.05
V_MAX = 6.4

def fitness(individuo):
    somatorio1 = 1/N * np.sum(individuo**2)
    somatorio2 = 1/N * np.sum(np.cos(2 * np.pi * individuo))
    resultado = -20 * np.exp(-0.2 * np.sqrt(somatorio1)) - np.exp(somatorio2) + 20 + np.e

    return resultado

def gera_populacao():
    return np.random.uniform(low=-32, high=32, size=(N_POPULACAO, N_GENES))

def atualiza_velocidade(posicao_inicial, velocidade_inicial, pbest, gbest):
    velocidade_intermediaria = np.zeros_like(velocidade_inicial)
    
    r1 = np.random.rand(N_POPULACAO, N_GENES)
    r2 = np.random.rand(N_POPULACAO, N_GENES)
    
    velocidade_intermediaria = (
        W * velocidade_inicial + 
        C1 * r1 * (pbest - posicao_inicial) +
        C2 * r2 * (gbest - posicao_inicial)
    )
    
    return velocidade_intermediaria

def atualiza_posicao(posicao_inicial, velocidade_inicial):
    posicao_intermediaria = np.zeros_like(posicao_inicial)
    posicao_intermediaria = posicao_inicial + velocidade_inicial
    return np.clip(posicao_intermediaria, -32, 32)

def atualiza_bests(posicao_inicial, pbest, gbest):
    for i in range(N_POPULACAO):
        if fitness(posicao_inicial[i]) < fitness(pbest[i]):
            pbest[i] = posicao_inicial[i]
            
            if fitness(pbest[i]) <  fitness(gbest):
                gbest = np.copy(pbest[i])
                
    return pbest, gbest
        

def run():
    posicao_inicial = gera_populacao()
    velocidade_inicial = np.zeros_like(posicao_inicial)
    pbest = np.copy(posicao_inicial)
    gbest = np.copy(posicao_inicial[0])
    
    for _ in range(N_GERACOES):
        pbest, gbest = atualiza_bests(posicao_inicial, pbest, gbest)
        velocidade_inicial = atualiza_velocidade(posicao_inicial, velocidade_inicial, pbest, gbest)
        posicao_inicial = atualiza_posicao(posicao_inicial, velocidade_inicial)
        
    print(f"Melhor fitness: {fitness(gbest)}")


run()