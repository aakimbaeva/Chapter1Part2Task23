def define_year():
    year = int(input('Year: '))
    if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        return "Usual year"
    else:
        return "Leap year"
print(define_year())