# @author Matheus Alves dos Santos

n_usbs = int(input())
file_size = int(input())

capacities = []
used_usbs = 0

for i in range(n_usbs):
    capacities.append(int(input()))
capacities.sort(reverse = True)

while (file_size > 0):
    file_size -= capacities[used_usbs]
    used_usbs += 1

print(used_usbs)