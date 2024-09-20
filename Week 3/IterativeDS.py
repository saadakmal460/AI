
from Transportation import TransportationProblem

class DepthLimitedSearch:
    def __init__(self, problem , limit):
        self.problem = problem
        self.limit = limit

    def search(self):
        start = self.problem.start_state()
        if self.problem.is_end(start):
            return [start]

        frontier = []
        
        frontier.append((start,0))
        
        explored = set()
        parent = {start: None}
        

        while frontier:
            state , depth = frontier.pop()
            
            
            if self.problem.is_end(state):
                path = []
                while state is not None:
                    path.append(state)
                    state = parent[state]
                return list(reversed(path))
            
            
            if depth >= self.limit:
                continue
                
            explored.add(state)
            
            for action, next_state, cost in self.problem.successors(state):
                if next_state not in explored and all(node != next_state for node in frontier):
                    frontier.append((next_state ,depth+1))
                    parent[next_state] = state
                    

        return None


def IterativeDeapiningSearch(problem):
    depth = 0
    while True:
        dfs = DepthLimitedSearch(problem , depth)
        result = dfs.search()
        
        if result != None:
            return result,depth
        
        depth= depth+1
        
