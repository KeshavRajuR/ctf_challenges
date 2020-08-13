
for i in range(200):
	print("How good is your typing")
	num=int(input("Enter the number after {}\n".format(i)))
	if not num == i+1:
		print("Wromg number")
		exit()
print("flag{aut0mated_c0unt1ng_1s_3asy}")
