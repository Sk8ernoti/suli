import datetime, random, calendar

def f01(input_date, input_day):
    """adott dátumhoz napok hozzáadása"""
    t_date = input_date.split("-")
    t_day = int(t_date[1]) + int(input_day)
    temp_date = datetime.datetime(int(t_date[0]),int(t_date[1]),int(t_day))
    return temp_date

def f02(input_lower, input_higher):
    temp_random = random.randrange(int(input_lower),int(input_higher))
    return temp_random

def f03(input_year):
    t_month = random.randrange(1,12)
    return datetime.datetime(input_year,t_month,calendar.monthrange(input_year,t_month)[1])

def f04(input_list):
    return random.choice(input_list)

def f05(input_date1, input_date2):
    return input_date1-input_date2

def f06(input_count, input_min_range, input_max_range):
    temp_tuple = []
    for i in range(int(input_count)):
        temp_tuple.append(random.randrange(input_min_range,input_max_range))
    return temp_tuple

def f07(in_year, in_month, in_day):
    if in_year > 0 and in_year <= datetime.datetime.today().year:
        if in_month > 0 and in_month < 13:
            if in_day > 0 and in_day < calendar.monthrange(in_year,in_month)[1]:
                return True
    return False


def main():
    print(f01("2025-07-06",10))
    print(f02(1,100))
    print(f03(2025))
    print(f04(["Alice", "Bob", "Charlie", "Diana"]))
    print (f05(datetime.datetime(2025,3,5),datetime.datetime(2025,7,12)))
    print(f06(10,1,50))
    print (f07(2025,7,5))

    return 0

main()