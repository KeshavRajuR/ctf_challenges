import random
flag="flag{bruteforce_for_the_win}"
try:
	while True:
		print("########################################################################################")
		print("Welcome to The Force Network \n\n")
		try:
			option=int(input("Choose any of these options:\n1.Login\n2.Rules\n3.Logout\n"))
		except:
			print("Invalid Input\n\n")
			
		if option == 1:
			user = input("Enter username: ")
			num = random.randint(1,len(flag)-1)
			#print(flag[num-1])
			pass1 = input("Enter the {} letter in password \n".format(num))
			if pass1 == flag[num-1] and user == "admin":
				print("The {} letter in password is CORRECT\n\n".format(num))
			else:
				print("The {} letter in password is WRONG\n\n".format(num))

		elif option == 2:
			print("The password contains only lowercase alphabets and the following characters { _ } \n\n")

		elif option == 3:
			print("GoodBye ... ")
			exit()

		else:
			print("Invalid Input\n\n")
except:
	exit()
