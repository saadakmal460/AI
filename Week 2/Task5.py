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
                    w = int(edge[3:])
                    
                    tup = (v,w)
                    tup2 = (u,w)
                    
                    #MAKING A ROW FOR EACH VERTEX
                    if u not in self.adjacency_list:
                        self.adjacency_list[u] = []
                    if v not in self.adjacency_list:
                        self.adjacency_list[v] = []
                    
                    #ADDING SECOND VERTEX TO FIRST VERTEX NEIUGHBOUR 
                    
                    self.adjacency_list[u].append(tup)
                    
                    #IF GRAPGH IS UNDIRECTED THEN ADD FIRST VERTEX TO SECOND VERTEX NEIUGHBOUR TOO
                    if self.is_directed == False:
                        self.adjacency_list[v].append(tup2)
                

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
    
    





def distance_dijxtra(graph,  start_vertex, end_vertex):
    visited = [] #VISITED LIST
    path = []  #PATH FOR ALL TRACKS
    best_path = []  #BEST PATH
    best_cost = [10000000000000]  # BEST COST
    
    
    #START DFS
    dfs(graph, start_vertex,end_vertex, visited, path, 0, best_path, best_cost)
    
    #RETRNING IN REUIRED FORMAT
    return (best_cost[0] , best_path)



def dfs(graph, node, end, visited, path, current_cost, best_path, best_cost):
    
    #IF NODE IS ALREADY VISITED SO RETURN
    if node in visited:
        return
    
    #ADDING NODE IN VISITED LIST
    visited.append(node)
    
    #CHECKING IF THE NODE IS THE END
    if node == end:
        #CHECKING IF THE CURRENT COST IS ALSO THE BEST 
        if current_cost < best_cost[0]:
            
            #UPDATING THE BEST COAST AND THE BEST PATH
            best_cost[0] = current_cost
            best_path.clear()
            best_path.extend(list(path))
            
            
    else:
        #GETTING NEUGHBOURS
        neighbors = graph.get_neighbors(node)
        
        for i in neighbors: # 'i' WILL BE LIKE ('B' , 2)
            if i[0] not in visited:
          
                path.append((node,i[0],i[1])) #ADDING CURRENT NODE AND AND NEXT NODE IN PATH
                
                #MOVING TO THE NEXT NODE
                dfs(graph , i[0] , end , visited , path , current_cost + i[1] , best_path , best_cost)
                
                #REMOVING THE PATH WHEN RECURSION IS RETURNING
                path.pop()
                
    #REMOVING VISITED NODES WHEN RECUSRSION IS RETURNING            
    visited.remove(node)