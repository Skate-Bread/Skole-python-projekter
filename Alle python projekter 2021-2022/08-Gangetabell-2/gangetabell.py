#Lag en bruker input 
gangetabell = []
brukerTall = int(input("Skriv in tall for å generere en gangetabell (1-10): "))
#sjekk om bruker inputen er over 10 eller under 1. 
while brukerTall < 1 or brukerTall > 10:
 print("Det du har skrevet er ikke en gyldig verdi!")
 brukerTall = int(input("Skriv in tall for å generere en gangetabell (1-10): "))
#lag en for loop som looper 10 ganger. Appender hva bruker tall * syklusen for loopen er på.
for i in range(1, 11):
    gangetabell.append(brukerTall * i)
#lag input med navn slutt slik at hvis noen åpner den i en terminal så lukker den seg ikke automatisk
print("Dette er", brukerTall, "gangen")
for i in range(len(gangetabell)):
    print(gangetabell[i])
input("Slutt")
