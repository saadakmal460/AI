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
                
                # Add edges for all possible movements (up, down, left, right)
                # Students will implement the logic here
        

    def start_state(self):
        return self.grid  # Example start state

    def is_end(self, state):
        return state == self.goal  # Example goal state

    def successors(self, state):

        sucessor = []
        
        row_idx , col_idx = self.find_space(state)
        
        
        
        if col_idx + 1 < 3:
            new_state = self.swap(state , (row_idx , col_idx) , (row_idx , col_idx+1))
            sucessor.append(('Right' , new_state , 1 ))
        
        if col_idx - 1 >= 0:
            new_state = self.swap(state , (row_idx , col_idx) , (row_idx , col_idx-1))
            sucessor.append(('Left' , new_state , 1 ))
            
        if row_idx + 1 < 3:
            
            new_state = self.swap(state , (row_idx , col_idx) , (row_idx + 1 , col_idx))
            sucessor.append(('Down' , new_state , 1 ))
        
       
        if row_idx - 1 >= 0:
            
            new_state = self.swap(state , (row_idx , col_idx) , (row_idx - 1 , col_idx))
            sucessor.append(('Up' , new_state , 1 ))
            
        return sucessor
        
        
    def swap(self, grid, pos1, pos2):
    # Create a copy of the grid to keep the original unchanged
        temp_list = [list(row) for row in grid]
    
        # Get the indices
        row1, col1 = pos1
        row2, col2 = pos2
        
        # Swap the elements in the list of lists
        temp_list[row1][col1], temp_list[row2][col2] = temp_list[row2][col2], temp_list[row1][col1]
        
        # Convert the list of lists back to a tuple of tuples
        return tuple(tuple(row) for row in temp_list)
    
    
    def find_space(self , grid):
        for row_idx, row in enumerate(grid):
            if 0 in row:
                col_idx = row.index(0)
                return (row_idx , col_idx)
        
def bfs_priority(state, cost):
 return cost

        
            

grid = (
    (2, 5, 8), 
    (7, 4, 0), 
    (6, 3, 1)
)


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
