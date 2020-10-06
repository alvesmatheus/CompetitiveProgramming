# @author Matheus Alves dos Santos

size_s, size_t = map(int, input().split())
s, t = input(), input()

n_changes = 100000
changes_indexes = []

for i in range(size_t - size_s + 1):
    changes = []
    for j in range(size_s):
        if s[j] != t[i + j]:
            changes.append(j)

    if len(changes) < n_changes:
        changes_indexes = changes
        n_changes = len(changes)

print(n_changes)
print(' '.join([str(c + 1) for c in changes_indexes]))
