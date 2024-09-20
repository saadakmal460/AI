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

    def is_end(self, state):
        return state == self.goal
    
    def successors(self, state):
        sucessor = []
        
        if state[2] == 0:
            
            if state[0]-1 >= 0:
                
                sucessor.append(('Move right with one canabel' , (state[0]-1 , state[1] , 1),1))
                
            if state[1]-1 >= 0:
                sucessor.append(('Move right with one missionary' , (state[0] , state[1]-1 , 1 ),1))
            
            if state[1]-1 >= 0 and  state[0]-1 >= 0:    
                sucessor.append(('Move right with both' , (state[0]-1 , state[1]-1 , 1),1))
        
        if state[2] == 1:
            sucessor.append(('Move left' , (state[0] , state[1] , 0),1))
            
        
        return sucessor
 
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