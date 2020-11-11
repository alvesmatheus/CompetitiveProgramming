# @author Matheus Alves dos Santos
# Submitted using PyPy

n_items, max_weight = map(int, input().split())
knapsacks, items, row = [], [], ([0] * (max_weight + 1))

knapsacks.append(row.copy())
for i in range(n_items):
    weight, value = map(int, input().split())
    items.append((weight, value))
    knapsacks.append(row.copy())

for i in range(n_items):
    item_weight, item_value = items[i]

    for j in range(max_weight):
        if (j + 1) >= item_weight:
            knapsacks[i + 1][j + 1] = max(
                knapsacks[i][j + 1 - item_weight] + item_value,
                knapsacks[i][j + 1]
            )
        else:
            knapsacks[i + 1][j + 1] = knapsacks[i][j + 1]

max_value = max(knapsacks[n_items])
print(max_value)
