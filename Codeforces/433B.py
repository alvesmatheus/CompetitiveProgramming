# @author Matheus Alves dos Santos

n_stones = int(input())
costs = map(int, input().split())
questions = int(input())

sum1 = [0] * 100001
sum2 = [0] * 100001

for i in range(1, n_stones + 1):
    sum1[i] = sum1[i - 1] + costs[i - 1]
costs.sort()     

for i in range(1, n_stones + 1):
    sum2[i] = sum2[i - 1] + costs[i - 1]
        
for i in range(questions):
    t, left, right = map(int, input().split())
    
    if (t == 1):
        print(sum1[right] - sum1[left - 1])
    else:
        print(sum2[right] - sum2[left - 1])

