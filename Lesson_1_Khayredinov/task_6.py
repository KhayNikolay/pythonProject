distance = int(input("Дистанция первой пробежки: "))

purpose = int(input("Цель: "))

day = 1

print(day, "день:", distance)

while distance < purpose:
    distance *= 1.1
    day += 1
    print(day, "день:", distance)
else:
    print("На", day, "день цель достигнута")
