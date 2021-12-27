revenue = int(input("Выручка: "))

costs = int(input("Издержки: "))

if revenue > costs:
    profitability = (revenue - costs) / revenue * 100
    staff = int(input("Количество сотрудников: "))
    staff_profitability = profitability / staff
    print("Выручка больше издержков. Рентабельность персонала", staff_profitability)
else:
    print("Издержки больше выручки")
