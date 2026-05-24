import numpy as np

def distance(p1, p2):
    return pow((pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2)), 0.5)
      
class AStar():
    def __init__(self, matriz, source, target):
        self.mapa = np.array(matriz)
        self.custo = np.array(matriz, dtype=float)
        self.source = source
        self.target = target
        self.pais = {} 
        
    def custo_inicial(self):
        self.custo.fill(np.inf)
        self.custo[self.source] = 0
        self.pais[self.source] = None 
        
    def price(self, anterior, atual):
        return self.custo[anterior] + self.mapa[atual]
    
    def menor_custo(self, visitados):
        menor = visitados[0]
        f_menor = self.custo[menor] + distance(menor, self.target)
        
        for v in visitados:
            f_v = self.custo[v] + distance(v, self.target)
            if f_v < f_menor:
                f_menor = f_v
                menor = v
        return menor
            
    def run(self):
        self.custo_inicial()
        abertos = [self.source]
        linhas, colunas = self.mapa.shape
        
        while len(abertos) > 0:
            atual = self.menor_custo(abertos)
            abertos.remove(atual)
            
            if atual == self.target: 
                break
            
            direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for d in direcoes:
                v_x, v_y = atual[0] + d[0], atual[1] + d[1]
                vizinho = (v_x, v_y)
                
                if 0 <= v_x < linhas and 0 <= v_y < colunas:
                    if self.mapa[vizinho] != -1:
                        custo_estimado = self.price(atual, vizinho)
                        
                        if self.custo[vizinho] > custo_estimado:
                            self.custo[vizinho] = custo_estimado
                            self.pais[vizinho] = atual 
                            
                            if vizinho not in abertos:
                                abertos.append(vizinho)
                    
        print(f"Custo do caminho: {self.custo[self.target]}", )
        self.imprimir_caminho()

    def imprimir_caminho(self):
        if self.target not in self.pais:
            print("Não foi possível encontrar um caminho até o destino.")
            return

        caminho = []
        atual = self.target
        
        while atual is not None:
            caminho.append(atual)
            atual = self.pais[atual]
        
        caminho = caminho[::-1]
        
        print("Caminho encontrado:")
        print(caminho)

# =================================================================================================================================

astar_matriz = np.array([
    [ 1,  2,  1,  1,  1,  2],
    [ 1, -1,  2, -1,  3,  1],
    [ 1,  4, 15, -1, -1,  1],
    [ 2, -1, 15, -1,  4,  1],
    [-1, -1,  2,  2,  9,  2],
    [-1, -1, -1, -1,  0,  1]
]).astype(float)

def main():
    astar = AStar(astar_matriz, (0,0), (5,4))
    astar.run()

if __name__ == '__main__':
    main()