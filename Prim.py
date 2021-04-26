#Lucca Ianaguivara Kisanucki - 11201812090

#Esse programa recebe como entrada um 'Numero de Entradas' e para cada numero ele recebe uma coordenada X e Y de um ponto em um plano
#O Objetivo desse programa é pegar todos esses pontos e conectar todos eles de forma que o comprimento entre os pontos seja o menor possivel
#Gerando uma Minimum spanning tree
#A saida do programa é a soma do comprimento entre todos os pontos, e qual ponto conectou com qual de forma crescente

#Importação do Collections para criar a Lista de Adjacência
from collections import defaultdict
#Importação do math para facilitar na conta da Raiz Quadrada (usada para determinar a distancia entre os pontos)
import math

#Função para tirar o elemento minimo da Heap
def heappop(heap):
    ultimo = heap.pop()
    if heap:
        saida = heap[0]
        heap[0] = ultimo
        corrigeDescendo(heap, 0)
        return saida
    return ultimo

#Função Corrige Subindo da Heap
def corrigeSubindo(heap, inicial, pos):
    global listaIndex
    aux = heap[pos]
    while pos > inicial:
        posPai = (pos - 1) >> 1
        pai = heap[posPai]
        if aux < pai:
            heap[pos] = pai
            listaIndex[heap[pos][2]] = pos #Atualiza o index na listaIndex[] dos vertices
            pos = posPai
            continue
        break
    heap[pos] = aux
    listaIndex[heap[pos][2]] = pos #Atualiza o index na listaIndex[] dos vertices

#Função Corrige Descendo da Heap
def corrigeDescendo(heap, pos):
    final = len(heap)
    inicial = pos
    aux = heap[pos]
    posFilho = 2*pos + 1
    while posFilho < final:
        posDir = posFilho + 1
        if posDir < final and not heap[posFilho] < heap[posDir]:
            posFilho = posDir
        heap[pos] = heap[posFilho]
        listaIndex[heap[pos][2]] = pos #Atualiza o index na listaIndex[] dos vertices
        pos = posFilho
        posFilho = 2*pos + 1
    heap[pos] = aux
    listaIndex[heap[pos][2]] = pos #Atualiza o index na listaIndex[] dos vertices
    corrigeSubindo(heap, inicial, pos)

#Função para transformar uma lista em Heap, faz a ordenação da lista inteira
def heap(x):
    n = len(x)
    for i in reversed(range(n//2)):
        corrigeDescendo(x, i)

#Classe que representa o Grafo
class Grafo(object):
    def __init__(self,vertices):
        self.adj = [[] for item  in range(vertices)]

    #Função para adicionar uma aresta não direcionada
    def adicionarAresta(self, u, v, peso):
        self.adj[u].append((v, peso))
        self.adj[v].append((u, peso))
    
    #Retorna o peso da aresta
    def peso(self, u, v):
        for item in self.adj[u]:
            if item[0] == v:
                return item[1]

#Variavel global para uma lista de todos os index dos vertices
listaIndex = []
#Variavel global para somatoria do peso("comprimeto")
pesoTotal = 0

#Implementação do Algoritmo de Prim
def algoritmoPrim(grafo):
    global pesoTotal
    global listaIndex
    pesoLista = [0] #Lista do peso de todos os vertices, da MST até o vertice
    for x in range(len(grafo.adj)): #Inicia todos os index da listaIndex com '-1', só para ter um valor salvo e podermos manipular direto depois
        listaIndex.append(-1)
    for destino, peso in grafo.adj[0]: #Inicia todos os pesos em relação ao peso do vertice 0 até o outro vertice, MST só contem vertice 0 até agora
        pesoLista.append(peso)
    saida = defaultdict(set) #Uma lista de adjancencia para representar a MST
    visto = [0] #Uma lista para para representar os vertices que já estão na MST
    heapPredPeso = [ #Cria uma lista contendo todos os vertices com: o peso da MST até ele, o vertice pai dele(origem), o vertice em si
        (peso, 0, destino)
        for destino, peso in grafo.adj[0]
    ]
    heap(heapPredPeso) #Transforma a lista a cima em Heap
    for item in range(len(heapPredPeso)): #Para cada vertice na Heap salva o index dele na listaIndex
        listaIndex[heapPredPeso[item][2]] = item
    while heapPredPeso: #Enquanto Heap não vazia
        peso, origem, destino = heappop(heapPredPeso) #Pega o primeiro elementa da Heap
        visto.append(destino) #Adiciona na lista de vertices que já estão na MST
        if(origem < destino): #Adiciona na MST de uma forma ordenada já
            saida[origem].add(destino)
        else:
            saida[destino].add(origem)
        pesoTotal = pesoTotal + peso #Soma o peso até o vertice no pesoTotal
        pesoLista[destino] = peso #Atualiza o peso desse vertice na pesoLista
        for destinoProx, peso in grafo.adj[destino]: #Para cada outro vertice conectado nesse vertice
            if peso < pesoLista[destinoProx] and destinoProx not in visto: #Se o novo vertice não está na MST e o peso desse vertice é menor que o peso dele salvo na pesoLista
                heapPredPeso[listaIndex[destinoProx]] = (peso,destino,destinoProx) #Então, substitui esse novo peso na Heap pelo index salvo em listaIndex
                pesoLista[destinoProx] = peso #Atualiza o peso do vertice na pesoLista
                corrigeSubindo(heapPredPeso, 0, listaIndex[destinoProx]) #Corrige subindo a Heap apartir desse novo vertice
    return saida

#Leitura do numero de entradas
numeroEntradas = input()

#Nova instancia da classe Grafo
grafo = Grafo(int(numeroEntradas))

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
        grafo.adicionarAresta(x,y,peso)

#Chama a função do algoritmo de prim e retorna a MST que é salva em 'resultado'
resultado = dict(algoritmoPrim(grafo))

#Printa o peso total, da variavel global 'pesoTotal'
print('comprimento de cabeamento minimo: ' + "{:.4f}".format(pesoTotal))

#Para cada item um resultado, printa as coordenadas de forma crescente
for item in range(len(entrada)):
    if(item in resultado):
        aux2 = sorted(resultado[item]) #Ordena de forma crescente
        for x in aux2:
            if(item < x):
                print(str(item) + ' ' + str(x))
            else:
                print(str(x) + ' ' + str(item))