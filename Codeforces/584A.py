# @author Matheus Alves dos Santos

rules = list(map(int, input().split()))
number = ''

if ((rules[1] == 10) and (rules[0] == 1)):
    number = -1
    
elif (rules[1] == 10):
    number += str(rules[1])
    number += ('0' * (rules[0] - 2))

else:
    number += (str(rules[1]) * rules[0])

print(number)