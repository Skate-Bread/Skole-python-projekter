import random, string
lengde = int(input("Skriv inn ønsket lengde på passordet: "))
tegn = string.ascii_letters + string.digits + string.punctuation
passord = ""
for i in range(lengde):
    passord = passord + random.choice(tegn)
print("Dette er ditt tilfeldig generete passord: {}".format(passord))
