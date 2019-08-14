# @author Matheus Alves dos Santos

days, min_walks = map(int, input().split())
walks = list(map(int, input().split()))
news_walks = 0

for i in range(1, days):
    j = walks[i]
    if ((j + walks[i - 1]) < min_walks):
        walks[i] = (min_walks - walks[i - 1])
        news_walks += (walks[i] - j)

print(news_walks)
print(" ".join(map(str, walks)))
