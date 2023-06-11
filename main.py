from reader import Reader
from graph import Graph
reader = Reader("C:/Users/mathe/Downloads/pmed1.txt")
graph = Graph(reader.lista_de_adjancenia, reader.costs, reader.k)
graph.k_centers_preciso()