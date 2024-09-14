class Graph:
    def __init__(self):
        self.vertices = []          # List to store vertex names
        self.edges = []             # List to store edges as tuples (start, end)
        self.is_directed = False    # To store whether the graph is directed
        self.adjacency_list = {}    # Dictionary to store adjacency list

    def read_graph_from_file(self, filename):
        """
        Reads the graph from a file with the specified format.
        Input: filename - name of the file containing the graph.
        """
        with open(filename, 'r') as file:
            
                lines = file.readlines()  
                #SPLITING THE DATA GOT FROM FILE
                first = lines[0].strip().split('_')
                self.vertices = lines[2].strip().split()   #VERTICES NAME
                self.is_directed = True if first[1] == '1' else False #DIRECTED OR NOT
                self.edges = [line.strip() for line in lines[6::2] if line.strip()] #EDGES LIST
                for edge in self.edges:
                    #SEPERATING EDGES NODES LIKE FOR AB u=A and v=B
                    u, v = edge[0], edge[1]
                    
                    #MAKING A ROW FOR EACH VERTEX
                    if u not in self.adjacency_list:
                        self.adjacency_list[u] = []
                    if v not in self.adjacency_list:
                        self.adjacency_list[v] = []
                    
                    #ADDING SECOND VERTEX TO FIRST VERTEX NEIUGHBOUR 
                    self.adjacency_list[u].append(v)
                    
                    #IF GRAPGH IS UNDIRECTED THEN ADD FIRST VERTEX TO SECOND VERTEX NEIUGHBOUR TOO
                    if self.is_directed == False:
                        self.adjacency_list[v].append(u)
                

    def get_vertex_count(self):
        """
        Returns the total number of vertices in the graph.
        Output: int - number of vertices.
        """
        
        return len(self.vertices)

    def get_edge_count(self):
        """
        Returns the total number of edges in the graph.
        Output: int - number of edges.
        """
        return len(self.edges)

    def is_graph_directed(self):
        """
        Returns whether the graph is directed or not.
        Output: bool - True if the graph is directed, False otherwise.
        """
        return self.is_directed

    def get_neighbors(self, vertex):
        """
        Returns the neighbors of the given vertex.
        Input: vertex - the vertex whose neighbors are to be returned.
        Output: list - list of neighboring vertices.
        """
        return self.adjacency_list.get(vertex, [])
    
    


g = Graph()


file_name = input("Enter file name: ")

g.read_graph_from_file(file_name)

v = g.get_vertex_count()
print(f'The vertices are {v}')

edges = g.get_edge_count()
print(f'The number of edges are {edges}')


directed = g.is_graph_directed()
print(f'The graph is {"Directed" if directed else "Undirected"}')



while True:
    n = input("Enter vertex to get neighbours/ Press q to exit: ")
    if n =='q':
        break
    print(f'The neighbour of {n} are {g.get_neighbors(n)}')