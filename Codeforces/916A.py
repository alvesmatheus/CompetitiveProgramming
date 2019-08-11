# @author Matheus Alves dos Santos

snooze_time = int(input())
hours, minutes = map(int, input().split())
n_snooze = 0

while ('7' not in (str(hours) + str(minutes))):
    n_snooze += 1    
    minutes -= snooze_time
    
    if (minutes < 0):
        minutes += 60
        hours -= 1
    
    if (hours < 0):
        hours += 24

print(n_snooze)