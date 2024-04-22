s = input("Введите слово: ")
glas = 0
soglas = 0
bykv1 = set("уеыаоэяию")
bykv2 = set("цкнгшщзхфвпрлджчсмтбй")
for str in s:
    if str in bykv1:
        glas += 1
    if str in bykv2:
        soglas += 1
print("Количество гласных равно: ", glas)
print("Количество согласных равно: ", soglas)
