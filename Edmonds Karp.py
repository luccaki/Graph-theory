#Lucca Ianaguivara Kisanucki - 11201812090

#A primeira linha da entrada consiste de um número n (1 <= n <= 100000) que denota o número de vértices do digrafo D;
#A segunda, de um número inteiro m (0 <= m <= n (n - 1)) que presenta o número total de arcos em D;
#A terceira linha consiste de um número inteiro s;
#A quarta, de um inteiro t;
#Cada uma das próximas m linhas consiste de três números inteiros x y w, onde 0 <= x, y < n e 0 <= w <= 999, representando que D contém um arco xy tal que c(xy) = w.
#O objetivo do programa e usando o algoritmo de Edmonds_Karp, retorna o fluxo maximo do grafo apartir do vertice s até o vertice t
#E printar em seguida o fluxo de todas as arestas

#Função Algoritmo de Edmonds_Karp
#Recebe um grafo C, um vertice de origem s e um vertice de destino t
def algoritmoEdmondsKarp(C, s, t):
    vertices = len(C.adj) #Numero de vertices no grafo
    grafoFluxos = Grafo(vertices) #Cria um grafo secundario para listar o fluxo das arestas

    caminho = BFS(C, grafoFluxos.adj, s, t) #Chama a função BFS para trazer um caminho disponivel no grafo do vertice s ao t
    while caminho != None: #Enquanto existir um caminho
        u, v = caminho[0], caminho[1] #Pega o primeiro e segunda vertice do caminho
        fluxo = C.capacidade(u,v) - grafoFluxos.adj[u][v] #Calcula o fluxo do arco u v, (capacidade - quantidade de fluxo ja alocado)
        for item in range(len(caminho) - 2): #Percorre todo o caminho procurando o menor fluxo entre os arcos
            u, v = caminho[item+1], caminho[item+2] #Pega dois novos vertices
            fluxo = min(fluxo, C.capacidade(u,v) - grafoFluxos.adj[u][v]) #Sempre busca o menor fluxo
        for item in range(len(caminho) - 1): #Percorre todo o caminho adicionando o novo fluxo e excluindo o fluxo no sentido contrario do arco
            u, v = caminho[item], caminho[item+1] #Pega dois novos vertices
            grafoFluxos.adj[u][v] += fluxo #Adiciona o fluxo no arco
            grafoFluxos.adj[v][u] -= fluxo #Retira o fluxo no arco
        caminho = BFS(C, grafoFluxos.adj, s, t) #Pega um novo caminho no grafo

    return grafoFluxos.adj #Retorna o fluxo maximo e o grafo secundario dos fluxos

#Função BFS
def BFS(C, fluxo, s, t):
    pai = [-1] * len(C.adj) #Inicia uma lista de pai por index com todos em -1
    pai[s] = s #Pai do vertice inicial é ele mesmo
    lista = [s] #Lista para guardar todos os vertices alcancaveis
    while lista: #Enquanto tiver um vertice na lista
        u = lista.pop(0) #Pega o primeiro vertice
        for v in range(len(C.adj)): #Para cada vertice no grafo:
            if C.capacidade(u,v) - fluxo[u][v] > 0 and pai[v] == -1: #Se o fluxo do arco u v for positivo e não tiver um pai ainda:
                pai[v] = u #Adiciona o pai nele
                lista.append(v) #Adiciona na lista de vertices alcancaveis
                if v == t: #Se chegou no vertice de destino:
                    caminho = [] #Inicia uma lista para retorna o caminho
                    while True: #Até chegar no destino
                        caminho.insert(0, v) #insere no primeiro index do caminho o vertice v (ordena de forma da origem até o destino)
                        if v == s: #se v for origem já para
                            break
                        v = pai[v] #se v não for a origem ainda, v vira o pai dele mesmo (o vertice anterior)
                    return caminho #retorna a lista do caminho
    return None #Caso acabe a lista toda de vertices e não chegar no destino, retorna NULL(None)

#Classe que representa um Grafo
class Grafo(object):
    def __init__(self,vertices):
        self.adj = [[ 0 for item in range(vertices)] for item in range(vertices)] #Inicia todos os arcos em 0

    #Função para adicionar uma aresta não direcionada
    def adicionarAresta(self, u, v, capacidade):
        self.adj[u][v] = capacidade

    #Função para retorna o peso(capacidade)
    def capacidade(self, u, v):
        return self.adj[u][v]

vertices = input() #Pega o numero de vertices
arestas = input() #Pega o numero de arestas
s = input() #Pega o vertice de origem
t = input() #Pega o vertice de destino

grafo = Grafo(int(vertices)) #Inicia o grafo com tantos vertices
for item in range(int(arestas)): #Para cada aresta
    entrada = input() #Pega a nova aresta com a capacidade
    grafo.adicionarAresta(int(entrada.split(" ")[0]),int(entrada.split(" ")[1]),int(entrada.split(" ")[2])) #Adiciona a aresta com a capacidade no grafo

fluxo = algoritmoEdmondsKarp(grafo,int(s),int(t)) #Chama o algoritmoEdmondsKarp, retornando o grafo que representa os fluxos

#Calcula o fluxo maximo do grafo apartir do vertice de origem
fluxoMaximo = 0
for item in range(int(vertices)):
    fluxoMaximo += fluxo[int(s)][item]

print(fluxoMaximo) #Printa o fluxo maximo
for i in range(len(grafo.adj)): #Para cada aresta no grafo printa os vertices e o fluxo
    for j in range(len(grafo.adj)):
        if(grafo.adj[i][j] != 0): #Sempre verifica no grafo de capacidade para ver se existe a aresta nele
            print(str(i) + " " + str(j) + " " + str(fluxo[i][j]))