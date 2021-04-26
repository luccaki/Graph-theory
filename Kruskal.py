#Lucca Ianaguivara Kisanucki - 11201812090

#Esse programa recebe como entrada um 'Numero de Entradas' e para cada numero ele recebe uma coordenada X e Y de um ponto em um plano
#O Objetivo desse programa é pegar todos esses pontos e conectar todos eles de forma que o comprimento entre os pontos seja o menor possivel
#Gerando uma Minimum spanning tree
#A saida do programa é a soma do comprimento entre todos os pontos, e qual ponto conectou com qual de forma crescente

#Importação do Collections para criar a Lista de Adjacência
from collections import defaultdict
#Importação do math para facilitar na conta da Raiz Quadrada (usada para determinar a distancia entre os pontos)
import math

#Classe que representa o Grafo
class Grafo:
    def __init__(self):
        self.grafo = []

    # função para adicionar uma aresta no grafo
    def adicionaAresta(self, u, v, p):
        self.grafo.append([u, v, p])
 
    # função recursiva para procurar o representante de i
    def procura(self, lista, i):
        if lista[i] == i:
            return i
        return self.procura(lista, lista[i])
 
    # algoritmo de Kruskal em si
    def kruskal(self):
        MST = []  # vetor MST final que ira armazenar todas as arestas
        i = 0 # variavel para incrementar
        visto = 0 # guarda o numero de vertices visto
        self.grafo = sorted(self.grafo,key=lambda item: item[2]) # ordena o grafo conforme o peso

        listaRepres = [] #lista dos representantes por index
        for item in range(0,int(numeroEntradas)): #Inicia as lista dos representes
            listaRepres.append(item) #cada aresta é seu proprio representante inicial
        
        while visto < int(numeroEntradas) - 1: # enquanto ter vertices não visto
            u, v, p = self.grafo[i] #pega o menor vertice
            i = i + 1 #incrementar para pegar o proximo menor vertice
            representante1 = self.procura(listaRepres, u) #procura o representante do componente que contem u
            representante2 = self.procura(listaRepres, v) #procura o representante do componente que contem v
            if representante1 != representante2: #verifica se u e v são de componentes distintos
                if u < v: #adiciona na MST de forma pré ordenada
                    MST.append([u, v, p])
                else:
                    MST.append([v, u, p])
                visto += 1 # +1 vertice visto
                listaRepres[representante1] = representante2 # faz a uniao dos componentes, muda o representante na lista
        return MST

#Leitura do numero de entradas
numeroEntradas = input()

#Nova instancia da classe Grafo
grafo = Grafo()

#Cria uma lista para guardar as entradas
entrada = list()

#Para cada entrada adiciona 'X Y' na lista
for x in range(int(numeroEntradas)):
    entrada.append(input())

#Para cada coordenada 'X Y' na lista, faz o calculo do peso entre dois pontos diferentes e adiciona no Grafo
for x in range(len(entrada)):
    for y in range(x+1,len(entrada)):
        x1 = int(entrada[x].split()[0])
        x2 = int(entrada[x].split()[1])
        y1 = int(entrada[y].split()[0])
        y2 = int(entrada[y].split()[1])
        peso = math.sqrt((x1-y1)**2+(x2-y2)**2)
        grafo.adicionaAresta(x,y,peso)

#Chama a função do algoritmo de Kruskal e retorna a MST que é salva em 'MST'
MST = grafo.kruskal()

#ordena as arestas da MST
MST = sorted(MST, key=lambda item: item[1])
MST = sorted(MST, key=lambda item: item[0])

pesoTotal = 0 #variavel para armazenas o peso total
for u, v, peso in MST: #Somatoria dos pesos
    pesoTotal += peso
print('comprimento de cabeamento minimo: ' + "{:.4f}".format(pesoTotal)) # printa o peso total

#Para cada item um resultado, printa as coordenadas de forma crescente
for item in MST:
    print(str(item[0]) + ' ' + str(item[1]))