import os
import re
import sys

class Reader:
    def __init__(_self, path:str):
        _self.k = 0
        _self.lista_de_adjancenia = []
        _self.costs = []
        _self._trata_arquivo(path)
        
    def _readFile(_self, path:str) -> list:
        inputs = []
        with open(path, 'r') as f:
            for line in f:
                inputs.append(line.strip())
        return inputs
    
    #matriz de adjacencia com pesos
    def _trata_arquivo(_self, path:str):
        lines = _self._readFile(path)
        params = re.findall(r'\d+', lines.pop(0)) 
        _self.k = params[2]
        _self.lista_de_adjancenia =  [[sys.maxsize for _ in range(int(params[0]) + 1)] for _ in range(int(params[0]) + 1)] 
        for i in range(1, int(params[0])):
            _self.lista_de_adjancenia[i][i] = 0
        for line in lines:
            values = re.findall(r'\d+', line)
            _self.lista_de_adjancenia[int(values[0])][int(values[1])] = int(values[2])
    
    # lista de adjacencia
    # def _trata_arquivo(_self, path:str):
    #     lines = _self._readFile(path)
    #     params = re.findall(r'\d+', lines.pop(0)) #recebe n vertices, n arestas e k, enquanto remove  a linha
    #     _self.k = params[2] # pega o k
    #     _self.lista_de_adjancenia = [[] for _ in range(int(params[0]) + 1)] #inicia a lista de adjacencia com n posicoes
    #     _self.costs = [[] for _ in range(int(params[0]) + 1)] #inicia a lista de custa com as mesmas n posicoes
    #     for line in lines:
    #         values = re.findall(r'\d+', line)
    #         _self.lista_de_adjancenia[int(values[0])].append(int(values[1])) #dando append no vertice final na lista do vertice de origem
    #         _self.costs[int(values[0])].append(int(values[2])) #dando append do custo da aresta na lista do vertice de origem, na mesma posicao do vertice final