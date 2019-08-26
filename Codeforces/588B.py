# @author Matheus Alves dos Santos

import math

divisors = []
answer = 1
i = 0

number = int(input())
sqrt = int(math.floor(math.sqrt(number)))

for j in range(1, sqrt + 1):
    if ((number % j) == 0):
        divisors.append(j)
        divisors.append(number // j)
divisors.sort(reverse = True)

while (True): 
    sqrt = math.sqrt(divisors[i])
    if ((sqrt % 1) == 0):
        i += 1
    
    bln = True
    last = divisors[i]
    sqrt = int(math.sqrt(last))
    
    for j in range(2, sqrt + 1):
        if ((last % j) == 0):         
            if ((math.sqrt(last // j) % 1 == 0) or ((math.sqrt(j) % 1) == 0)):
                bln = False
                break
                
    if (bln):
        answer = last
        break
    else:
        i += 1    

print(int(answer))