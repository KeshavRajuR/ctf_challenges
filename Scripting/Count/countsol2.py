from pwn import *
import string
import random
import time
context.log_level='critical'
p=remote("127.0.0.1",1234)
i=0

try:
	while True:
		output = p.recv()
		print(output)
		num=output[-10:].strip("\n").split()
		#print(num)
		#print(int(num[-1]))
		number = int(num[-1])+1
		p.sendline(str(number))
except:
	exit()

	
