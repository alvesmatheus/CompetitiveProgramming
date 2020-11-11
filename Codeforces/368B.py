# @author Matheus Alves dos Santos

n_values, n_tests = map(int, input().split())
values = list(map(int, input().split()))

distinct_values = [0] * 100010
found_values = [False] * 100010

for i in range(n_values - 1, -1, -1):
    value = values[i]
    if not found_values[value]:
        distinct_values[i + 1] += 1
    found_values[value] = True

for i in range(n_values, -1, -1):
    distinct_values[i] += distinct_values[i + 1]

for i in range(n_tests):
    target_index = int(input())
    print(distinct_values[target_index])
