numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for a in range(len(numbers) + 1):
	if a > 1:
		for b in range(2, a):
			if a % b == 0:
				not_primes.append(a)
				break
		else:
			primes.append(a)



print('Primes:', primes)
print('Not primes:', not_primes)