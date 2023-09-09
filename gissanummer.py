#Gissa numret 
#Av Oscar schmerer wolfbrandt

# start system och main manu 
import os
from colors import bcolors
restart = False
exit = False

while restart == False:
    os.system("cls")
    print(bcolors.CYAN + "####################################################################################### \n \n"+ bcolors.WHITE +"                                Välkomen till\n                           "+ bcolors.PURPLE +"G I S S A   N U M R E T\n\n")
    restart = input(bcolors.WHITE +"Tryck på "+ bcolors.GREEN +"y"+ bcolors.WHITE +" för att börja "+ bcolors.GREEN +"q"+ bcolors.WHITE +" för att avsluta och "+ bcolors.GREEN +"r"+ bcolors.WHITE +" för att se regler du är redo att börja \n \n" + bcolors.CYAN + "####################################################################################### \n:").lower()  

    # meny instälningar
    if restart == "y":
        restart = True
    elif restart == "q":
        break
    elif restart == "r":
        print(bcolors.WHITE +"Detta är gissa nummret spelet fungerar på ett enkelt sätt, du ska gissa ett nummer som är någonstans mellan 1 - 100.\nDu kommer att få 7 försök att gissa och varje gång du gissar fel kommer du få reda på om din gissning är störe eller mindre\nFör att spelet ska fungera behöver du skriva ett heltal du får inte skriva decimaler eller bokstäver du kan trycka på \n" + bcolors.GREEN + "q " + bcolors.WHITE +"för att avsuta och"+ bcolors.GREEN +" m "+bcolors.WHITE+"för att ge upp")
        restart = False   
    elif restart != "y" "r" "n":
        print(bcolors.RED + "skriv "+ bcolors.GREEN +"r "+ bcolors.RED +"för att se hur spelaet funkar "+ bcolors.GREEN +"n"+ bcolors.RED +" för att avsluta och "+ bcolors.GREEN +"y "+ bcolors.RED +"för att börja")
        restart = False

        # konfigerering av spelet 
    while restart == True:    
        import random 
        number = random.randint(1, 100)
        guess_amount = 7
        wrong = "det var fel tal"
        slisk = False

        # dett är sjelva spletet   
        while guess_amount > 0:
            try:
                guess=input( bcolors.GREEN +"gissa villket nummer: " + bcolors.WHITE ).lower()
                guess_amount = guess_amount - 1  
                if guess == "q":
                    exit = True
                    break
                elif guess == "m":
                    break 
                guess == int(guess)
                if int(guess) == int(number):
                    print(bcolors.GREEN + "det var rätt bra jobbat, Du klarade det på"+bcolors.WHITE,  7 - guess_amount, bcolors.GREEN+ "gissningar"+ bcolors.WHITE+"\n------------------------------------------")
                    slisk = True
                    break
                elif int(guess) > int(100):
                    print(bcolors.RED + "Gissningen måste vara mindre en "+ bcolors.WHITE +"100")
                    guess_amount = guess_amount + 1 
                elif int(guess) > int(number):
                    print("Din gissning var "+bcolors.UNDERLINE+"STÖRE"+ bcolors.WHITE +" en talet")
                elif int(guess) < int(number):
                    print(bcolors.WHITE + "Din gissning var "+bcolors.UNDERLINE+"MINDRE"+ bcolors.WHITE +" en talet")
                print(bcolors.WHITE +bcolors.RED +"du har"+ bcolors.WHITE , guess_amount, bcolors.RED +"gissningar kvar"+ bcolors.WHITE +"\n------------------------------------------",)
            except:
                print(bcolors.RED + "skriv ett giltigt nummer tack"+ bcolors.WHITE + "\n------------------------------------------")
                guess_amount = guess_amount + 1  
        
        # fel system och omstart
        if exit == True:
            break            
        if slisk == False:                                      
            print(bcolors.RED + "du förlorade nummret var"+ bcolors.WHITE, number)
        x = input(bcolors.WHITE +"Tryck på " + bcolors.GREEN +"q "+ bcolors.WHITE +"för att avslua eller "+ bcolors.GREEN +"r "+ bcolors.WHITE +"för att köra igen trykck på en övriga knapp för att gå till menyn: ").lower()
        if x == "q": 
            os.system("cls")   
            break
        elif x == "r":
            os.system("cls")
            restart = True
        elif x != "q" "y":
            os.system("cls")
            print(bcolors.WHITE + "------------------------------------------" + bcolors.RED + "\n")
            restart = False 