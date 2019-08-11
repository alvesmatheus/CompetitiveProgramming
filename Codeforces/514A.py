# @author Matheus Alves dos Santos

def transform_digit(digit):
    if (int(digit) > 4):
        return str(9 - int(digit))
    return digit

number = input()
transformed_digits = []

for digit in number:
    transformed_digits.append(transform_digit(digit))

if (transformed_digits[0] == '0'):
    transformed_digits[0] = '9'

print(''.join(transformed_digits))