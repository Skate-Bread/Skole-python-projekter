#lag en algorytme som finner den optimale høyden på en boks slik at den får høyes volum
#Det vi begynner med er å liste variablene som er bredda, lengden og inkrementet/høyden på arket
#så tar vi lengeden å deler den på 2 slik at vi finner den største verdien som høyden kan nå
bredde = 21
lengde = 29.7
hoydeink = 0
maks = lengde / 2
vol = 0
vol1 = 0
svar = []
hoyde= 0


#så lager vi en while loop som looper med 0.1 inkrement slik at vi kan teste om det er det er det mest optimale volum 
while hoydeink < maks and vol > 0:
    #vi sjekker volumet med V=(bredde-2*x)*(side-2*x)*x denne formelen 
    vol = (bredde-2*hoydeink)*(lengde-2*hoydeink)*hoydeink
    hoydeink = hoydeink + 0.1
    #så lager vi en if statment som sjekker hvem av disse som er høyest 
    #dette gjør vi ved hjelp av > operatoren 
    svar.append(vol)
    if vol > vol1:
    #vi lagrer da disse resultatene i to verdier
        vol1 = vol 
        hoyde = hoydeink




#Til slutt printer vi ut den optimale høyden og volumet
vol1 = round(vol1 / 1000, 2)
print(vol1, "liter", hoyde, " høyde")
print(round(max(svar)/ 1000,2))

#jeg vil også gjør algorytmen skalerbar som jeg løser med lister over størrelse på flere ark.