class Vertex:
    def __init__(self, name):
        self.name = name

class Graph:
    vertices = {}
    edges = []
    indices_of_edges = {}

    def add_vertex(self, vertex):
        if vertex.name not in self.vertices and isinstance(vertex, Vertex):
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges)+1))
            self.indices_of_edges[vertex.name] = len(self.indices_of_edges)
            return True
        else:
            return False


################################################################

v1 = Vertex('Elk_Street')
v2 = Vertex('Main Street')
graph1 = Graph()

print(graph1.add_vertex(v1))
print(graph1.add_vertex(v2))

print(Graph.edges)
print(Graph.vertices)
print(Graph.indices_of_edges)
