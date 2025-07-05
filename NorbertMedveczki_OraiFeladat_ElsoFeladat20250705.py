"""I. Feladat
Adott a 'data' lista: data = [list comp.]
0.Csinálj egy ciklust, ami minden páros elemet megszoroz 3-al, minden páratlant 5-elszoroz és kettővel oszt, és minden 5. elemet hagyj ki, ami a listába nem kerül bele. Ha lehet list comprehension-el oldd meg ezt. A lista hossza legyen 42.
Használd az alábbi kódot ha list comp. nem menne!
import random
rand_list=[]
rand_list_length=42
for random_num in range(rand_list_length):
rand_list.append(random.randint(1,100))
print(rand_list)
0+1. List comprehension-el oldd meg a ciklusokat amennyiben ez lehetséges.
1.Tájékoztasd a felhasználót a program működéséről a mintának megfelelően!
2.Írasd ki a listát a konzolra a mintának megfelelően!
3.Kérj be a felhasználótól egy kétjegyű számot és azt szúrd be a lista másodikhelyére! A felhasználó jó számot ad meg, azt nem kell ellenőrizni.
4.Írd ki a módosított listát!
5.Kérd be a felhasználótól, hogy melyik elemet akarja törölni! A felhasználómeglévő elemet ad meg, azt nem kell ellenőrizni.
6.Töröld a kért elemet a listából és írd ki újra a listát!
7.Rendezd a listát és írd ki újra!
8.Fordítsd meg a lista elemeinek a sorrendjét és írd ki újra!
"""
import random

rand_list=[]
rand_list_length=42
for random_num in range(rand_list_length):
    rand_list.append(random.randint(1,100))

#0. 0.Csinálj egy ciklust, ami  minden páros elemet megszoroz 3-al,
#                               minden páratlant 5-elszoroz és kettővel oszt, és
#                               minden 5. elemet hagyj ki, ami a listába nem kerül bele.
#Ha lehet list comprehension-el oldd meg ezt. A lista hossza legyen 42.
def ParosElemMegszoroz3Al(input_list):
    temp_index = 0
    output_list = input_list.copy()
    for i in input_list:
        if output_list[temp_index] % 2 == 0:
            output_list[temp_index]= output_list[temp_index] * 3
            temp_index += 1
        #print(i)

    return output_list

def ParatlanElemMegszoroz5ElOszt2Vel(input_list):
    temp_index = 0
    output_list = input_list.copy()
    for i in input_list:
        if input_list[temp_index] % 2 == 1:
            #output_list.append(input_list[temp_index])
            output_list[temp_index] = output_list[temp_index] *5 // 2
        temp_index += 1
        #print(i)

    return output_list

def Minden5dikElemKihagy(input_list):
    temp_index = 0
    output_list = []
    for i in input_list:
        if input_list[temp_index] % 5 != 0:
            output_list.append(input_list[temp_index])
        temp_index += 1
        #print(i)

    return output_list


def FelhasznaloTajekoztat():
    print("A program egy meghatározott n elemű input listát dolgoz fel.")
    print("A ParosElemMegszoroz3Al függvény hívásával minden páros eleme szorozva lesz 3-al, majd az eredmény lista visszatér.")
    print("A ParatlanElemMegszoroz5ElOszt2Vel függvény hívásával minden páratlan eleme szorozva lesz 5-el és osztva 2-vel, majd az eredmény lista visszatér.")
    print("A Minden5dikElemKihagy függvény hívásával a beadott lista minden 5. eleme kivételével felveszi a többi elemet a kimeneti listára(amivel visszatér a függvény).")
    return ""











#------------------------------------------------------------------------#1.Tájékoztasd a felhasználót a program működéséről a mintának megfelelően!
print(FelhasznaloTajekoztat())
#------------------------------------------------------------------------#2.Írasd ki a listát a konzolra a mintának megfelelően!
print("eredeti lista: ",rand_list)
#1/1. feladat prezentál
print("eredmeny lista(1): ",ParosElemMegszoroz3Al(rand_list))
#1/2 feladat prezentál
print("eredmeny lista(2): ",ParatlanElemMegszoroz5ElOszt2Vel(rand_list))
#1/3 feladat prezentál
print("eredmeny lista(3): ",Minden5dikElemKihagy(rand_list))
#------------------------------------------------------------------------#3.Kérj be a felhasználótól egy kétjegyű számot és azt szúrd be a lista másodikhelyére! A felhasználó jó számot ad meg, azt nem kell ellenőrizni.
felh_input = int(input("Kérek egy kétjegyű számot:"))
tuzdelt_lista = []
if (felh_input>9 and felh_input <100):
    temp_index = 0
    for i in rand_list:
        if temp_index == 1:
            tuzdelt_lista.append(felh_input)
        tuzdelt_lista.append(rand_list[temp_index])
        temp_index += 1
#------------------------------------------------------------------------# 4.Írd ki a módosított listát!
print("A felhasználó által megadott érték beszúródik az új lista második indexére:\n", tuzdelt_lista)

#------------------------------------------------------------------------# 5.Kérd be a felhasználótól, hogy melyik elemet akarja törölni! A felhasználómeglévő elemet ad meg, azt nem kell ellenőrizni.
felh_input = int(input("Melyik elemet szeretnéd törölni:"))
tuzdelt_listabol_torolt = []
temp_index = 0
for i in tuzdelt_lista:
    if felh_input != tuzdelt_lista[temp_index]:
        tuzdelt_listabol_torolt.append(i)
    #tuzdelt_lista.append(rand_list[temp_index])
    temp_index += 1

#------------------------------------------------------------------------#6.Töröld a kért elemet a listából és írd ki újra a listát!
print("A következő elem törölve a listából:", felh_input, ", frissített lista:",tuzdelt_listabol_torolt)

#------------------------------------------------------------------------#7.Rendezd a listát és írd ki újra!
tuzdelt_listabol_torolt.sort(reverse=False)
print("Rendezett lista:    ", tuzdelt_listabol_torolt)
#------------------------------------------------------------------------#8.Fordítsd meg a lista elemeinek a sorrendjét és írd ki újra!
tuzdelt_listabol_torolt.reverse()
print("Megfordított lista: ", tuzdelt_listabol_torolt)
