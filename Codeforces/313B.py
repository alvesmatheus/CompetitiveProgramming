# @author Matheus Alves dos Santos

string = input()
queries = [0] * (len(string) + 1)

for i in range(1, len(string)):   
    if(string[i] != string[i - 1]):
        queries[i + 1] = queries[i]
    else:
        queries[i + 1] = queries[i] + 1

n_queries = int(input())
for i in range(n_queries):
    left, right = map(int, input().split())    
    print(queries[right] - queries[left])
