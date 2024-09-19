
from Transportation import TransportationProblem

class DepthFirstSearch:
    def __init__(self, problem):
        self.problem = problem
        

    def search(self):
        start = self.problem.start_state()
        if self.problem.is_end(start):
            return [start]

        frontier = []
        
        frontier.append(start)
        
        explored = set()
        parent = {start: None}
        

        while frontier:
            state = frontier.pop()
            
            if self.problem.is_end(state):
                path = []
                
                while state is not None:
                    path.append(state)
                    state = parent[state]
                return list(reversed(path))

            explored.add(state)
            
            for action, next_state, cost in self.problem.successors(state):
                if next_state not in explored and all(node != next_state for node in frontier):
                    frontier.append(next_state)
                    parent[next_state] = state

        return None


# Running DFS on the Transportation Problem

problem = TransportationProblem(N=10)

dfs = DepthFirstSearch(problem)
print(dfs.search())