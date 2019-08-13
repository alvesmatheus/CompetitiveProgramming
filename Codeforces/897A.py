# @author Matheus Alves dos Santos

length, n_operations = map(int, input().split())
string = list(input())

for i in range(n_operations):
    l, r, c1, c2 = input().split()
    l, r = int(l), int(r)

    for j in range(l - 1, r):
        if (string[j] == c1):
            string[j] = c2

print(''.join(string))