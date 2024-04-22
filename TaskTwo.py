a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
max = a if a > b else b
max = max if max > c else c
print ("Максимальное число:", max)
