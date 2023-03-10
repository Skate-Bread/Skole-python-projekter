kjopesum = float(input("Skriv inn kjøpe sum: ")) #henter sum på vare
betalerMed = float(input("Skriv inn betaler sum: ")) #henter hvor mye kunden betaler
while betalerMed < kjopesum: #sjekker at kunder betaler nokk
    print("Kunden betaler ikke nokk oppgi en høyere sum!")
    kjopesum = float(input("Skriv inn kjøpe sum: ")) #henter sum på vare
    betalerMed = float(input("Skriv inn betaler sum: ")) #henter hvor mye kunden betaler

#to lister som lagrer informasjon om vekslene
lapper = [0, 0, 0, 0, 0, 0, 0, 0]
seddler = ["stk 500 lapp", "stk 200 lapp", "stk 100 lapp", "stk 50 lapp", "stk 20 Krone", "stk 10 Krone", "stk 5 Krone", "stk 1 Krone"]
#sjekker hva kunden skal få igjen 
tilbake =  betalerMed - kjopesum 
#Dette er en while loop som kjører så lenge summen fortsatt er over 1. 
# if statmentsa sjekker om summen er delige med 500, 200 osv. ved hjelp av modulo. Så printer den det inn i arrayen. Den suptraherer også seddelen av summen.
while tilbake > 0:
    if tilbake % 500 == 0:
        lapper[0] = lapper [0] + 1
        tilbake = tilbake - 500
    elif tilbake % 200 == 0: 
        lapper[1] = lapper [1] + 1
        tilbake = tilbake - 200
    elif tilbake % 100 == 0: 
        lapper[2] = lapper [2] + 1
        tilbake = tilbake - 100
    elif tilbake % 50 == 0:
        lapper[3] = lapper [3] + 1
        tilbake = tilbake - 50
    elif tilbake % 20 == 0: 
        lapper[4] = lapper [4] + 1
        tilbake = tilbake - 20
    elif tilbake % 10 == 0:
        lapper[5] = lapper [5] + 1
        tilbake = tilbake - 10
    elif tilbake % 5 == 0:
        lapper[6] = lapper [6] + 1
        tilbake = tilbake - 5
    elif tilbake %1 == 0:
        lapper[7] = lapper [7] + 1
        tilbake = tilbake - 1
#hær printer vi ut resultatet ved hjelp av for loop. Den looper så mange ganger som lengden på arrayen.
#Den vill også sjekke om summen er 0 da printer den ikke ut noe fra den spesifike summen.
for i in range(len(lapper)):
    if lapper[i] > 0:
     print( lapper[i], seddler[i])

