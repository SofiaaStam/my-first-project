month = int(input("Введите номер месяца (1-12)"))

if month == 12 or month <= 2:
    print("Это зима")
elif month <= 5:
    print("Это весна")
elif month <= 8:
    print("Это лето")
elif month <= 11:
    print("Это осень")
else:
    print("Вы дурачок!!!")
