# @author Matheus Alves dos Santos

import math

def get_primes(upper_limit):
    

    primes = [True] * (upper_limit + 1)
    size = int(math.ceil(math.sqrt(len(primes))))
    primes[0], primes[1] = False, False

    for i in range(2, size):
        if (primes[i]):
            for j in range(2 * i, len(primes), i):
                primes[j] = False
    
    return primes

primes = get_primes(1000000)
n_values = int(input())
values = map(int, input().split())

for v in values:
    sqrt_v = math.sqrt(v)
    answer = primes[int(sqrt_v)] if (sqrt_v % 1 == 0) else False    

    print("YES") if answer else print("NO")
    