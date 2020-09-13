import re

def fnd(sum):
	rezult = 0
	i = 2
	while True:
		if sum%i == 0:
			if sum/i == 1:
				rezult +=i
				break
			else:
				sum/=i
				#print(i,end =' ')
				rezult +=i
				i=2
		else:
			i+=1
	return rezult			

email = 'dr.haoooooos6@yandex.ru'

reg = re.compile('[^a-zA-Z ]')
email = reg.sub('', email).lower()

sum = 0
for letter in email:
		sum+=ord(letter)-96

print(sum)
rez = fnd(sum)
while rez != fnd(rez):
	rez = fnd(rez)
	
print(rez)