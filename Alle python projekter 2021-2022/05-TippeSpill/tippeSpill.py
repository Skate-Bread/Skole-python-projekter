import random #inporterer random
igjen = "j" #lager en placeholder for om koden skal kjøre
while igjen == "j":   #denne while loopen kjører så lenge "igjen" = "J" denne variablene kan brukeren endre på på slutten av spillet.
 tall = random.randint(1,10) #genererer et tillferldig tall fra 1 til 10. lager også 2 variabler til forsøk og brukerinput
 forsok = 0
 brukerinput = 0
#Denne while loopen kjører så lenge brukerinput ikke er == tall. 
#I while loopen så sjekker vi om bruker input er lavere, høyere eller det samme som, svaret.
# Hvis den ikke var det samme som svare vil den legge til et forsøk også loope til toppen igjen.
 while not brukerinput == tall: 
     brukerinput = int(input("Skriv inn tall: ")) 
     while brukerinput < 1 or brukerinput > 10:
         print("Tallet du har skrevet er ikke gyldig oppgi et tall fra 1 t.o.m 10 ")
         brukerinput = int(input("Skriv inn tall: ")) 
     if brukerinput > tall:
        print("Tallet er lavere en det du skrev! ")
     elif brukerinput < tall: 
        print("Tallet er høyere en det du skrev!")
     forsok = forsok +1
 print("Du brukte ", forsok, " forsøk!")  #Hær printer vi ut hvor mange forsøk persjonen brukte
 igjen2 = input("Vill du spille igjen?(Skriv J for ja eller N for nei): ") # Hær får brukere mulighet til å svare på om dem vill spille igjen
 igjen = igjen2.lower() #konverterer brukerens svar til lower case



   
