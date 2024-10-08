class MDP:
    def __init__(self, grid , start , goal , gamma , convergence , fail_prob):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.gamma = gamma
        self.convergence = convergence
        self.fail_prob = fail_prob
      

    def start_state(self):
        return self.start

    def is_goal(self, state):
        return state == self.goal
    
    def reward(self , state , action):
        
        reward = 0 
        row , col = state
        
        if action == 'Right':
            reward = self.grid[row][col+1]
            
        if action == 'Left':
            reward = self.grid[row][col-1]
            
        if action == 'Up':
            reward = self.grid[row-1][col]
            
        if action == 'Down':
            reward = self.grid[row+1][col]
        
        return reward
            
            
    
    
    def actions(self,state):
        row , col = state
        actions = []
        
        rows = len(self.grid)
        cols = len(self.grid[0])
        

        if col+1 < cols:
            actions.append('Right')
        if col-1 >= 0 :
            actions.append('Left')
        if row+1 < rows:
            actions.append('Down')
        if row-1 >= 0:
            actions.append('Up')
                
        return actions
   
    
    def transision_proability(self , state , action):
        prob = 1
        
        river_edges = self.is_river(state)
        
        if river_edges == 0:
            return prob
        else:
            prob = prob - river_edges*self.fail_prob       
        
        return prob

    def is_river(self,state):
        count = 0 
        row,col = state
        
        if  row < 3 and self.grid[row+1][col] == -50:
            count+=1
                
        if  row > 0 and self.grid[row-1][col] == -50:
            count+=1
        
        if  col > 0 and self.grid[row][col-1] == -50:
            count+=1
        
        if col < 3 and self.grid[row][col+1] == -50:
            count+=1

        return count
        
             

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
    
    
def value_iteration(mdp):
        
    rows = len(mdp.grid)
    cols = len(mdp.grid[0])
    values = [[0 for _ in range(cols)] for _ in range(rows)]
    
    while True:
        curr_convergence = 0
        for row in range(rows):
            for col in range(cols):
                
                curr_state = (row,col)
                
                if mdp.is_goal(curr_state):
                    continue
                
                curr_value = values[row][col]
                
                new_value = -1000000000
                
                for action in mdp.actions(curr_state):
                    new_state = mdp.transition(curr_state , action)
                    probability = mdp.transision_proability(curr_state , action)
                    reward = mdp.reward(curr_state,action)
                    new_row , new_col = new_state
                    new_value = max(new_value , probability * (reward + mdp.gamma*values[new_row][new_col]))
                
                values[row][col] = new_value
                curr_convergence = max(curr_convergence , abs(new_value-curr_value))
        
        if curr_convergence < mdp.convergence:
            break
        
    return values    

def policy_evaluation(mdp , values):
    
    rows = len(mdp.grid)
    cols = len(mdp.grid[0])
    
    moves = [['' for _ in range(cols)] for _ in range(rows)]
    
    for row in range(rows):
        for col in range(cols):
            
            curr_state = (row,col)
            
            if mdp.is_goal(curr_state):
                moves[row][col] = 'Goal State'
                continue
            
            best_action = ''
            best_value = -100000000000
            
            for action in mdp.actions(curr_state):
                new_state = mdp.transition(curr_state , action)
                proability = mdp.transision_proability(curr_state,action)
                reward = mdp.reward(curr_state,action)
                new_row , new_col = new_state
                curr_value = proability * (reward + mdp.gamma*values[new_row][new_col])
                
                if curr_value > best_value:
                    best_value = curr_value
                    best_action = action
                    
            moves[row][col] = best_action
            
    return moves
        


def create_grid():
    size = int(input("Enter the size of the grid (n x m): "))
    grid = []
    
    print("Enter rewards for each state (row by row):")
    for i in range(size):
        row = []
        for j in range(size):
            reward = int(input(f"Enter reward for state ({i}, {j}): "))
            row.append(reward)
        grid.append(row)
    
    return grid        

            
grid = create_grid()

start_state_row = int(input('Enter start state row: '))
start_state_col = int(input('Enter start state col: '))

end_state_row = int(input('Enter end state row: '))
end_state_col = int(input('Enter end state col: '))

reward = int(input('Enter reward for end state col: '))

grid[end_state_row][end_state_col] = reward

discount = float(input('Enter discount factor (gamma): '))
convergence = float(input('Enter convergence: '))
slip_prob = float(input('Enter slip proability: '))

g = MDP(grid, (start_state_row, start_state_col), (end_state_row, end_state_col) , discount , convergence , slip_prob)



values = value_iteration(g)
moves = policy_evaluation(g , values)


for i in values:
    print(i)
    
for i in moves:
    print(i)
