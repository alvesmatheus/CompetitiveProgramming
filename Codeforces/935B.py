# @author Matheus Alves dos Santos

def move(x, y, move):
    if( move == "R"):
        return x + 1, y
    return x, y + 1

n_moves = int(input())
moves = input()

x, y, coins = 0, 0, 0
x, y = move(x, y, moves[0])
at_right_kingdom = (x > y)

for i in moves[1:]:
    x, y = move(x, y, i)
        
    if (at_right_kingdom and (x < y)):
            at_right_kingdom = False
            coins += 1
    elif (not at_right_kingdom and (x > y)):
            at_right_kingdom = True
            coins += 1

print(coins)
    
