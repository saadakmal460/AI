import random


class Game:
    def __init__(self, number):
        self.number = number
        self.turn = 1
        
    def start_state(self):
        return (self.number,self.turn)

    def is_end(self, state):
        number,turn=state
        return  number== 0
    
    def utility(self,state):
        
        assert self.is_end(state)
        number,turn=state
        
        return (turn,float('inf'))
            
    
    def actions(self,state):
        
        number,turn=state

        if turn == -1:
            action = self.opponent()
        else:
            action = self.player()
            
        return action
    
    
    def player(self):
        
        action = input('Enter you move: ')    
        return action
    
    def opponent(self):
        return random.choice(['D', 'M'])
    
    
    def succ(self,state,action):
        
        number,turn = state        
        if action == 'M':
            return (number-1,-turn)
        if action == 'D':
            return (number//2,-turn)
               
 


number = int(input('Enter number to start game: ')) 
g = Game(number)

state = g.start_state()


while True:
    action = g.actions(state)
    move = g.succ(state , action)
    print(f'Move: {({move} , {action})} ')
    if g.is_end(move):
        
        number,player = move
        turn,utility = g.utility(move)
        if player == 1:
            print(f'You won!! Your utlitlty {utility}')
        else:
            print(f'You lost!! Your utlitlty {-utility}')
        break
    
    else:
        state = move