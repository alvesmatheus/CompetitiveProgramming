# @author Matheus Alves dos Santos

number = int(input())

beautiful_divs = [1, 6, 28, 120, 496, 2016, 8128, 32640, 130816]
for i in beautiful_divs:
    if ((number % i) == 0):
        greater = i

print(greater)
