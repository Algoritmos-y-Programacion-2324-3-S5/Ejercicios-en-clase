day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))
month_label = ""
isValid = True

if month == 1:
    isValid = day <= 31
    month_label = "enero"
elif month == 2:
    isValid = day <= 28
    month_label = "febrero"
elif month == 3:
    isValid = day <= 31
    month_label = "marzo"
elif month == 4:
    isValid = day <= 30
    month_label = "abril"
elif month == 5:
    isValid = day <= 31
    month_label = "mayo"
elif month == 6:
    isValid = day <= 30
    month_label = "junio"
elif month == 7:
    isValid = day <= 31
    month_label = "julio"
elif month == 8:
    isValid = day <= 31
    month_label = "agosto"
elif month == 9:
    isValid = day <= 30
    month_label = "septiembre"
elif month == 10:
    isValid = day <= 31
    month_label = "octubre"
elif month == 11:
    isValid = day <= 30
    month_label = "noviembre"
elif month == 12:
    isValid = day <= 31
    month_label = "diciembre"
else:
    isValid = False

if year < 1950 or year > 2024:
    isValid = False

if isValid:
    print(f"{day} de {month_label} de {year}")
else:
    print("Invalid date")