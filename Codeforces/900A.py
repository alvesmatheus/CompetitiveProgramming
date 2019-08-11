# @author Matheus Alves dos Santos

n_points = int(input())
left, right = 0, 0

for i in range(n_points):
    if (int(input().split()[0]) < 0):
        left += 1
    else:
        right += 1
        
if ((left > 1) and (right > 1)):
    print("No")
else:
    print("Yes")
