# @author Matheus Alves dos Santos

n_columns = int(input())
columns = list(map(int, input().split()))

columns.sort()
columns = map(str, columns)

print(' '.join(columns))