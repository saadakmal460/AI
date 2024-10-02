from Graph import Graph
from BestSearch import BestFirstSearch
from UniforrmCost import uniform_search_cost
from IterativeDS import IterativeDeapiningSearch
from DFS import DepthFirstSearch


class RobotNavigation:
    def __init__(self, grid , start , goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.graph = Graph()
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
        return self.start

    def is_goal(self, state):
        return state == self.goal
    
    def cost(slef,state,action):
        return 1
    
    
    def actions(self,state):
        row , col = state
        actions = []
        
        rows = len(self.grid)
        cols = len(self.grid[0])
        

        if col+1 < cols and self.grid[row][col+1] != 1:
            actions.append('Right')
        if col-1 >= 0 and self.grid[row][col-1] != 1:
            actions.append('Left')
        if row+1 < rows and self.grid[row+1][col] != 1:
            actions.append('Down')
        if row-1 >= 0 and self.grid[row-1][col] != 1:
            actions.append('Up')
                
        return actions
        

    def transition(self, state , action):
        row , col = state
    
        if action == 'Right':
            return (row,col+1)
        if action == 'Left':
            return (row,col-1)
        if action == 'Down':
            return (row+1,col)
        if action == 'Up':
            return (row-1,col)
                


def bfs_priority(state, cost):
 return cost        
            
grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0]
]



start = (0, 0)
end = (5, 5)



p = RobotNavigation(grid ,start , end)


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
