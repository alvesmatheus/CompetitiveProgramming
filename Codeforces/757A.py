# @author Matheus Alves dos Santos

letters = input()
counter = [0, 0, 0, 0, 0, 0, 0]

for c in letters:
    if (c == 'B'):
        counter[0] += 1
    elif (c == 'u'):
        counter[1] += 1
    elif (c == 'l'):
        counter[2] += 1
    elif (c == 'b'):
        counter[3] += 1
    elif (c == 'a'):
        counter[4] += 1
    elif (c == 's'):
        counter[5] += 1
    elif (c == 'r'):
        counter[6] += 1

counter[1] //= 2
counter[4] //= 2

print(min(counter))
