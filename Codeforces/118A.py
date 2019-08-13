# @author Matheus Alves dos Santos

string = input().lower()
vowels = 'aoyeui'
answer = ''

for i in string:
    if i not in vowels:
        answer += ('.' + i)

print(answer)
