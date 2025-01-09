from Task1 import Graph

track = []
cycle = []

def dfs(graph,node):
    visited = []
    
    
    dfs_rec(graph , node , visited)
    return visited
    

def dfs_rec(graph,node,visited):
    if node in visited:
        return
    
    # OTHER WISE ADD IN VISTED LIST
    visited.append(node)
    track.append(node)
    
    #CHECKING ITS neighbors
    neighbors = graph.get_neighbors(node)
    
    #APPLYING SAME FUNCTION FOR ALL neighbors OF A NODE
    for i in neighbors:
        if i not in visited:
            dfs_rec(graph , i , visited)
        if i not in track and i!=node:
            cycle.extend(track)

g = Graph()


g.read_graph_from_file('graph.txt')

print(dfs(g,'A'))