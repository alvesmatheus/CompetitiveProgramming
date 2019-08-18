# @author Matheus Alves dos Santos

n, pos, l, r = map(int, input().split())

seconds = 0
if pos < l:
    seconds += (l - pos)
    pos = l
if pos > r:
    seconds += (pos - r)
    pos = r

close_left, close_right = (l > 1), (r < n)

if (close_left and close_right):
    seconds += (min(pos - l, r - pos) + (r - l) + 2)
elif (close_left):
    seconds += (1 + (pos - l))
elif (close_right):
    seconds += (1 + (r - pos))

print(seconds)


