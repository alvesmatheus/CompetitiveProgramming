# @author Matheus Alves dos Santos

n_cities = int(input())
cities = list(map(int, input().split()))

print(abs(cities[1] - cities[0]), abs(cities[n_cities - 1] - cities[0]))

for i in range(1, n_cities - 1):
    nearest = min(abs(cities[i] - cities[i - 1]), abs(cities[i + 1] - cities[i]))
    farthest = max(abs(cities[i] - cities[0]), abs(cities[n_cities - 1] - cities[i]))
    print(nearest, farthest)

print(abs(cities[n_cities - 1] - cities[n_cities - 2]), abs(cities[n_cities - 1] - cities[0]))
