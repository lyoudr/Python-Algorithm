from dictionary import Dictionary
from queue import Queue

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'G', 'H', 'I']

class Graph:
  def __init__(self):
    self.vertices = []
    self.adjList = Dictionary()
  def addVertex(self, v):
    self.vertices.append(v)
    self.adjList.add(v, [])
  def addEdge(self, v, w):
    self.adjList.get(v).append(w)
    self.adjList.get(w).append(v)
  def toString(self):
    stx = ''
    for i in range(0, len(self.vertices)):
      stx += self.vertices[i] + ' => '
      neighbors = self.adjList.get(self.vertices[i])
      for j in range(0, len(neighbors)):  
        stx += neighbors[j] + ' '
      stx += '\n'
    print(stx)
    return stx  
  # Breadth-First Search, BFS
  def bfs(self, v, callback):
    # Previous setting
    d = {}
    pred = {}
    color = {}

    for i in vertices:
      color[i] = 'white'
      d[i] = 0
      pred[i] = None

    queue = Queue()
    queue.enqueue(v)    

    while not queue.isEmpty():
      u = queue.dequeue()
      neighbors = self.adjList.get(u)
      color[u] = 'grey'
    
      for n in neighbors:
        if color[n] == 'white':
          color[n] = 'grey'
          # Count distance and set pred
          d[n] = d[u] + 1
          pred[n] = u
          queue.enqueue(n)
      color[u] = 'black'
    print('distance is =>',d) 
    print('predecessors is =>', pred)
    return pred
  
  # Depth-First Search, DFS
  def dfs(self, df_u):
    df_color = {}
    d = {} # discovered time of vertices
    f = {} # completed time of vertices
    p = {} # predecessor of vertices
    time = 0    
    for i in vertices:
      df_color[i] = 'white'
    for i in vertices:
      f[i] = 0
      d[i] = 0
      p[i] = None
    self.dfsVisit(df_u, df_color, d, f, p, time)
    print('discovery is =>', d)
    print('finished is =>', f)
    print('predecessor is =>', p)
  
  def dfsVisit(self, u, color, d, f, p, time):
    print('discovered => ', u)
    color[u] = 'grey'
    time += 1
    d[u] = time
    neighbors = self.adjList.get(u)
    for i in range(0, len(neighbors)):
      w = neighbors[i]
      if color[w] == 'white':
        p[w] = u
        self.dfsVisit(w, color, d, f, p, time)
    color[u] = 'black'
    time += 1
    f[u] = time
    print('explored => ', u)

def printNode(value):
  print('Visited vertex: ' + value)

graph = Graph()

for v in vertices:
  graph.addVertex(v)
### 1. Add Edges
graph.addEdge('A', 'B')
graph.addEdge('A', 'C')
graph.addEdge('A', 'D')
graph.addEdge('C', 'D')
graph.addEdge('C', 'G')
graph.addEdge('D', 'G')
graph.addEdge('D', 'H')
graph.addEdge('B', 'E')
graph.addEdge('B', 'F')
graph.addEdge('E', 'I')
# graph.toString()

### 2.BFS
# graph.bfs(vertices[0], printNode)

# find A to each vertices path
# fromVerte = vertices[0]
# predecessors = graph.bfs(vertices[0], printNode)

# for i in range(1, len(vertices)):
#   path = []
#   def reverseFunc(v):
#     path.append(v)
#     if predecessors[v] != None:
#       reverseFunc(predecessors[v])
#     else :
#       s = path.pop()
#       while len(path):
#         s += ' - ' + path.pop()
#       print(s)
#   reverseFunc(vertices[i])

### 3.DFS
graph.dfs(vertices[0])
graph.dfs(vertices[0])


  
