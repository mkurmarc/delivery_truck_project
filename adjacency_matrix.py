class Address:
    def __init__(self, name):
        self.name = name

class Graph:
    addresses = {}
    edges = []
    indices_of_edges = {}

    def add_address(self, address):
        if address.name not in self.addresses and isinstance(address, Address):
            self.addresses[address.name] = address
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges)+1))
            self.indices_of_edges[address.name] = len(self.indices_of_edges)
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
            if u in self.addresses and v in self.addresses:
                self.edges[self.indices_of_edges[u]][self.indices_of_edges[v]] = weight
                self.edges[self.indices_of_edges[v]][self.indices_of_edges[u]] = weight
                return True
            else:
                return False

    def print_map(self):
        for v, i in sorted(self.indices_of_edges.items()):
            print(v + ' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end='')
            print(' ')



################################################################
del_map = Graph()


A = Address('Elk_Street')
B = Address('Main Street')

del_map.add_address(A)
del_map.add_address(B)

for i in range(10):
    del_map.add_address(Address(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'GJ', 'HI']
for element in edges:
    del_map.add_edge(element[:1], element[1:])

# print(Graph.edges)
# print(Graph.addresses)
# print(Graph.indices_of_edges)

del_map.print_map()
