positive_integer = abs(int(input("Введите целое положительное число ")))

max = positive_integer % 10

while positive_integer >= 1:
    positive_integer = positive_integer // 10
    if positive_integer % 10 > max:
        max = positive_integer % 10
    if positive_integer > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break
