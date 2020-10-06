# @author Matheus Alves dos Santos

n_houses, girl_house, money = map(int, input().split())
house_costs = list(map(int, input().split()))
girl_house -= 1

min_distance = 100000

for i in range(girl_house - 1, -1, - 1):
    if house_costs[i] > 0 and house_costs[i] <= money:
        distance = (girl_house - i) * 10
        if distance < min_distance:
            min_distance = distance

for i in range(girl_house + 1, len(house_costs)):
    if house_costs[i] > 0 and house_costs[i] <= money:
        distance = (i - girl_house) * 10
        if distance < min_distance:
            min_distance = distance  

print(min_distance)
