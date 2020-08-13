
for i in range(200):
	print("How good is your typing")
	num=int(input("Enter the number after {}\n".format(i)))
	if not num == i+1:
		print("Wromg number")
		exit()
print("flag{nice_c0unting}")
