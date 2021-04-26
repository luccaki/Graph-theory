from collections import defaultdict

class Grafo(object):
    def __init__(self):
        self.adj = defaultdict(set)

    def adicionarAresta(self, u, v):
        self.adj[u].add(v)
        self.adj[v].add(u)

    def existeAresta(self, u, v):
        return u in self.adj and v in self.adj[u]

grafo = Grafo()

numeroFuncionarios = input()

numeroEntradas = input()

for x in range(0,int(numeroEntradas)):
    entrada = input()
    u = int(entrada.split()[0])
    v = int(entrada.split()[1])
    grafo.adicionarAresta(u,v)

def function():
    for x in range(0,int(numeroFuncionarios)):
        for y in range(1,int(numeroFuncionarios)-x):
            if grafo.existeAresta(x,x+y):
                for z in range(1,int(numeroFuncionarios)-x):
                    if grafo.existeAresta(x,x+z) and grafo.existeAresta(x+y,x+z):
                        return True
    return False

if function():
    print("VAI TER CASAMENTO!")
else:
    print("NAO VAI TER CASAMENTO")