#PIL is used for Image processing
from PIL import Image
import time

#We are first loading the image, converting it to RGB and later storing the RGB values of first pixel
img = Image.open('password.png')
rgb_im = img.convert('RGB')
red, green, blue = rgb_im.getpixel((0, 0))

background_color = [red, green, blue]

#Conversion table for Morse to ASCII
CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

#We will be dealing with converting Morse to ASCII, so WRT to dictionary above, this is reversed
CODE_REVERSED = {value:key for key,value in CODE.items()}

#Function that takes care of the conversion. It's a good practice to shift the final answer to lower case
def from_morse(s):
    password = ''.join(CODE_REVERSED.get(i) for i in s.split())
    print(password.lower())

#Some variables that are needed
morse = ""
count = 0
flag = 0

#This is where the processing and extraction of Morse code happens
#Note: The size and colour scheme of different images are different. That is why we store the RGB value of the first pixel and also it's dimensions.
#In Morse code, 1 dot is taken as '.' and 3 dots are taken as '-'. That is how we are getting the code here. Dots here are basically individual pixels
for j in range(img.size[1]):
    for i in range(img.size[0]):
        r, g, b = rgb_im.getpixel((i, j))
        font_color = [r, g, b]
        if background_color != font_color:
            count = count + 1
            flag = 1
        if flag == 1 and background_color == font_color:
            if count == 3:
                morse = morse + "-"
            elif count == 1:
                morse = morse + "."
            flag = 0
            count = 0
    morse = morse + " "

#Here we are calling the Morse converter program
from_morse(morse)
