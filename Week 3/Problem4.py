from Graph import Graph
from BestSearch import BestFirstSearch
from UniforrmCost import uniform_search_cost
from IterativeDS import IterativeDeapiningSearch
from DFS import DepthFirstSearch


class WaterJugProblem:
    
    def start_state(self):
        return (0,0)

    def is_goal(self, state):
        return state[0] == 2 or state[1] == 2

    def cost (self,state,action):
        return 1
    
    def actions(self,state):
        
        actions = []
        
        if state[0] != 4:
            
            actions.append('Fill 4 gallon')
            
        if state[1] != 3:
            
            actions.append('Fill 3 gallon')
            
        if state[0] <= state[1]:
            actions.append('Pour from 3 to 4 gallon')
        
        if state[1] <= state[0]:
            actions.append('Pour from 4 to 3 gallon')
        
        if state[0] != 0:
            
            actions.append('Empty 4 gallon')
        
        if state[1] != 0:
            actions.append('Empty 3 gallon')
        
        return actions
        
    def transition(self, state , action):

        if action == 'Fill 4 gallon':
            new_State = (4,state[1])
            return new_State
            
        if action == 'Fill 3 gallon':
            new_State = (3,state[1])
            return new_State
            
            
        if action == 'Pour from 3 to 4 gallon':
            j1 = state[0]
            j2 = state[1]
            while j2 != 0 and j1 != 4:
                j1 = j1+1
                j2 = j2-1
                
            new_State = (j1,j2)
            
            return new_State
        
        if action == 'Pour from 4 to 3 gallon':
            j1 = state[0]
            j2 = state[1]
            while j1!=0 and j2 != 3:
                j1 = j1-1
                j2 = j2+1
                
            new_State = (j1,j2)
            return new_State
        
        if action == 'Empty 4 gallon':
            j1=0
            j2 = state[1]
            return (j1,j2) 
        
        if action == 'Empty 3 gallon':
            j2=0
            j1 = state[0]
            return (j1,j2)
        



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
