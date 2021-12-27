time_sec = int(input("Введите время в секундах: "))

hour_value = time_sec // 3600
minutes_value = (time_sec - hour_value * 3600) // 60
seconds_value = time_sec - (hour_value * 3600 + minutes_value * 60)
print(f"{hour_value} : {minutes_value} : {seconds_value}")
