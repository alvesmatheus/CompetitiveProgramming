# @author Matheus Alves dos Santos

basics = ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99"]
zcy = [11, 22, 33, 44, 55, 66, 77, 88, 99]

total = 0
k, p = map(int, input().split())

if (len(zcy) < k):
    for i in zcy:
        for j in basics:
            copy = str(i)
            half = (len(copy) // 2)
            copy = copy[:half] + j + copy[half:]
            zcy.append(int(copy))
                 
        if (len(zcy) >= k):
            break

for i in range(0, k):
    total += zcy[i]

print(total % p)
