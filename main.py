from reader import Reader
from graph import Graph
import time

option = -1
path = ''
while option != 0:
    option = int(input("Insira 1 caso queira passar um path de grafo ou 0 para finalizar: "))
    if option == 1:
        path = input("Insira o caminho (as barras devem ser assim /): ")
    elif option == 0:
        break
    else:
        continue
    reader = Reader(path)
    graph = Graph(reader.lista_de_adjancenia, reader.costs, reader.k)
    method_option = -1
    while method_option != 0:
        method_option = int(input("Insira 1 caso queira o método aproximado, 2 para o preciso ou 0 para finalizar: "))
        if method_option == 1:
            start = time.time()
            graph.k_centers_aproximado()
            end = time.time()
            print("Tempo de execucação: ", (end - start) * 10**3, "ms")
        elif method_option == 2:
            start = time.time()
            graph.k_centros_exato()
            end = time.time()
            print("Tempo de execucação: ", (end - start) * 10**3, "ms")
        elif method_option == 0:
            break
        else:
            continue