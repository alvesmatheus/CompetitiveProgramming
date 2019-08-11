# @author Matheus Alves dos Santos

distance = int(input())
steps = (distance // 5)

if ((distance % 5) != 0):
    steps += 1

print(steps)