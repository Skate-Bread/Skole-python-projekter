import matplotlib.pyplot as plt
#lag en algorytme som finner den optimale høyden på en boks slik at den får høyes volum
#Det vi begynner med er å liste variablene som er bredda, lengden og inkrementet/høyden på arket
#så tar vi lengeden å deler den på 2 slik at vi finner den største verdien som høyden kan nå
brukerinput = float(input("Skriv in høyde på boksen: "))
bredde = 21
lengde = 29.7
hoydeink = 0
maks = lengde / 2
vol = 0.1
svar = []
hoyde= []

def formel (hoydeink):
   vol = (bredde-2*hoydeink)*(lengde-2*hoydeink)*hoydeink
   return vol

brukersvar = formel(brukerinput)
print(brukersvar, " Dette er volumet på boksen din, utifra høyden du oppgidde ")

#så lager vi en while loop som looper med 0.1 inkrement slik at vi kan teste om det er det er det mest optimale volum 
while hoydeink < maks and vol > -1:
    #vi sjekker volumet med V=(bredde-2*x)*(side-2*x)*x denne formelen 
    vol = formel(hoydeink)
    hoydeink = hoydeink + 0.1
    #så lager vi en if statment som sjekker hvem av disse som er høyest 
    #dette gjør vi ved hjelp av > operatoren 
    hoyde.append(hoydeink)
    svar.append(vol)

#Til slutt printer vi ut den optimale høyden og volumet
print(round(max(svar)/ 1000,2),"liter, er den mest optimale")
plassering = svar.index(max(svar))
print(round(hoyde[plassering],2),"høyde i cm, er den mest optimale")
#jeg vil også gjør algorytmen skalerbar som jeg løser med lister over størrelse på flere ark.

brukerJN = input("Ønsker du en kurve over hva slags høyde som er mest optimal? (Svar med ja eller nei):")
svarlower =  brukerJN.lower()
while svarlower == "ja":
 plt.plot(svar, label = "Forsøk")
 plt.ylabel("Antall milliliter")
 plt.xlabel("Høyden på boksen i millimeter")
 plt.title("Graf over endring i høyden på boksen")
 plt.legend()
 plt.show()
 exit()