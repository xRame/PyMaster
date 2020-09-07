def rez(n):
	l = []
	i = 2
	while n != 1.0:
		if(n%i==0):
			n /= i
			l.append(i)
			i = 2
		else:	
			i+=1
	print(" ".join(map(str, l)))	

n = int(input())
if(n==1):
	print(1)
else:	
	rez(n)		