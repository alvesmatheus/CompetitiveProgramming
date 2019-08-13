# @author Matheus Alves dos Santos

def is_even(value):
    return ((value % 2) == 0)

n_cards = int(input())
cards = list(map(int, input().split()))

pointers = [0, n_cards - 1]
score = [0, 0]

player_flag = True
for i in range(n_cards):
    if (is_even(n_cards) and (pointers[0] > pointers[1])):
        break
    
    if (player_flag):
        player_flag = False
        if (cards[pointers[0]] >= cards[pointers[1]]):
            score[0] += cards[pointers[0]]
            pointers[0] += 1
        else:
            score[0] += cards[pointers[1]]
            pointers[1] -= 1
    else:
        player_flag = True
        if (cards[pointers[0]] >= cards[pointers[1]]):
            score[1] += cards[pointers[0]]
            pointers[0] += 1
        else:
            score[1] += cards[pointers[1]]
            pointers[1] -= 1

print(score[0], score[1])
