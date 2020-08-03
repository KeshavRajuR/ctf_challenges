from PIL import Image
import numpy as np
import random

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
					'C':'-.-.', 'D':'-..', 'E':'.', 
					'F':'..-.', 'G':'--.', 'H':'....', 
					'I':'..', 'J':'.---', 'K':'-.-', 
					'L':'.-..', 'M':'--', 'N':'-.', 
					'O':'---', 'P':'.--.', 'Q':'--.-', 
					'R':'.-.', 'S':'...', 'T':'-', 
					'U':'..-', 'V':'...-', 'W':'.--', 
					'X':'-..-', 'Y':'-.--', 'Z':'--..', 
					'1':'.----', '2':'..---', '3':'...--', 
					'4':'....-', '5':'.....', '6':'-....', 
					'7':'--...', '8':'---..', '9':'----.', 
					'0':'-----', ', ':'--..--', '.':'.-.-.-', 
					'?':'..--..', '/':'-..-.', '-':'-....-', 
					'(':'-.--.', ')':'-.--.-'}

def encrypt(message): 
	cipher = '' 
	for letter in message: 
		if letter != ' ': 
			cipher += MORSE_CODE_DICT[letter] + ' '
		else: 
			cipher += ' '

	return cipher

def passwd_gen():
    length = random.randint(24, 36)
    return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(length))

password = passwd_gen()

print(password.lower())

morse = encrypt(password.upper())

cipher = []
cipher.append("")

morse_array = []
morse_array.append(0)

min_width = 0

for char in morse:
    if char == ".":
        morse_array.append(1)
        morse_array.append(0)
    elif char == "-":
        morse_array.append(1)
        morse_array.append(1)
        morse_array.append(1)
        morse_array.append(0)
    elif char == " ":
        if len(morse_array) > min_width:
            min_width = len(morse_array)
        cipher.append(morse_array)       
        morse_array = []
        morse_array.append(0)

w = min_width + 3
h = 2 + len(password) * 2
t = (h, w, 3)

color1r = color2r = 0
color1g = color2g = 0
color1b = color2b = 0

while(color1r == color2r and color1g == color2g and color1b == color2b):
    color1r = random.randint(0,255)
    color1g = random.randint(0,255)
    color1b = random.randint(0,255)
    
    color2r = random.randint(0,255)
    color2g = random.randint(0,255)
    color2b = random.randint(0,255)

A = np.zeros(t, dtype=np.uint8)

for i in range(h):
    if i % 2 == 0:
        if i == h - 1:
            for j in range(w):
                A[i, j] = [color1r, color1g, color1b]
        else:
            for j in range(w):
                if j < len(cipher[int(i / 2)]):
                    if cipher[int(i / 2)][j] == 1:
                        A[i, j] = [color2r, color2g, color2b]
                    elif cipher[int(i / 2)][j] == 0:
                        A[i, j] = [color1r, color1g, color1b]
                else:
                    A[i, j] = [color1r, color1g, color1b]
    else:
        for j in range(w):
            A[i, j] = [color1r, color1g, color1b]

i=Image.fromarray(A, "RGB")
i.save('password.png')
