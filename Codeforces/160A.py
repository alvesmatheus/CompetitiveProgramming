# @author Matheus Alves dos Santos

n_coins = int(input())
coins = list(map(int, input().split()))

coins.sort(reverse = True)
sum_coins = sum(coins)
sum_taken = 0
coins_taken = 0

while (sum_coins >= sum_taken):
    sum_coins -= coins[coins_taken]
    sum_taken += coins[coins_taken]
    coins_taken += 1

print(coins_taken)