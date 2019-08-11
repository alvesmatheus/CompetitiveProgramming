# @author Matheus Alves dos Santos

n_notes = int(input())
notes = input().split()
notes.sort()

if (notes[0] == '1'):
    print(-1)
else:
    print(1)
