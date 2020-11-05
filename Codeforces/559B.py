# @author Matheus Alves dos Santos

def slice_halves(string, length):
    half = length // 2
    return string[ : half], string[half : ]


def sort_substrings(string):
    length = len(string)

    if (length % 2 == 0):
        left_half, right_half = slice_halves(string, length)
        a, b = sort_substrings(left_half), sort_substrings(right_half)

        return min(f'{a}{b}', f'{b}{a}')
    else:
        return string


def is_equivalent(a, b):
    return (sort_substrings(a) == sort_substrings(b))


a, b  = input(), input()
print('YES' if (is_equivalent(a, b)) else 'NO')
