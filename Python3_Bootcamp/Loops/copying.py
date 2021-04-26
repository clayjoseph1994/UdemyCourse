#This program asks the user how's it going and then prompts them to respond. 
#When they do, it repeats their answer back to them infinitely until the user
#responds with "stop copying me"
ans = input("Hey how's it going?")
while ans != "stop copying me":
	print(ans)
	ans = input()
print("Fine, you win")