# @author Matheus Alves dos Santos

n_employees = int(input())

leaders, subordinates = n_employees - 1, 1
answer = 1

if (n_employees > 2):
    for i in range(n_employees // 2):
        leaders -= 1
        subordinates += 1
        
        if ((leaders % subordinates) == 0):
            answer += 1
    
print(answer)