from Graph import Graph
from BestSearch import BestFirstSearch
from UniforrmCost import uniform_search_cost
from IterativeDS import IterativeDeapiningSearch
from DFS import DepthFirstSearch


class WaterJugProblem:
    
    def start_state(self):
        return (0,0)

    def is_end(self, state):
        return state[0] == 2 or state[1] == 2

    def successors(self, state):
        
        sucessor = []
        
        if state[0] != 4:
            new_State = (4,state[1])
            sucessor.append(('Fill 4 gallon' , (new_State) , 1))
            
        if state[1] != 3:
            new_State = (3,state[1])
            sucessor.append(('Fill 3 gallon' , (new_State) , 1))
            
        if state[0] <= state[1]:
            j1 = state[0]
            j2 = state[1]
            while j2 != 0 and j1 != 4:
                j1 = j1+1
                j2 = j2-1
                
            new_State = (j1,j2)
            
            sucessor.append(('Pour from 3 to 4 gallon' , (new_State) , 1))
        
        if state[1] <= state[0]:
            j1 = state[0]
            j2 = state[1]
            while j1!=0 and j2 != 3:
                j1 = j1-1
                j2 = j2+1
                
            new_State = (j1,j2)
            
            sucessor.append(('Pour from 4 to 3 gallon' , (new_State) , 1))
        
        if state[0] != 0:
            j1=0
            j2 = state[1]
            sucessor.append(('Empty 4 gallon' , (j1,j2) , 1))
        
        if state[1] != 0:
            j2=0
            j1 = state[0]
            sucessor.append(('Empty 3 gallon' , (j1,j2) , 1))
        
                
        return sucessor


def bfs_priority(state, cost):
 return cost        
            


p = WaterJugProblem()



dfs = DepthFirstSearch(p)

dfs_result = dfs.search()


bfs = BestFirstSearch(p, bfs_priority)
bfs_result = bfs.search()

usc = uniform_search_cost(p)
ids = IterativeDeapiningSearch(p)


print(f'BFS result is  {bfs_result}')
print(f'DFS result is  {dfs_result}')
print(f'UCS result is  {usc}')
print(f'IDS result is {ids}')
