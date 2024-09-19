from Graph import Graph

class GridWorldProblem:
    def __init__(self, grid):
        self.grid = grid
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
                
                # Add edges for all possible movements (up, down, left, right)
                # Students will implement the logic here
        

    def start_state(self):
        return (0, 0)  # Example start state

    def is_end(self, state):
        return state == (len(self.grid) - 1, len(self.grid[0]) - 1)  # Example goal state

    def successors(self, state):
        row , col = state
        sucessor = []
        print(row)
        print(col)
        rows = len(self.grid)
        cols = len(self.grid[0])
        
        if col+1 < cols:
            sucessor.append((state , 'Right' , (row,col+1)))
        if col-1 >= 0:
            sucessor.append((state , 'Left' , (row,col-1)))
        if row+1 < rows:
            sucessor.append((state , 'Down' , (row+1,col)))
        if row-1 >= 0:
            sucessor.append((state , 'Up' , (row-1,col)))
                
        return sucessor
        
            
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

g = GridWorldProblem(grid)
print(g.successors((1,1)))


