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
levels = {}

#FUNCTION FOR RECURSION
def bfs(visited , adjList , source):
    
    running = []
    levels[source] = 0
    recBfs(visited , adjList , source , running)


# RECURSIVE FUNCTION    
def recBfs(visited , adjList , node , running):
    
    #IF NOD IS ALREADY VISTED RETIRN I.E BASE CASE
    if node in visited:
        return
    
    # OTHER WISE ADD IN VISTED LIST
    visited.append(node)
    
    #CHECKING ITS NEIUGHBOURS
    neiughbours = adjList.get(node , [])
    
    flag = False #INITIALIZING A FLAG FOR SAME LEVEL
    
    
    
    for i in neiughbours:
        
        #IF ALREADY VISITED THEN CONTINUE
        if i in visited:
            continue
        
        #APPEND TO RUNNING QUEUE SO WE APPLY RECURSION IN FIFO ORDER NOT IN LIFO
        running.append(i)
        
        #CHECKING IF ITERATING OVER SAME LEVEL 
        if not flag:
            #GETTING THE MAX LEVEL AND INCREMENTING IT 
            prevLevelNode = max(levels , key = levels.get)
            prevLevelNodeVal = levels[prevLevelNode]
            flag = True #CHANGING VALUE SO DONT GET THE VALUE OF SAME LEVEL
            
        #APPENDING VALUE IN LEVELS DICTIONARY    
        levels[i] = prevLevelNodeVal+1
        print(levels)
     
    #LOOPING THROUGH THE QUEUE        
    for i in running:
        recBfs(visited , adjList , i , running)       



#CALCULATING DISTANCE
def distance(node)->int:
    
    distance = 0
   
   #LOOPING THROUGH NODES AND GETTING DISTANCE
    for i in visited:
       if i == node:
           break
       distance = distance + 1
    
    return distance
        
    


source = 'B'
destination = 'D'
bfs(visited , adjacencylist , source)


#PRINT FUNCTIONS
for i in range(len(visited)):
    if i != len(visited) - 1:
        print(f'{visited[i]} ->', end=' ')
    else:
        print(visited[i], end=' ')
        
x = distance(destination)

print(f'\nThe distance from {source} to {destination} is: {x}')


for node, level in levels.items():
    print(f"{node} is at level {level}")