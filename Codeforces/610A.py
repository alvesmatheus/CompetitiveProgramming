# @author Matheus Alves dos Santos

def divisible_by(value, n):
    return ((value % n) == 0)

length = int(input())
ways = 0

if (divisible_by(length, 2)):
    ways = (length // 4)
    
    if (divisible_by(length, 4)):
        ways -= 1

print(ways)