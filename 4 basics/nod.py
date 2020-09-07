def nod(n,m):
	max = 0
	for i in range(1,m+1):
		if(n%i==0 and m%i==0 and max<i):
			max = i
	return max

n,m = map(int, input().split())
print('GCD of ' + str(n) + ' and ' + str(m) + ' is ' + str(nod(n,m)))				