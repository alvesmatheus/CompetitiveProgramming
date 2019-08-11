# @author Matheus Alves dos Santos

def remove_duplicates(values):
    return list(set(values))

n_balls = int(input())
balls = list(map(int, input().split()))
balls = remove_duplicates(balls)
balls.sort()

happy = False
for i in range(0, len(balls) - 2):
    if ((balls[i] + 1) == balls [i + 1]):
        if ((balls[i] + 2) == balls [i + 2]):
            happy = True
            break

if (happy):
    print("YES")
else:
    print("NO")
    


