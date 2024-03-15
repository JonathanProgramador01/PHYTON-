from sources import *
import random



def suma(Cartas):
    sum=0
    for a in Cartas:
        sum+=a
    return sum
 
def opciones():
    return input("DO YOU WANTT TO PLAYY A GAME OF BLACKJACK TYPE Y / N :  ").lower()




def quien_gano (cartas_j,cartas_m,jugador,maquina):
    
    print(f"\nYour final hand {cartas_j}, final score: {jugador}")
    print(f"\nComputer final hand {cartas_m}, final score: {maquina}")
       
    if jugador>maquina:
        print("YOUUU WINNNNN\n") 
    elif jugador<maquina:
        print("YOOOUUU LLLOSSEEE\n")
    else:
        print("YOUUUU AREEEE TIEEEDD\n")         

                    
          
    
    
    
    

  
          
YN=input("Do you want to play backjack 21 Type Y / N :   ")
   
def inicio(YN):
    
    
    if YN=="Y":
        
        print(logo)
        Cartas_del_jugador=[random.choice(cards),random.choice(cards)]   # esto de aca es para generar tus numeros al azar
        score_ususario=suma(Cartas_del_jugador)
        Cartas_dela_maquina=[random.choice(cards),random.choice(cards)]
        score_maquina=suma(Cartas_dela_maquina)
        
        
        
        
        
        if 11 in Cartas_del_jugador and 10 in Cartas_del_jugador:
            print(f"Your cards: {Cartas_del_jugador}, current score: {score_ususario}")
            print("\n\nYouu winnn you have a Blackjack Housem\n\n")
            if (opciones()=='y'): inicio("Y")
        elif 11 in Cartas_dela_maquina and 10 in Cartas_dela_maquina:
            print(f"Your cards: {Cartas_del_jugador}, current score: {score_ususario}")
            print(f"Computer cards: {Cartas_dela_maquina}, current score: {score_maquina}")
            print("\n\nYouu loseee the machinee have a blackjack\n\n")
            if (opciones() =='y'): inicio("Y")
        elif 11 in Cartas_del_jugador and 10 in Cartas_del_jugador and 11 in Cartas_dela_maquina and 10 in Cartas_dela_maquina:
            print("AA TIEDDDD YOU ARE OF A GOOD LOKKYY TODAYYY BOTHH GET 21 :)))) ")
        
        
        
        
        print(f"Your cards: {Cartas_del_jugador}, current score: {score_ususario}")
        print(f"Computer's first card: {Cartas_dela_maquina[0]}\n")
        
        
        while(True): 
            add_or_no=input("Type 'y' to get an other card or 'n' to pass: ").lower()
            if add_or_no=="y":
                Cartas_del_jugador.append(random.choice(cards))
                score_ususario=suma(Cartas_del_jugador)
                print(f"Your cards: {Cartas_del_jugador}, current score: {score_ususario}")
                print(f"Computer's first card: {Cartas_dela_maquina[0]}\n")
                
                if score_ususario>21:
                    print("YOOU LOSEEE YOU HAVE MORE THAN 21  \n")
                    if (opciones()=="y"):inicio("Y")
                    else:exit(1)
                    
                    
                    
                    
                    
            else:
            
            
                while score_maquina<16:
                    Cartas_dela_maquina.append(random.choice(cards))
                    score_maquina=suma(Cartas_dela_maquina)    
                quien_gano(Cartas_del_jugador,Cartas_dela_maquina,score_ususario,score_maquina)     
                if opciones()=="y": inicio("Y")
                else:exit(1)
                break
            
        
        
        
           
    else:
        print("ADIOSSS\n")
        
inicio(YN)