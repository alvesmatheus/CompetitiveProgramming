# @author Matheus Alves dos Santos

def is_sheep_safe(i, j):
    if ((i > 0) and (pasture[i - 1][j] == 'W')):
        return False
    if ((i < rows - 1) and (pasture[i + 1][j] == 'W')):
        return False
    if ((j > 0) and (pasture[i][j - 1] == 'W')):
        return False
    if ((j < columns - 1) and (pasture[i][j + 1] == 'W')):
        return False

    return True

rows, columns = map(int, input().split())

pasture = []
possible = True

for i in range(rows):
    pasture.append(input().replace('.', 'D'))
    
for i in range(rows):
    for j in range(columns):
        if ((pasture[i][j] == 'S') and not is_sheep_safe(i, j)):
            possible = False

if (possible):
    print('Yes')
    for i in pasture:
        print(i)
else:
    print('No')
             
