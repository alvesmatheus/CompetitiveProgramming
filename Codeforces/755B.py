# @author Matheus Alves dos Santos

n, m = map(int, input().split())

common_words = 0
p_words = {}

for i in range(n):
    p_words[input()] = True

for i in range(m):
    if (input() in p_words):
        common_words += 1

print("NO") if ((m > n) or ((n == m) and (common_words % 2 == 0))) else print("YES")