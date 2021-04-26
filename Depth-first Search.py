'''Lucca Ianaguivara Kisanucki - 11201812090'''

from collections import defaultdict

class Grafo(object):
    def __init__(self):
        self.adj = defaultdict(set)
        self.visto = []

    def adicionarAresta(self, u, v):
        self.adj[u].add(v)
        self.adj[v].add(u)

    def existeAresta(self, u, v):
        return u in self.adj and v in self.adj[u]

    def DFS(self, v):
        self.visto.append(v)
        for x in self.adj[v]:
            if x not in self.visto:
                self.DFS(x)


grafo = Grafo()

numeroAeroportos = input()

numeroEntradas = input()

for x in range(0,int(numeroEntradas)):
    entrada = input()
    u = int(entrada.split()[0])
    v = int(entrada.split()[1])
    grafo.adicionarAresta(u,v)

saida = 0

grafo.DFS(0)

while(len(grafo.visto) < int(numeroAeroportos)):
    saida = saida + 1
    for x in range(0,int(numeroAeroportos)):
        if x not in grafo.visto:
            grafo.DFS(x)
            break


print('# de novos voos: ' +  str(saida))