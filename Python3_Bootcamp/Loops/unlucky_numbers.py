for x in range(1,21):
	n = str(x)
	if x == 4 or x ==13:
		state = "unlucky"
	elif x % 2 == 0:
		state = "even"
	elif x % 2 != 0:
		state = "odd"
	print(f"{n} is {state}")
