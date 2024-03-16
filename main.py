import source
import random
flag2=0


#inciio 
def generar():
    global Opcion_uno,Opcion_dos
    
    
    if flag2==1:
        Opcion_dos=random.choice(source.data) #no hacer esto 
    elif flag2==2:  
        Opcion_uno=Opcion_dos
        Opcion_dos=random.choice(source.data)
    else:
        Opcion_uno=random.choice(source.data) #no hacer esto 
        Opcion_dos=random.choice(source.data)
        



def imprimir(Opcion_uno,Opcion_dos,score):
    
    print(source.line)
    print(f"YOUR SCORE IS : {Score}")
    print(f"Compare: A {Opcion_uno['name']}, a {Opcion_uno['description']}, from {Opcion_uno['country']}")
       
    print(source.vs)
    
    print(f"Compare: B {Opcion_dos['name']}, a {Opcion_dos['description']}, from {Opcion_dos['country']}")
    print(source.line)


def decide (Opcion_uno,Opcion_dos,chose):
    global flag2
 
    if (chose=="A"):
        
        if Opcion_uno["follower_count"]>Opcion_dos["follower_count"]:
            flag2=1
            return True
        else:
            return False
    else:
        
        if Opcion_dos["follower_count"]>Opcion_uno["follower_count"]:
            flag2=2
            return True
        else:
            return False
        
            
            
Score=0

print(source.logo)
while True:
  
    generar()
    imprimir(Opcion_uno,Opcion_dos,Score)
    chose=input("Who has more followers? Type 'A' or 'B':")
    
    if decide(Opcion_uno,Opcion_dos,chose):
        Score+=1
        
    else:
        print("YOOUUU LOSEEE , YOUR SCORE WAS:  ",Score)
        break






