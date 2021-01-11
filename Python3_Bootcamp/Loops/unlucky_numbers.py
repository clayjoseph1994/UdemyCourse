#This program simply prints the numbers in the specified range and assigns them a value of even, odd, or unlucky 
for x in range(1,21):
	#converting x to a string and storing as n
	n = str(x)
	if x == 4 or x ==13:
		state = "unlucky"
	elif x % 2 == 0:
		state = "even"
	elif x % 2 != 0:
		state = "odd"
	print(f"{n} is {state}")
