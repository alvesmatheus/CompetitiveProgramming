# @author Matheus Alves dos Santos

n_tests = int(input())
impossible_values = [1, 2, 4, 5, 8, 11]

for i in range(n_tests):
    n_chunks = int(input())
    
    if (n_chunks in impossible_values):
        print('NO')
    else:
        print('YES')
