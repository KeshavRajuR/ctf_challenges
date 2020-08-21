flag='flag{y0ur_5cr1p7_w0rk5}'
nums=[68063791, 74483302, 75954910, 96467534, 64068545, 69817667, 96517586, 64135709, 44184432, 48655518, 56677504, 74776856, 79364598, 48235231, 88185035, 83459483, 56882622, 50310192, 95053595, 73229563, 71929296, 41601056, 83688411, 48809058, 41721949, 67212995, 40991969, 58850438, 73723176, 85458243]
banner='''
__          ________ _      _____ ____  __  __ ______ 
\ \        / /  ____| |    / ____/ __ \|  \/  |  ____|
 \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__   
  \ \/  \/ / |  __| | |   | |   | |  | | |\/| |  __|  
   \  /\  /  | |____| |___| |___| |__| | |  | | |____ 
    \/  \/   |______|______\_____\____/|_|  |_|______|
'''
check = 1
i=0
while(check and i<30):
    print(banner)
    print("You are in level :",i)
    inp = input("Enter a number : ")
    try:
        inp = int(inp)
    except:
        print("I said a number -_-")
        exit(0)
    
    if(inp==nums[i] and i==29):
        check=0
        i+=1
        print('You can have it now')
        print(flag)
   
    elif(inp == nums[i]):
        print("Correct! You have leveled up")
        i+=1
    
    else:
        print("Wrong Number :/")
        print("This is the correct number :",nums[i])
        check = 0
