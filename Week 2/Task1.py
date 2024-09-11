#TAKING INPUT TO WRITE IN FILE
vertices = int(input('Enter number of vertices: '))
names = []
for i in range(vertices):
    x = input(f'Enter name of vertex {i+1}: ')
    names.append(x)


directed = input('Directed or not: ')
noOfedges = int(input('Enter number of edges: '))
edges = []

for i in range(noOfedges):
    x = input(f'Enter edge {i+1}: ')
    edges.append(x)


#WRITING IN FILE
with open('graph.txt', 'w') as file:
    file.write(f'{vertices}_{directed}\n')
    
    for i in names:
        file.write(f'{i} ')
        
    file.write(f'\n{noOfedges}\n')
    
    for i in edges:
        file.write(f'{i}\n')


#READING FROM FILE
with open('graph.txt', 'r') as file:
    lines = file.readlines()  



#SPLITING THE DATA GOT FROM FILE
first = lines[0].strip().split('_')

vertices = first[0] #NO OF VERTICES
nodes = lines[1].strip().split()   #VERTICES NAME
directed = "Directed" if first[1] == '1' else "Undirected" #DIRECTED OR NOT
noOfEdges = int(lines[2].strip())   #NO OF EDGES
edges = [line.strip() for line in lines[3:]] #EDGES LIST


#BULDING ADJANCEY LIST
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
    

#FINDING NEIUGBOUR BY JUST GETTING FROM LIST     
def findNeighbors(vertex):
    return adjacencylist.get(vertex, [])

adjacencylist = buildAdjacencylist()


print(f'Number of vertices are: {vertices}')
print(f'The number of edges are: {noOfEdges}')
print(f'The graph is {directed}')

n = ''

while True:

    n = input('Enter vertex name to find neighbour OR Press q to exit: ')
    if n.lower()=='q':
        break
    print(f'The neighbors of vertex {n} are :  {findNeighbors(n)}')
    