# @author Matheus Alves dos Santos

n_balls, n_colors, new_ball = map(int, input().split())
balls = list(map(int, input().split()))

answer = 0

for i in range(n_balls):
    copy = balls[:]
    copy.insert(i, new_ball)
    
    while (len(copy) > 2):
        size = len(copy)
        for j in range(2, len(copy)):          
            if ((copy[j - 2] == copy[j - 1]) and (copy[j - 1] == copy[j])):
                cut = j + 1
                while (cut < len(copy)):
                    if (copy[j] != copy[cut]):
                        break
                    cut += 1
                copy = (copy[:j - 2] + copy[cut:])
                break
        
        if (len(copy) == size):
            break
    
    answer = max(answer, n_balls - len(copy))        
    
print(answer)