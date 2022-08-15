from itertools import count

alist = [['.', '.', '.', '.', '.'],
         ['o', 'o', 'o', '.', '.'],
         ['.', '.', '.', '.', '.'],
         ['.', '.', 'x', 'x', 'x'],
         ['.', '.', '.', '.', 'x']]
win=3
width = 5
height = 5
x=0

for a in range(width):
    for b in range(width-2):
        for n in range(win-1):
             if alist[a][b] == alist[a][b+n] and alist[a][b] != '.':
                x=x+1
                print(x)
             if x == win:
                print('Win', alist[a][b])
                x=0


for a in range(height):
    for b in range(height-2):
        if alist[b][a] == alist[b+1][a] == alist[b+2][a] and alist[b][a] != '.' and alist[b+1][a] != '.' and alist[b+2][a] != '.':
            print('Win', alist[b][a])
