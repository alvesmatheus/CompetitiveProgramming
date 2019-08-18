# @author Matheus Alves dos Santos

n = int(input())
squares = list(map(int, input().split()))

ways = 0
sum_left = 0
sum_right = sum(squares)

for i in range(len(squares) - 1):
    sum_left += squares[i]
    sum_right -= squares[i]
    
    if (sum_left == sum_right):
        ways += 1

print(ways)
