#BFS    
def bfs(graph, start_vertex):
    
    running = []
    visited = []
    rec_bfs(visited , graph , start_vertex , running)
    return visited


#CALCULATING THE DISTANCE
def bfs_distance(graph, start_vertex,end_vertex)->int:
    
    distance = 0
    visited = bfs(graph , start_vertex)
   
   #LOOPING THROUGH NODES AND GETTING DISTANCE
    for i in visited:
       if i == end_vertex:
           break
       distance = distance + 1
    
    return distance


def bfs_number_of_levels(graph, start_vertex,end_vertex)->int:
    level = 0
    visited = bfs(graph , start_vertex)
   
   #LOOPING THROUGH NODES AND GETTING LEVEL
    for i in visited:
       if i == end_vertex:
           break
       level = level + 1
    
    return level
    
    
#HELPING FUNCTION    
def rec_bfs(visited , graph , node , running):
    
    #IF NOD IS ALREADY VISTED RETIRN I.E BASE CASE
    if node in visited:
        return
    
    # OTHER WISE ADD IN VISTED LIST
    visited.append(node)
    
    #CHECKING ITS NEIUGHBOURS
    neiughbours = graph.get_neighbors(node)
    
    
    for i in neiughbours:
        
        #IF ALREADY VISITED THEN CONTINUE
        if i in visited:
            continue
        
        #APPEND TO RUNNING QUEUE SO WE APPLY RECURSION IN FIFO ORDER NOT IN LIFO
        running.append(i)
        
    #LOOPING THROUGH THE QUEUE        
    for i in running:
        rec_bfs(visited , graph , i , running)    