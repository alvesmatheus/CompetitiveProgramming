# @author Matheus Alves dos Santos

n_intersections = int(input())
shortcuts = list(map(int, input().split()))

shortcuts = [(shortcut - 1) for shortcut in shortcuts]
costs = [0] + ([-1] * (n_intersections - 1))

i, queue = 0, [0]
while (i < len(queue)):
    intersection = queue[i]
    shortcut = shortcuts[intersection]

    if costs[shortcut] == -1:
        costs[shortcut] = costs[intersection] + 1
        queue.append(shortcut)

    if intersection < (n_intersections - 1):
        if costs[intersection + 1] == -1:
            costs[intersection + 1] = costs[intersection] + 1
            queue.append(intersection + 1)  

    if intersection > 0:
        if costs[intersection - 1] == -1:
            costs[intersection - 1] = costs[intersection] + 1
            queue.append(intersection - 1)

    i += 1

print(' '.join(map(str, costs)))
