def is_year_leap(year):
    if year % 4 == 0:
        return 'False'
    else:
        return 'True'


year = int(input('Введите год: '))
result = is_year_leap(year)
print(f"год {year}: {result}")
