class Problem1:
    def __init__(self, N , goal):
        self.N = N
        self.goal = goal

    def start_state(self):
        return self.N

    def is_end(self, state):
        return state == self.N
    
    def goal_state(self , state):
        
        return  self.goal == state

    def successors(self, state):
        sucessor = []
        
        
        
        
        if state[2] == 0:
            
            sucessor.append((state[0]-1 , state[1] , 1))
            sucessor.append((state[0] , state[1]-1 , 1))
            sucessor.append((state[0]-1 , state[1]-1 , 1))
        
        if state[2] == 1:
            sucessor.append((state[0] , state[1] , 0))
            
        
        return sucessor
 
 
start = (3,3,0)
end = (0,0,1)

p = Problem1(start,end)
successors = p.successors(start)
print(successors)


def test_successors(problem, start_state):
    frontier = [start_state]  # Initialize frontier with the start state
    visited = set()  # To track visited states

    while frontier:
        state = frontier.pop(0)  # FIFO queue for BFS

        if problem.goal_state(state):
            break
        
        if state in visited:
            continue

        visited.add(state)
        successors = problem.successors(state)
        print(f"State: {state} -> Successors: {successors}")

        # Add successors to the frontier for further exploration
        frontier.extend(s for s in successors if s not in visited)

# Run the test
test_successors(p, start)
