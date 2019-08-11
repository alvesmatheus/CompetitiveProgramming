# @author Matheus Alves dos Santos

def charge_discharge(x, y):
    return x + 1, y - 2

p1, p2 = map(int, input().split())
minutes = 0

while ((p1 > 0) and (p2 > 0) and not ((p1 == 1) and (p2 == 1))):
    minutes += 1

    if (p1 == 1):
        p1, p2 = charge_discharge(p1, p2) 
    elif (p2 == 1):
        p2, p1 = charge_discharge(p2, p1)
    elif (p1 < p2):
        p1, p2 = charge_discharge(p1, p2)
    else:
        p2, p1 = charge_discharge(p2, p1)
    
print(minutes)
