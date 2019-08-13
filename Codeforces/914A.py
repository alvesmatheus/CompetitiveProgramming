# @author Matheus Alves dos Santos

n = int(input())
sequence = list(map(int, input().split()))
sequence.sort(reverse = True)

for i in sequence:
    if (i < 0):
        unperfect_square = i
        break
    elif ((round(i ** 0.5) ** 2) != i):
        unperfect_square = i
        break

print(unperfect_square)

