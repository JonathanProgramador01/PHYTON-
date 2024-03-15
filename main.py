import random
from source import logo

print(logo)
print("Welcome to the guessing number")
print("Im think in a number 1 and 100")
deficult=input("Chosee the dificult: 'EASY' / 'HARD' ").lower()

#
if deficult =="easy":
    atemps=10
else:
    atemps=5

n=random.randrange()
flag=0   
    
while atemps>0:

    print(f"You have {atemps} reaming to gueess the number")
    ususario=int(input("Make a guess: "))
    if (ususario==n):
        print("""
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
                                                           
              """)
        break
    elif (ususario>n):
        print("Too highttt")
    elif ususario<n:
        print("Tooo loww")
    atemps-=1
    if (atemps==0):
        flag=1

if (flag==1):
    print('''
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝
 ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  
  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  
   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝
                                                                     
          ''')
    