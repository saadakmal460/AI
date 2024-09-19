import heapq
from Transportation import TransportationProblem

class BestFirstSearch:
    def __init__(self, problem, priority_function):
        self.problem = problem
        self.priority_function = priority_function

    def search(self):
        start = self.problem.start_state()
        if self.problem.is_end(start):
            return [start]

        frontier = []
        heapq.heappush(frontier, (self.priority_function(start, 0), start))
        
        explored = set()
        parent = {start: None}
        cost_so_far = {start: 0}

        while frontier:
            priority, state = heapq.heappop(frontier)

            if self.problem.is_end(state):
                path = []
                temp = state
                while state is not None:
                    path.append(state)
                    state = parent[state]
                return list(reversed(path)), cost_so_far[temp]

            explored.add(state)
            
            for action, next_state, cost in self.problem.successors(state):
                if next_state not in explored and all(node[1] != next_state for node in frontier):
                    new_cost = cost_so_far[state] + cost
                    if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                        cost_so_far[next_state] = new_cost
                        priority = self.priority_function(next_state, new_cost)
                        heapq.heappush(frontier, (priority, next_state))
                        parent[next_state] = state

        return None




# Example priority functions for BFS
def bfs_priority(state, cost):
 return cost
# Running BFS on the Transportation Problem

problem = TransportationProblem(N=10)


bfs_search = BestFirstSearch(problem, bfs_priority)
print(bfs_search.search())
