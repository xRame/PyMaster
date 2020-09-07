def isSimple(n):
	for i in range(2,n-1):
		if n%i==0:
			return False
	return True


if isSimple(x):
	print(str(x) + ' is prime')
else:
	print(str(x) + ' is composite')			