from pwn import *
import string
import random
import time
context.log_level='critical'
p=remote("127.0.0.1",1234)
i=0

try:
	while True:
		p.clean()
		p.sendline(str(i+1))
		print(p.recv())
		i+=1
except:
	exit()
	
