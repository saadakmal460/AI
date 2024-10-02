from Graph import Graph
from BestSearch import BestFirstSearch
from UniforrmCost import uniform_search_cost
from IterativeDS import IterativeDeapiningSearch
from DFS import DepthFirstSearch


class GridWorldProblem:
    def __init__(self, grid , goal):
        self.grid = grid
        self.graph = Graph()
        self.goal = goal
        self._build_graph()

    def _build_graph(self):
        rows = len(self.grid)
        cols = len(self.grid[0])
        for row in range(rows):
            for col in range(cols):
                state = (row, col)
                
                if state[1] + 1 < state[1]:
                    self.graph.add_edge(state, 'Right', 1, state[1] + 1)
                    
                if state[1] - 1 < state[1]:
                    self.graph.add_edge(state, 'Left', 1, state[1] + 1)
                
                if state[0] + 1 < state[0]:
                    self.graph.add_edge(state, 'Down', 1, state[0] + 1)
                    
                if state[0] + 1 <state[0]:
                    self.graph.add_edge(state, 'Up', 1, state[0] + 1)

    def start_state(self):
        return self.grid  

    def is_goal(self, state):
        return state == self.goal
    
    def cost(self,state,action):
        return 1 
    
    
    def actions(self,state):
        
        actions = []
        row_idx , col_idx = self.find_space(state)
        
        if col_idx + 1 < 3:

            actions.append('Right')
        
        if col_idx - 1 >= 0:
            actions.append('Left')
            
        if row_idx + 1 < 3:
            actions.append('Down')
        
        if row_idx - 1 >= 0:
            actions.append('Up')
            
        return actions
        
    def transition(self, state , action):

        row_idx , col_idx = self.find_space(state)    
        if action == 'Right':
            new_state = self.swap(state , (row_idx , col_idx) , (row_idx , col_idx+1))
            return new_state
        
        if action == 'Left':
            new_state = self.swap(state , (row_idx , col_idx) , (row_idx , col_idx-1))
            return new_state
            
        if action == 'Down':
            
            new_state = self.swap(state , (row_idx , col_idx) , (row_idx + 1 , col_idx))
            return new_state
        
        if action == 'Up':
            
            new_state = self.swap(state , (row_idx , col_idx) , (row_idx - 1 , col_idx))
            return new_state
            

        
        
    def swap(self, grid, pos1, pos2):

        temp_list = [list(row) for row in grid]

        row1, col1 = pos1
        row2, col2 = pos2
       
        temp_list[row1][col1], temp_list[row2][col2] = temp_list[row2][col2], temp_list[row1][col1]
         
        return tuple(tuple(row) for row in temp_list)
    
    
    
    def find_space(self , grid):
        for row_idx, row in enumerate(grid):
            if 0 in row:
                col_idx = row.index(0)
                return (row_idx , col_idx)





        
def bfs_priority(state, cost):
 return cost

        
            

grid = ((1, 2, 3), (4, 0, 6), (7, 5, 8))


end = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

p = GridWorldProblem(grid , end)


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
