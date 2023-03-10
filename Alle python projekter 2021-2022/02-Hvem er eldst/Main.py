#lag en input for alder nr1
alder1 = float(input("Skriv in alder nr.1: "))
#lag en input for alder nr2
alder2 = float(input("Skriv in alder nr.2: "))
#lag en if statment som sjekker om alder nr1 er større en alder nr2
if alder1 > alder2 :
    # print ut resultat
    print( "alder 1",  alder1 , " er større enn ","alder 2 ", alder2)
# lag en else if statment som sjkker om alder nr2 er større en alder nr2
if alder2 > alder1:
    # print ut resultat
    print("alder 2", alder2, " er større enn ", "alder 1 ", alder1)
#lag en else if statment som sjekker om alder nr1 er like stor som alder nr2
elif alder2 == alder1:
    #print ut resultat
    print("Begge alderene du har skrevet inn er like")
#lag en else statment som vill si i fra om alderene ikke er i riktig format
else:
    # print ut resultat
    print("verdien du skrev inn er ikke gyldig")












