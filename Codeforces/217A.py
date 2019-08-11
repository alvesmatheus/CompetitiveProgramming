# @author Matheus Alves dos Santos

def drift_dfs(root):
    visited_drifts[root] = True

    for i in range(n_drifts):
        if(not visited_drifts[i]):
            if ((drifts[root][0] == drifts[i][0]) or (drifts[root][1] == drifts[i][1])):
                drift_dfs(i)

n_drifts = int(input())
drifts = [None] * 1000
visited_drifts = [False] * 1000

for i in range(n_drifts):
    x, y = map(int, input().split())
    drifts[i] = (x, y)

new_drifts = 0
for i in range(n_drifts):
    if (not visited_drifts[i]):
        drift_dfs(i)
        new_drifts += 1

print(new_drifts - 1)
