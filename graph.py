import sys
from random import randint
class Graph:
    def __init__(_self, adjacency_matrix: list[list], cost_list: list[list], k: int):
        _self.adjacency_matrix = adjacency_matrix
        #_self.costs = cost_list
        _self.k = k
        
    def _floyd_warshall(_self):
        n = len(_self.adjacency_matrix)
        # Inicializar a matriz de distâncias com os custos conhecidos
        dist = [row[:] for row in _self.adjacency_matrix]
        # Atualizar as distâncias considerando os vértices intermediários
        for k in range(1, n):
            for i in range(1, n):
                for j in range(1, n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist
    
    def _find_centers(_self, centers, distances):
        current = centers[0]
        for i in range (1, int(_self.k)):
            greatest = 0
            greatestIndex = 0
            for j in  range (1, len(distances)):
                if(distances[current][j] > greatest and not j in centers):
                    greatest = distances[current][j] 
                    greatestIndex = j
            centers.append(greatestIndex)
            current = greatestIndex
            
    def k_centers_aproximado(_self):
        distances = _self._floyd_warshall()
        centers = []
        initial = randint(1, len(_self.adjacency_matrix))
        centers.append(initial)
        _self._find_centers(centers, distances)
        dists = []
        smaller = sys.maxsize
        for i in  range (1, len(distances)):
            for center in centers:
                if (distances[i][center] < smaller and i != center):
                    smaller = distances[i][center]
            dists.append(smaller)
        dists.sort()
        print(dists[(len(dists) -1)])
        print(centers)
        
    #def k_centers_preciso(_self):