#Lucca Ianaguivara Kisanucki - 11201812090

#Esse programa recebe 4 numeros como entrada SOLAR SYSTEMS, WORMHOLES, ORIGIN, DESTINATION.
#SOLAR SYSTEMS - representa a quantidade de vertices no grafo
#WORMHOLES - representa a quantidade de arestas no grafo
#ORIGIN e DESTINATION - representam respectivamente qual a origem e destino
#Depois o programa recebe 'WORMHOLES' números de entrada que contém cada uma o (X, Y e PESO), formando uma aresta com peso
#O Objetivo desse programa é pegar todas essas arestas e montar o menor caminho possivel do vertice origem até o destino
#Gerando um caminho até esses dois pontos
#A saida do programa é:
#TOTAL JUMPS: - o número de vertices no caminho
#ENERGY REQUIRED: - o peso total do caminho
#ROUTE: -  uma sequencia de saidas do caminho, contendo todos os vertices ordenados da origem até o destino

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
            pos = posPai
            continue
        break
    heap[pos] = aux

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
        pos = posFilho
        posFilho = 2*pos + 1
    heap[pos] = aux
    corrigeSubindo(heap, inicial, pos)

#Função para transformar uma lista em Heap, faz a ordenação da lista inteira
def heap(x):
    n = len(x)
    for i in reversed(range(n//2)):
        corrigeDescendo(x, i)

 #Função do algoritmo de Dijkstra, recebe o grafo e uma origem e um destino
def algoritmoDijkstra(grafo, origem, destino):
    atual = origem #começa pela origem
    listaDistancia = [] #lista para guarda a distancia até o vertice e o vertice pai
    listaPeso = [[] for item in range(len(grafo))] #lista para guardar o peso do vertice
    vistos = [] #lista para guardar os vertices vistos

    listaPeso[atual] = 0 #zera o peso até a origem
    heapPredPeso = [] #Cria uma lista que será usada como heap
    
    for vertice in range(len(grafo)):
        listaDistancia.append(float('inf')) #inicia a distancia até os vertices como infinito

    listaDistancia[atual] = [0,origem] #distancia até a origem é 0 e o pai é a propria origem
    vistos.append(atual) #adiciona a origem nos vistos

    #enquanto tiver vertices não vistos
    while len(vistos) < len(grafo):
        for vizinho, peso in grafo[atual]: #para cada vizinho do vertice atual
             novoPeso = peso + listaPeso[atual] #peso da origem até o vertice
             if listaDistancia[vizinho] == float("inf") or listaDistancia[vizinho][0] > novoPeso: #se o novo peso for menor que o peso atual
                 listaDistancia[vizinho] = [novoPeso,atual] #atualiza na lista o peso novo e o pai novo
                 heapPredPeso.append((novoPeso,vizinho)) #adiciona na heap
                 heap(heapPredPeso) #atualiza a heap
                 
        if heapPredPeso == [] : break #se a heap estiver vazia sai do while
        peso, minVizinho = heappop(heapPredPeso) #pop no menor vizinho
        atual = minVizinho #novo atual é o menor vizinho
        listaPeso[atual] = peso #atualiza o peso dele na lista
        if atual not in vistos:
            vistos.append(atual) #adiciona o vertice nos vistos, dá uma verificada caso ele já esteja

    global energyRequired #variavel global para guardar o o peso total
    if(listaDistancia[destino] == float("inf")): #se no final de tudo o peso até o destino for infinito, quer dizer que não tem um caminho
        energyRequired = -1 #retorna menos -1 para representar que não tem caminho
    else:
        energyRequired = listaDistancia[destino][0] #pega o peso total até o destino
        caminho(listaDistancia,origem, destino) #chama a função recursiva caminho para determinar os vertices que fazem parte do caminho
    
totalJump = 0 #variavel global para guardar o numero total de vertices passados
route = [] #lista para guardar os vertices do caminho gerado

#função recursiva para gerar o caminho
def caminho(distancias,atual, destino):
    global totalJump
    global route
    if  destino != atual: #se não estamos no destino
        totalJump += 1 #+1 no totalJump
        route.append(destino) #adiciona o vertice no caminho
        return caminho(distancias,atual, distancias[destino][1]) #chama novamente a função caminho até chegar no destino
    else:
        totalJump += 1 #+1 no totalJump
        route.append(destino) #por ultimo adiciona o destino na lista
        return atual #retorna atual

#Classe que representa o Grafo
class Grafo(object):
    def __init__(self,vertices):
        self.adj = [[] for item in range(vertices)]

    #Função para adicionar uma aresta não direcionada
    def adicionarAresta(self, u, v, peso):
        self.adj[u].append((v,peso))
        self.adj[v].append((u,peso))

#Leitura das entradas
input()
solarSystems = int(input().split(" ")[2])
wormHoles = int(input().split(" ")[1])
origin = int(input().split(" ")[1])
destination = int(input().split(" ")[1])
input()

#Nova instancia da classe Grafo
grafo = Grafo(solarSystems)

#Cria uma lista para guardar as entradas
entrada = []

#Para cada entrada adiciona 'X Y PESO' na lista
for x in range(int(wormHoles)):
    entrada.append(input())

#Para cada aresta 'X Y PESO' na lista, adiciona no Grafo
for x in entrada:
    grafo.adicionarAresta(int(x.split(" ")[0]), int(x.split(" ")[1]), float(x.split(" ")[2]))

#chama a função de algoritmo de Dijkstra
algoritmoDijkstra(grafo.adj,origin,destination)

if(energyRequired == -1): #se energyRequired igual -1 então não existe caminho até o destino
    print("NO ROUTE FOUND!") #printa que não tem caminho
else:#se tiver caminho
    print("TOTAL JUMPS: " + str(totalJump)) #printa numero total dos vertices no caminho
    print("ENERGY REQUIRED: " + "{:.4f}".format(energyRequired)) #peso total das arestas no caminho
    print("ROUTE:") #printa em ordem da origem até o destino todos os vértices
    for item in range(len(route)):
        print(str(item) + ": " + str(route[len(route)-item-1]))