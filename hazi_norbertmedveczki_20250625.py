#Medveczki Norbert házi feladat

"""
20250625
1. Magánhangzó-számláló
Kérj be egy szöveget, és számold meg, hány magánhangzót tartalmaz! (A, E, I, O, Ö, U, Ü + kisbetűk is)
Példa: Bemenet: Hello Világ Kimenet: 4 magánhangzó található.
"""
from re import split

#-------------------function 1----------------------------------------
def MaganhangzoSzamlalo(DropInString,StringOfChosenCharacters):
    SumOfChosenCharacters = 0

    i = -1
    while i < (len(DropInString) - 1):
        i += 1
        j = -1
        while j < (len(StringOfChosenCharacters) - 1):
            j += 1
            #print(i, j) #körök ellenőrzése
            if StringOfChosenCharacters[j] == DropInString[i]:
                #print (StringOfChosenCharacters[j], DropInString[i]) #összehasonlított karakterek ellenőrzése
                SumOfChosenCharacters += 1
                break
    return SumOfChosenCharacters;


#-------------------end function 1-----------------------------------------
"""
2. Számjegyek összege
Kérj be egy egész számot, majd számold össze a számjegyeit! Pl. 753 → 7 + 5 + 3 = 15
Tipp: alakítsd át stringgé, menj végig rajta, és alakítsd vissza az egyes karaktereket int()-tel.
"""
#-------------------function 2----------------------------------------
def SzamjegyekOsszege(InputNumberForProcessing):
    InputAsString = str(InputNumberForProcessing)
    SumOfValues = 0
    print(InputAsString, "=")
    IndexHelper = 0
    for i in InputAsString:
        IndexHelper += 1
        SumOfValues += int(i)
        print(i)
        if IndexHelper < len(InputAsString): print ("+")
        else: print ("->")
    return SumOfValues
#-------------------end function 2-----------------------------------------
"""
20250626
3. Szavak visszafelé
Kérj be egy mondatot, és írd ki a szavait visszafelé sorrendben, de a szavak betűit ne fordítsd meg!
Példa: Bemenet: Szeretem a Python nyelvet Kimenet: nyelvet Python a Szeretem
Tipp: split(), majd reversed() vagy [::-1]
"""
#-------------------function 3-----------------------------------------
def SzavakVisszafele():
    ReversedString = ""

    InputString = input("Kérek egy mondatot: ")
    WordsListFromInput = InputString.split()
    ReversedWordsTuple = WordsListFromInput[::-1]

    for i in range(len(ReversedWordsTuple)):
        ReversedString += ReversedWordsTuple[i] + " "

    return ReversedString
#-------------------end function 3-----------------------------------------
"""
4. Leggyakoribb szám
Kérj be számokat egy listába (Enterrel lezárható), majd írd ki, melyik szám szerepelt a legtöbbször, és hányszor!
Tipp: Olyan, mint a feladatok_pontok(), de itt a leggyakoribb értéket keresed.
"""
#-------------------function 4-----------------------------------------
def LeggyakoribbSzam():
    TempInput = input("Kérek egy számot: ")
    TempContainer = []                      #ez lesz a bekért számok halmaza
    DistinctTempContainer = []              #ez lesz az egyedi bekért számok halmaza
    TempContainerCount = []                 #az indexedik lesz a számossága az indexedik egyedinek

    if TempInput == "": return ""                                   #ha nem volt bevitel, akkor visszatér

    while TempInput != "" and TempInput.isnumeric():                #bekérjük a halmazt
        if TempInput != "": TempContainer.append(int(TempInput))
        TempInput = input("Kérek egy számot: ")

    DistinctTempContainer.append(TempContainer[0])                  #első elem felvétele
    for i in range(len(TempContainer)):                             #egyedi számok bejegyzése
         FoundItemCount = 0
         for j in range(len(DistinctTempContainer)):
            if DistinctTempContainer[j] == TempContainer[i]:
                FoundItemCount += 1
         if FoundItemCount == 0:
            DistinctTempContainer.append(TempContainer[i])

    DistinctTempContainer.sort()                                    #egyedi számok sorrendben

    for i in range(len(DistinctTempContainer)):                     #megszámoljuk a tételeket a halmazból
        TempContainerCount.append(0)
        for j in range(len(TempContainer)):
            if DistinctTempContainer[i] == TempContainer[j]: TempContainerCount[i] += 1

    MaxValue = 0
    MaxIndex = 0
    for i in range(len(DistinctTempContainer)):                     #kiírjuk egymás mellett az összetartozókat
        if TempContainerCount[i] > MaxValue:
            MaxValue = TempContainerCount[i]                        #megjegyezzük a legnagyobbat
            MaxIndex = i                                            #és hozzá az indexet
        print(DistinctTempContainer[i], ":", TempContainerCount[i])

    print("A legnagyobb számosság a következő számban:",DistinctTempContainer[MaxIndex],": ",MaxValue)

#-------------------end function 4-----------------------------------------
"""
5. Egyszerű jelszó-ellenőrző
Írj egy függvényt, ami bekér egy jelszót, és eldönti, hogy elég erős-e! A jelszó akkor erős, ha:
 Legalább 8 karakter hosszú
 Tartalmaz számot
 Tartalmaz nagybetűt
 Tartalmaz kisbetűt
Tipp: használhatsz any(c.isdigit() for c in jelszo) jellegű megoldást.
"""
#-------------------function 5-----------------------------------------
def JelszoEllenorzo():
    ResultValue = 0
    Resultstring = ""
    InputPassAsString = input("Add meg a jelszót:")
    if len(InputPassAsString) < 8: Resultstring += "Jelszó nem elég hosszú.\n"
    if MaganhangzoSzamlalo(InputPassAsString, "1234567890") < 1: Resultstring += "Jelszó nem tartalmaz számot.\n"
    if MaganhangzoSzamlalo(InputPassAsString,"AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ") < 1: Resultstring += "Jelszó nem tartalmaz nagybetűt.\n"
    if MaganhangzoSzamlalo(InputPassAsString,"aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz") < 1: Resultstring += "Jelszó nem tartalmaz kisbetűt.\n"
    if Resultstring == "": print("Jelszó megfelelően választott.")

    return Resultstring


#-------------------end function 5-----------------------------------------

#-------------present function 1----------------------------------------------------------------------------------------
    FilterCharacters = "AÁEÉIÍOÓÖŐUÚÜŰaáeéiíoóöőuúüű"
    InputStringForSearch = "Hello Világ"
    print ("Bemenet: ",f'{InputStringForSearch}',"Kimenet:", MaganhangzoSzamlalo(InputStringForSearch,FilterCharacters), "magánhangzó található.") #show result_1
#-------------present function 2----------------------------------------------------------------------------------------
    InputParameter = 753
    print (SzamjegyekOsszege(InputParameter))
#-------------present function 3----------------------------------------------------------------------------------------
    print(SzavakVisszafele())
#-------------present function 4----------------------------------------------------------------------------------------
    LeggyakoribbSzam()
#-------------present function 5----------------------------------------------------------------------------------------
    print(JelszoEllenorzo())