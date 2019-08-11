# @author Matheus Alves dos Santos

n_lines, n_columns = list(map(int, input().split()))

for i in range(n_lines):
    line = list(input())

    for j in range(n_columns):
        if (line[j] == '.'):
            if ((i % 2) == (j % 2)):
                line[j] = 'B'
            else:
                line[j] = 'W'

    print(''.join(line))
