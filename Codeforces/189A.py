# @author Matheus Alves dos Santos

length, a, b, c = map(int, input().split())

sizes = [a, b, c]
sizes.sort(reverse = True)

dp_list = [0] * (length + 1)
counter = [0] * (length + 1)

for i in range(len(dp_list)):
    for j in range(len(sizes)):
        if (sizes[j] <= i):
            if ((dp_list[i - sizes[j]] + sizes[j]) >= dp_list[i]):
                dp_list[i] = dp_list[i - sizes[j]] + sizes[j]
                counter[i] = max(counter[i], counter[i - sizes[j]] + 1)
    
print(counter[length])
