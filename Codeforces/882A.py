# @author Matheus Alves dos Santos

values = list(map(int, input().split()))
minimum = min(values)
factorial = 1

while (minimum > 1):
    factorial *= minimum
    minimum -= 1

print(factorial)