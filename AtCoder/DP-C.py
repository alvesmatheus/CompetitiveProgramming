# @author Matheus Alves dos Santos

n_days = int(input())
activities, happiness = [], []

for i in range(n_days):
    daily_activities = list(map(int, input().split()))
    activities.append(daily_activities)

happiness.append(activities[0])
for i in range(1, n_days):
    happiness.append([
        activities[i][0] + max(happiness[i - 1][1], happiness[i - 1][2]),
        activities[i][1] + max(happiness[i - 1][0], happiness[i - 1][2]),
        activities[i][2] + max(happiness[i - 1][0], happiness[i - 1][1])
    ])

print(max(happiness[n_days - 1]))
