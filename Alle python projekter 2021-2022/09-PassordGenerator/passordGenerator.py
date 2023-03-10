#inporter random biblioteket 
import random
#spør brukeren lengden på passordet
antall = int(input("Skriv inn antall siffer du vill ha i passordet ditt!: "))
#lag en array som passordet lagres i 
passord = []
#lag en for loop som looper antall ganger brukeren oppga
for i in range(1, antall):
    #append det tilfeldige generete passordet til arrayen "passord"
    passord.append(random.randint(0,9))
#Så putter vi sammen hele arrayen til en tallrekke
slutt = ''.join(map(str, passord))
#så printer vi ut resultatet av slutt
print(slutt)