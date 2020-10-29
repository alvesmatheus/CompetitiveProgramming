# @author Matheus Alves dos Santos

n_piles, n_colors = map(int, input().split())
pile_sizes = list(map(int, input().split()))

max_size, min_size = 1, 100
for size in pile_sizes:
    if size > max_size:
        max_size = size
    if size < min_size:
        min_size = size

if (max_size - min_size) <= n_colors:
    print('YES')    
    for size in pile_sizes:
        painted_pebbles = [str((p % n_colors) + 1) for p in range(size)]
        print(' '.join(painted_pebbles))
else:
    print('NO')
