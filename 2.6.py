def stairs(n):
	if n <= 1:
		return n
	return stairs(n-1) + stairs(n-2)

def countWays(s):
	return stairs(s + 1)

s = int(input("Enter the number : "))
print ("Number of ways = ")
print (countWays(s))


