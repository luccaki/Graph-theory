class Graph: 
  
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = [] 
  
    def addEdge(self, u, v, w): 
        self.graph.append([u, v, w])
        #self.graph.append([v, u, w]) 
          
    def printArr(self, dist, dest): 
        print("Vertex Distance from Source") 
        print("{0}".format(dist[dest])) 
      
    def BellmanFord(self, src, dest): 
        dist = [float("Inf")] * self.V 
        dist[src] = 0
        
        #int(self.V/2)
        for _ in range(int(self.V/2)): 
            for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        dist[v] = dist[u] + w 
  
        for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        print("Graph contains negative weight cycle")
                        return
        self.printArr(dist, dest)
  
g = Graph(5)
#g.addEdge(0, 2, 67.7132)
#g.addEdge(0, 4, 2.7441)
#g.addEdge(1, 4, 0.8613)
#g.addEdge(1, 5, 9.1149)
#g.addEdge(2, 3, 4.5596)
#g.addEdge(3, 5, 0.4337)

g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 
g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3)

  
g.BellmanFord(0,3) 
"""
0               97.3479
1               719.8962999999999
2               729.7824999999999
3               776.8005999999999
4               0
5               98.30669999999999
6               99.77839999999999
7               622.2552
"""