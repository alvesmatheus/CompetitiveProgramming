# @author Matheus Alves dos Santos

n, a, b = map(int, input().split())
positions = 0

for i in range(n):
    if ((i <= (n - a - 1)) and (i <= b)):
        positions += 1

print(positions)