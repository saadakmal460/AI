
visited = []
path = []
all_cycles = []


def is_Acyclic(graph , start_vertex):

    util(graph , start_vertex , None , start_vertex)
    
    #CHECKING IF THEIR WASD A CYCLE  
    if all_cycles:
        return True , len(all_cycles) , all_cycles   #RETURN THE PATHS AND NUMBER OF CYCLES
    else:
        return False
    
def util(graph , node , parent , start_vertex):

        #IF NODE IS PRESENT RETURN IT
        if node in visited:
            return
        
        #ADDING THE NODE TO MARK AS VISITED AND ADDING IN PATH TOO
        visited.append(node)
        path.append(node)
        
        #GETTING NEIGHBORS
        neighbors = graph.get_neighbors(node)
        
        for i in neighbors: #LOOPING NEIGHBORS
            if i == start_vertex and i != parent: #CECKING IF THE NODE IS REPEATED AND IT IS NOT THE PREVIOUS NODE IN CASE OF UNDIRECTED GRAPH
                
                cycle = path.copy() # COPING THE PATH
                cycle.append(start_vertex) #ADD THE NODE TO SHOW A CYCLE
                all_cycles.append(cycle) #ADDING N CYCLES TO KEEP RECORD OF ALL CYCLES THAT OCCURED
                
            elif i not in visited: #IF NOT CYCLE MEANS NEW NODE SO CHECK IF ALREADY VISITED
                
                util(graph , i , node , start_vertex)  #CALLING THE FUNCTION AGAIN
                
        #CLEARING PATH AND VISITED WHEN ONE SIDE IS COMPLETELY VISITED        
        path.pop()
        visited.remove(node)
        return None