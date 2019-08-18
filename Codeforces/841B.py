# @author Matheus Alves dos Santos

lenght = int(input())
values = map(int, input().split())
first_wins = False

for i in values:
    if (i % 2):
        first_wins = True
        break

print("First") if (first_wins) else print("Second")
