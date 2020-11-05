# @author Matheus Alves dos Santos

def count_inversions(values, inversions):
    if len(values) <= 1:
        return inversions, values

    half = len(values) // 2
    on_left = count_inversions(values[ : half], inversions)
    on_right = count_inversions(values[half : ], inversions)

    inversions = on_left[0] + on_right[0]
    left_values, right_values = on_left[1], on_right[1]

    return count_side_inversions(left_values, right_values, inversions)


def count_side_inversions(left_values, right_values, inversions):
    i, j, sorted_values = 0, 0, []
    length_left, length_right = len(left_values), len(right_values)

    while (length_left > i) and (length_right > j):
        if (left_values[i] <= right_values[j]):
            sorted_values.append(left_values[i])
            i += 1
        else:
            sorted_values.append(right_values[j])
            j += 1
            inversions += (length_left - i)

    if (i < j):
        sorted_values.extend(left_values[i : ])
    else:
        sorted_values.extend(right_values[j : ])

    return inversions, sorted_values


while True:
    n_values = input()
    if (n_values == '0'):
        break

    values = list(map(int, input().split()))
    inversions, sorted_values = count_inversions(values, 0)
    print(inversions)
