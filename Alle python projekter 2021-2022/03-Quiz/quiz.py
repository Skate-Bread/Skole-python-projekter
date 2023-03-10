#lag en liste med alle spørsmålene + svarene i en separat liste.
sp = ["Hvilken windows er den nyeste?: ", "Hvilken måned har Benjamin bursdag?: ", "Hvilket år er det nå?: ", "Hvilken tempratur koker vann?: ", "Hvilken tempratur fyser vann?: ", "Hvor høy er galdhøpiggen?: ", "Hvor mange dager er det i et år?: ", "Hvor mange timer er det i en dag?: ", "Hvor mange minutter er det i en time?: ", "Hvor mange sekunder er de i et minutt?: "]
sv = ["11", "Februar", "2022", "100", "-1", "2469", "365", "24", "60", "60"]
#lag en score variabel. 
score = 0
#lag en for loop som looper antall ganger med langdene på arraysa. Print så ut første spørsmål.
#Etter det så henter vi "sv" arrayen og sjekker om den stemmer med det brukeren har skrevet inn.
#hvis brukeren får riktig så legger vi til +1 på score.
for i in range(len(sp)):
    print(sp[i])
    svar = input("Skriv in svar: ")
    if svar == sv[i]:
        print ("Riktig!") 
        score = score +1
    else: print ("Feil!")
#Til slutt så printer vi ut total scoren!
print("Du fikk", score, "riktige svar")
     
