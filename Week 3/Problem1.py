from DFS import DepthFirstSearch
from BestSearch import BestFirstSearch
from UniforrmCost import uniform_search_cost
from IterativeDS import IterativeDeapiningSearch
class Problem1:
    def __init__(self, N , goal):
        self.N = N
        self.goal = goal

    def start_state(self):
        return self.N

    def is_goal(self, state):
        return state == self.goal
    
    def cost(slef,s,a):
        return 1
    
    
    def actions(self , state):
        actions = []
        
        if state[2] == 0:
            
            if state[0]-1 >= 0:
                
                actions.append('Move right with one canabel')
                
            if state[1]-1 >= 0:
                actions.append('Move right with one missionary')
            
            if state[1]-1 >= 0 and  state[0]-1 >= 0:    
                actions.append('Move right with both')
        
        if state[2] == 1:
            actions.append('Move left')
            
        return actions
        
    
    def transition(self, state , action):

        if action == "Move right with one canabel":
            return (state[0]-1 , state[1] ,1)
            
        elif action == "Move right with one missionary":
            return (state[0] , state[1]-1 ,1)
        
        elif action == "Move right with both":   
            return (state[0]-1 , state[1]-1 ,1)
    
        elif action == "Move left": 
            return (state[0] , state[1],0)

 
 
 
def bfs_priority(state, cost):
 return cost

 
start = (3,3,0)
end = (0,0,1)

p = Problem1(start,end)
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