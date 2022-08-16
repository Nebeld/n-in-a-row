##############
# x in a row #
##############
#komma zahlen ausprobieren

from itertools import count

print('Welcome to x-in-a-row. \nThere are two players (x and o). "x" begins.')

class Board:
    
    def __init__(self, width, height, win=3):
        self.width = width
        self.height = height
        self.win_length = win
        self.game_status = 'active'
        self.turn_color = 'x'
        self.count_tokens = 0
        self.win = win
        if self.width <2:
            print('Your width must be at least 2')
            self.width = 2
        if self.height <2:
            print('Your height must be at least 2')
            self.height = 2
        self.current_list = [['.'] * self.width for x in range(self.height)]
            
        if self.win <= 1:
            print(f'{self.win}-in-a-row wouldn`t really make sense')
            self.win = width
        if  self.win > height and self.win > width:
            print('This game would be unwinnable')
            self.win = width
            print(f'You are now playing {self.win}-in-a-row\n')
        else:
            print(f'You are now playing {self.win}-in-a-row\n')
        
        string_with_numbers= '|'
        for a in range(1,self.width+1):
            string_with_numbers = string_with_numbers+str(a)+'|'
        print(string_with_numbers)
        print(' '+'\n '.join(map(lambda a:' '.join(map(str, a)), self.current_list))+'\n')
   
    def ascii(self):
        return '\n'.join(['.' * self.width ] * self.height)
    
    def drop(self, column):
        self.column = column
        current_list = self.current_list
        x=1
        
        if self.game_status == 'active':
            try:
                if  current_list[self.height-x][int(column)] == '.':
                    current_list[self.height-x][int(column)] = self.turn_color
                    self.position = ([self.height-x],[int(column)])
                    print('\n '+'\n '.join(map(lambda a:' '.join(map(str, a)), current_list)))
                    x=x+1
                    #change turn_color
                    if self.turn_color == 'x':
                        self.turn_color = 'o'
                    else:
                        self.turn_color = 'x'
                else: 
                    while current_list[self.height-x][int(column)] != '.':
                        x=x+1
                    current_list[self.height-x][int(column)] = self.turn_color
                    self.position = ([self.height-x],[int(column)])
                    print('\n'+'\n'.join(map(lambda a:' '.join(map(str, a)), current_list)))
                    #change turn_color
                    if self.turn_color == 'x':
                        self.turn_color = 'o'
                    else:
                        self.turn_color = 'x'
            except:
                print('This column is full')
            
            ##checks if win##
            #row
            for a in range(len(current_list)):
                string=''.join(current_list[a])
                if string.count('o'*self.win)>0:
                    print('o won')
                    self.game_status = 'over'
                if string.count('x'*self.win)>0:
                    print('x won')
                    self.game_status = 'over'

            #column
            for a in range(len(current_list[0])):
                for b in range(len(current_list)):
                    string=string+current_list[b][a]
                if string.count('o'*self.win)>0:
                    print('o won')
                    self.game_status = 'over'
                if string.count('x'*self.win)>0:
                    print('x won') 
                    self.game_status = 'over' 
                string= ''

            #diagonals
            ul_zu_or = [[] for a in range(len(current_list) + len(current_list[0]) - 1)]
            ur_zu_ol = [[] for a in range(len(current_list) + len(current_list[0]) - 1)]

            for x in range(len(current_list[0])):
                for y in range(len(current_list)):
                    ul_zu_or[x+y].append(current_list[y][x])
                    ur_zu_ol[x-y + len(current_list) - 1].append(current_list[y][x])


            for a in range(len(ul_zu_or)):
                string=''.join(ul_zu_or[a])
                if string.count('o'*self.win)>0:
                    print('o won')
                    self.game_status = 'over'
                if string.count('x'*self.win)>0:
                    print('x won')
                    self.game_status = 'over'

            for a in range(len(ur_zu_ol)):
                string=''.join(ur_zu_ol[a])
                if string.count('o'*self.win)>0:
                    print('o won')
                    self.game_status = 'over'
                if string.count('x'*self.win)>0:
                    print('x won')
                    self.game_status = 'over'
            
            #draw?
            if self.game_status == 'active':
                end=0
                for i in range(self.height):
                    end = end + current_list[i].count('o')
                    end = end + current_list[i].count('x')
                if end == self.height*self.width:
                    print('Draw')
                    self.game_status = 'over'

            #next?
            if self.game_status == 'active':
                print(f'\nIt`s {self.turn_color}`s turn')
                
                
a = 'a' 
b = 'b'
c = 'c'  

                         
while a.isdigit() == False:                          
    a = input('Now type the width of your game ')
while b.isdigit() == False: 
    b = input('Now type the heigth of your game ')
while c.isdigit() == False:
    c = input('With how many identical tokens in a row do you want to win? ')       
board = Board(int(a),int(b),int(c))
while board.game_status == 'active':
    try:
        d= input('Which column do you want to drop your token? ')     
        board.drop(int(d)-1)
    except:
        print(f'You have to insert a number between 1 and {board.width}\n')
