#lag en algorytme som finner den optimale høyden på en boks slik at den får høyes volum
#inporter matplotlib som lager diagramer bassert på resultatet. importerer også time slik at programmer ikke lukker seg selv med en gang 
import matplotlib.pyplot as plt
import time

#lag en funsjon som tar in et parimeter den skal inneholde formelen V=(bredde-2*x)*(side-2*x)*x
def formel (hoydeink):
   #kjør formelen med høyden som input
   vol = (bredde-2*hoydeink)*(lengde-2*hoydeink)*hoydeink
   #reurner svaret fra formelen
   return vol

#så spør vi om hvilket type ark brukeren har brukt vi sjkker også om talle er fra og med 10 til og med 10 hvis ikke så looper den og spør igjen
brukerinputark = int(input('Hvilket "A" type ark er det du måler? (tall fra og med 0 til og med 10): '))
while brukerinputark < 0 or brukerinputark > 10:
 print("Det du skrev er ikke et tall fra og med 0 til og med 10 prøv på nytt!")
 brukerinputark = int(input("Hvilket A type ark er det du måler? (tall fra og med 0 til og med 10): "))
#lag tre lister nr1 med navnet på arkene nr2 med bredden på arkene nr3 med lengden på arkene
ark = ["A0","A1","A2","A3","A4","A5","A6","A7","A8","A9","A10"]
storrelseb = [84.1, 59.4, 42.2, 29.7, 21, 14.8, 10.5, 7.4, 5.2, 3.7, 2.6]
storrelsel = [118.9, 84.1, 59.4, 42, 29.7, 21, 14.8, 10.5, 7.4, 5.2, 3.7]  
#skriv til skerm hvilket ark brukeren valgte
print("\nDu valgte ",ark[brukerinputark])
#hent bredden og lengen bassert på hva brukeren valgte. Så opretter vi en variabel for hoyden(inkrement teller) og en for volumet.
bredde = storrelseb[brukerinputark]
lengde = storrelsel[brukerinputark] 
hoydeink = 0
vol = 0
#Vi deler også høyden på 2 slik at vi vet hva maksimal høyde kan være
maks = lengde / 2
#lag to lister en for volumet og en for høyden
svar = []
hoyde= []
#så henter vi høyden på brukerens boks som ikke kan være høyere en maks høyden mulig.
#hvis den er høyere så vill den spørre igjen
brukerinput = float(input("Skriv in høyde på boksen(i cm): "))
while brukerinput > maks or brukerinput < 0:
    print("Verdien du skrev er enten for stor eller for liten!")
    brukerinput = float(input("Skriv in høyde på boksen(i cm): "))
#sen brukerinput gjennom funjonen for å finne volumet.
brukersvar = formel(brukerinput)
#print ut til skjerm hva volumet til brukeren var
print(round(brukersvar/1000,3), "\nLiter. Dette er volumet på boksen din, utifra høyden du oppgidde og arket du valgte.\n")

#så lager vi en while loop som looper med 0.1 inkrement slik at vi kan teste om det er det er det mest optimale volum 
#vi sier også at så lenge høyden ikke er større en makshøyde og volumet ikke er i minus skal den kjøre
while hoydeink < maks and vol >= -1:
    #vi sjekker volumet med V=(bredde-2*x)*(side-2*x)*x via formelen i funksjonen
    vol = formel(hoydeink)
    hoydeink = hoydeink + 0.1
    #så skriver vi inn i listene hva svaret er
    hoyde.append(hoydeink)
    svar.append(vol)
#Til slutt printer vi ut den optimale høyden og volumet
plassering = svar.index(max(svar))
print(round(hoyde[plassering],2),"høyde i cm, er den mest optimale", "som er ",round(max(svar)/ 1000,3),"liter")
print()
#så spør vi brukeren om brukeren ønsker en graf 
brukerJN = input("Ønsker du en kurve over hva slags høyde som er mest optimal? (Svar med J/N):")
#gjør brukerens svar til små bokstaver
svarlower =  brukerJN.lower()
#lag en if statmen som kjører hvis svaret er ja
if svarlower == "j":
 plt.axhline(brukersvar, label = "Med høyden du skrev inn", color='green', linestyle='-', linewidth=3)
 plt.plot(svar, label = "Forsøk")
 plt.ylabel("Antall milliliter")
 plt.xlabel("Høyden på boksen i millimeter")
 plt.title("Graf over endring i høyden på boksen ")
 plt.legend()
 plt.show()
print("Takk for")
time.sleep(5)
