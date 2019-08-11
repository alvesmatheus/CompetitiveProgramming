# @author Matheus Alves dos Santos

players = [1, 2, 3]
possible = True

n_games = int(input())
for i in range(n_games):
    winner = int(input())
    
    if winner == players[0]:
        players[1], players[2] = players[2], players[1]
    elif winner == players[1]:
        players[0], players[2] = players[2], players[0]
    else:
        possible = False
        break

if (possible):
    print('YES')
else:
    print('NO')
