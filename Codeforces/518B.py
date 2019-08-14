# @author Matheus Alves dos Santos

def invert_case(c):
	if c.isupper():
		return c.lower()
	return c.upper()

letters = {c: 0 for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"}
whoops = 0
yay = 0

message = list(input())
newspaper = list(input())

for c in newspaper:
	letters[c] += 1

for i in range(len(message)):
	if (letters[message[i]] > 0):
		letters[message[i]] -= 1
		message[i] = "."
		yay += 1

for i in range(len(message) - 1, -1 , -1):
	if message[i] == ".":
		message.pop(i)

for c in message:
	if (letters[invert_case(c)] > 0):
		letters[invert_case(c)] -= 1
		whoops += 1

print(yay, whoops)
