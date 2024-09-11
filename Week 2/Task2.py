#READING FILE
with open('graph.txt', 'r') as file:
    lines = file.readlines()  


#SPLITING THE DATA GOT FROM FILE
first = lines[0].strip().split('_')
vertices = first[0] #NO OF VERTICES
nodes = lines[1].strip().split()   #VERTICES NAME
directed = "Directed" if first[1] == '1' else "Undirected" #DIRECTED OR NOT
noOfEdges = int(lines[2].strip())   #NO OF EDGES
edges = [line.strip() for line in lines[3:]] #EDGES LIST

adjacencylist = {}
def buildAdjacencylist():
    adjacencylist = {}
    
    #ITERATING LIST
    for edge in edges:
        #SEPERATING EDGES NODES LIKE FOR AB u=A and v=B
        u, v = edge[0], edge[1]
        
        #MAKING A ROW FOR EACH VERTEX
        if u not in adjacencylist:
            adjacencylist[u] = []
        if v not in adjacencylist:
            adjacencylist[v] = []
        
        #ADDING SECOND VERTEX TO FIRST VERTEX NEIUGHBOUR 
        adjacencylist[u].append(v)
        
        #IF GRAPGH IS UNDIRECTED THEN ADD FIRST VERTEX TO SECOND VERTEX NEIUGHBOUR TOO
        if directed=='Undirected':
            adjacencylist[v].append(u)
    
    return adjacencylist


#GETTING ADJENCY LIST 
adjacencylist = buildAdjacencylist()


visited = []


#FUNCTION FOR RECURSION
def dfs(visited , adjList , source):
    
    recDfs(visited , adjList , source)


 
# RECURSIVE FUNCTION
def recDfs(visited , adjList , node):
    
    #IF NOD IS ALREADY VISTED RETIRN I.E BASE CASE
    if node in visited:
        return
    
    # OTHER WISE ADD IN VISTED LIST
    visited.append(node)
    
    #CHECKING ITS NEIUGHBOURS
    neiughbours = adjList.get(node , [])
    
    #APPLYING SAME FUNCTION FOR ALL NEIUGHBOURS OF A NODE
    for i in neiughbours:
        recDfs(visited , adjList , i)


#CALLING FUNCTION
dfs(visited , adjacencylist , 'B')


#DISPLAYING THE NODES IN VISTING ORDER
for i in range(len(visited)):
    if i != len(visited) - 1:
        print(f'{visited[i]} ->', end=' ')
    else:
        print(visited[i], end=' ')