"""
I. Feladat
Adott két lista:
fogalmak = ['majorság', 'hűbéres', 'jobbágy', 'nemes', 'tized', 'kilenced', 'robot', 'szügyhám', 'vetésforgó', 'ugar', 'lovag']
meghatarozasok = ['Egy-egy nagybirtok vagy valamely részének igazgatási központja.', 'Aki örökletes használatra megkapja a földet.', 'Telkes paraszt, aki a földesúrtól kapott földön gazdálkodik.', 'Kiváltságos réteg.', 'Egyházi adó.', 'Földesúrnak beszolgáltatott adó.', 'Ötvenkét igás, vagy 104 kézimunka nap kötelezettség.', 'Igavonási találmány, melynek köszönhetően nem az állat nyakában van a húzó eszköz.', 'A termőföld használata évszakonként más és más.', 'Művelés alá nem vont terület.', 'Vagyonos katonai szolgálattevő lóval, páncéllal.']
A két lista indexei megfelelnek egymásnak: az egyik listában szereplő fogalmakhoz a másik listában ugyanazon indexű meghatározások tartoznak, így mindegyik fogalomhoz a megfelelő párosítás található.
fogalmak[0] -> meghatarozasok[0]
fogalmak[1] -> meghatarozasok[1]
…
fogalmak[n] -> meghatarozasok[n]
1. Dictionary comprehension-el oldd meg, hogy a fogalmak lista elemei legyen a dict. kulcsa és a meghatarozasok lista elemei pedig az érték.
2. Kiindulásnak használd a fenti listát amely tartalmazza a fogalmak és meghatározások listáját.
3. Véletlenszerűen válassz ki egy meghatározást, azt írd ki.
4. Kérdezz rá a felhasználótól, hogy a meghatározáshoz milyen fogalom társul.
5. Ha eltalálta a fogalmat, akkor írd ki, hogy "Helyes válasz!". Ha nem találta el, akkor írd ki, hogy "Rossz válasz. Helyesen: " és ide írd ki a helyes választ.
6. A válasz ellenőrzésekor a kis-nagybetű eltérések és a kezdő-záró szóközök ne számítsanak. Azaz akkor is tekintsük helyesnek a választ, ha azt a felhasználó nagybetűkkel írta és az elejére, végére gépelt több szóközt is.
7. Addig ismételd a kikérdezést, ameddig mindegyik fogalomra rá nem kérdeztél. Mindegyikre csak egyszer kérdezz rá.
8. A program kommunikációját a mintának megfelelően szövegezd!
+ A program a fogalom bekérésre ha END, Q, vagy QUIT (ne legyen érzékeny a betűre, lehet kilépés az EnD és qUiT is) válasz érkezik akkor a program írja ki, hány helyes és hány helytelen választ adott, százalékosan is tegye ezt meg.
"""
import random

"""1-2. feladat"""
fogalmak = ['majorság', 'hűbéres', 'jobbágy', 'nemes', 'tized', 'kilenced', 'robot', 'szügyhám', 'vetésforgó', 'ugar', 'lovag']
meghatarozasok = ['Egy-egy nagybirtok vagy valamely részének igazgatási központja.', 'Aki örökletes használatra megkapja a földet.', 'Telkes paraszt, aki a földesúrtól kapott földön gazdálkodik.', 'Kiváltságos réteg.', 'Egyházi adó.', 'Földesúrnak beszolgáltatott adó.', 'Ötvenkét igás, vagy 104 kézimunka nap kötelezettség.', 'Igavonási találmány, melynek köszönhetően nem az állat nyakában van a húzó eszköz.', 'A termőföld használata évszakonként más és más.', 'Művelés alá nem vont terület.', 'Vagyonos katonai szolgálattevő lóval, páncéllal.']
custom_dictionary = dict(zip(fogalmak, meghatarozasok))

def main():
    print ("Középkori történelem fogalmakat kérdezünk ki.\nMilyen fogalmat ír le az alábbi meghatározés?\n")
    user_choice_counter = 0

    while user_choice_counter < len(meghatarozasok):
        chosen_description = random.choice(list(custom_dictionary.values()))
        #print("(",len(meghatarozasok)-user_choice_counter,") véletlenszerűen kiválasztott meghatározás: ", chosen_description)
        print(chosen_description)
        user_choice = input("Írd be, hogy ez szerinted melyik fogalom magyarázata:")
        if user_choice.lower() == "q" or user_choice.lower() == "quit" or user_choice.lower() == "end":
            break

        if(chosen_description in custom_dictionary.values()):
            for x,y in custom_dictionary.items():
                if y.lower().strip() == chosen_description.lower().strip() and x.lower().strip() == user_choice.lower().strip():
                    print ("Helyes válasz!\n")
                    user_choice_counter += 1
                    custom_dictionary.pop(x)
                    break
                elif x.lower().strip() != user_choice.lower().strip() and y.lower().strip() == chosen_description.lower().strip():
                    print ("Rossz válasz! Az általad megadott: ", user_choice, ", de a megoldás: ", x, "\n")

    return 0

main()