numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        numbers.remove(i)
        continue
    elif i != 1:
        for j in range(2,i):
            if (i % j) == 0:
                not_primes.append(i)
                break
        else:
            continue
else:
    for i in not_primes:
        numbers.remove(i)
    primes = numbers
print('Primes: ', primes)
print('Not Primes: ', not_primes)
