ticket = int(input("Сколько билетов Вы хотите приобрести? "))
customers = []
for i in range(ticket):
    age = int(input(f"Введите возраст {i+1}го посетителя: "))
    customers.append(age)
price = 0
for age in customers:
    if age < 18:
        price += 0
    elif age < 25:
        price += 990
    else:
        price += 1390
if ticket > 3:
    price = 0.9 * price
print("Стоимость покупки:", price)
