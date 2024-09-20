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
        cost_so_far = {start: 0}
        
        
        while frontier:
            state = frontier.pop()
            
            
            if self.problem.is_end(state):
                
                path = []
                temp = state
                while state is not None:
                    path.append(state)
                    state = parent[state]
                return list(reversed(path)), cost_so_far[temp] 

            explored.add(state)
    
            
            for action , next_state , cost in self.problem.successors(state):
                if next_state not in explored and all(node != next_state for node in frontier):
                        
                        new_cost = cost_so_far[state] + cost
                        if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                            cost_so_far[next_state] = new_cost
                            frontier.append(next_state)
                            parent[next_state] = state

        return None