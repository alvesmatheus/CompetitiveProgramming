# @author Matheus Alves dos Santos

def find_not_divisible(n, k, start_at, end_at):
    half = (start_at + end_at) // 2
    not_divisibles = half - (half // n)

    if start_at > end_at:
        return start_at
    if k <= not_divisibles:
        return find_not_divisible(n, k, start_at, half - 1)

    return find_not_divisible(n, k, half + 1, end_at)


n_tests = int(input())
MIN_VALUE, MAX_VALUE = 1, 10000000000000

for i in range(n_tests):
    n, k = map(int, input().split())
    print(find_not_divisible(n, k, MIN_VALUE, MAX_VALUE))
