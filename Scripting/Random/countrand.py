import random
try:
	for i in range(200):
		rand = random.randint(0,999)
		print("How good is your typing")
		num=int(input("Enter the number after {}\n".format(rand)))
		if not num == rand+1:
			print("Wromg number")
			exit()
except:
	exit()
print("flag{nice_c0unting_random}")
