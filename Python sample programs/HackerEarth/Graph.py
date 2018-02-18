class Vertex():
    def __init__(self,key):
        self.id = key
        self.adjVertex = {}

    def addEdgetoVertex(self,key,weight):

        self.adjVertex[key] = weight

    def getAdjVertex(self):
        return self.adjVertex

class Graph():
    def __init__(self):
        self.numVertices = 0
        self.Vertices = {}

    def addVertice(self,key):

        self.Vertices[key] = Vertex(key)
        self.numVertices += 1

    def addEdge(self,key1,key2,weight=0):
        if key1 in self.Vertices and key2 in self.Vertices:
            self.Vertices[key1].addEdgetoVertex(key2, weight)
            self.Vertices[key2].addEdgetoVertex(key1, weight)
        elif key1 not in self.Vertices:
            self.addVertice(key1)
            self.Vertices[key1].addEdgetoVertex(key2, weight)
            self.Vertices[key2].addEdgetoVertex(key1, weight)
        elif key2 not in self.Vertices:
            self.addVertice(key2)
            self.Vertices[key1].addEdgetoVertex(key2, weight)
            self.Vertices[key2].addEdgetoVertex(key1, weight)


    def printGraph(self):
        for node, adjVert in self.Vertices.items():
            print('Node:', node, " Adj Vertex:", adjVert.getAdjVertex())

    def findVertex(self,key):
        if key in self.Vertices :
            print(key, " is available")
        else :
            print(key, " is not available")

    def deleteVetex(self,key):
        for node in self.Vertices[key].getAdjVertex().keys():
            self.Vertices[node].getAdjVertex().pop(key)

        self.Vertices.pop(key)
        self.numVertices -= 1




def dijsktra(node):






g = Graph()

for i in range(1,6):
    g.addVertice(i)

g.addEdge(1, 2, 5)
g.addEdge(3, 2, 6)
g.addEdge(2, 4, 2)
g.addEdge(3, 5, 7)

g.printGraph()
g.findVertex(7)
g.deleteVetex(2)


g.printGraph()
print(g.numVertices)
#g.addVertice(2)
g.addEdge(1, 2, 5)
g.addEdge(3, 2, 6)
g.addEdge(2, 4, 2)
g.printGraph()
print(g.numVertices)



