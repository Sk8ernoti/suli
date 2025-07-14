import random, datetime, statistics, math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def MaiDatum():
    temp_date = datetime.date.today()
    temp_cutted = str(temp_date)
    return temp_cutted.split("-")

def SzamotGeneral():
    temp_tuple = []

    for i in range(10):
        temp_tuple.append(random.randint(1,100))

    return temp_tuple

def NapiSzerencseSzam(inputNumberOfDay):
    return random.choice(inputNumberOfDay)

def NapiSzerencseEsStatisztikaGenerator():
    napok = []


    for i in range(365):
        napok.append(SzamotGeneral())

    #print(napok[3],"\n", napok[333])

    print("Mai dátum: ", MaiDatum())
    date_tuple = MaiDatum()
    date_obj = datetime.date(int(date_tuple[0]), int(date_tuple[1]), int(date_tuple[2]))
    day_in_year = int(date_obj.strftime("%j"))
    print("Mai nap az évben: ", day_in_year)
    print("Mai nap neve: ", date_obj.strftime("%a"))
    szerencseszam = NapiSzerencseSzam(napok[day_in_year])
    print("Mai nap szerencseszáma: ", szerencseszam)
    if(is_prime(szerencseszam)):
        print("a szerencseszám prim!")

    print ("mai naphoz adott számok átlaga: ", statistics.mean(napok[day_in_year]),", maximuma:", max(napok[day_in_year]),", minimuma:",min(napok[day_in_year]) ,",összegének gyöke: ", math.sqrt(sum(napok[day_in_year])))

    return 0

def MasodikFeladat():
    #temp_bitrinput("Kérem a születési dátumodat: (yyyy-mm-dd)")

    pass

def HarmadikFeladat():
    pass

def main():

    NapiSzerencseEsStatisztikaGenerator()
    MasodikFeladat()

    return 0

main()
