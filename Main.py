a = int(input("Enter First Number:\n"))
b = int(input("Enter Second Number:\n"))
c = max(a, b)

while(True):
	if(c%a==0 and c%b==0):
		break
	c = c + 1

print("LCM of given two number is", c)