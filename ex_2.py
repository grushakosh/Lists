# Необходимо удалить пустые строки из списка строк.

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
resList = list(filter(None, list1))
print(resList)
