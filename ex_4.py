# Дан список чисел, необходимо удалить все вхождения числа 20 из него.

list1 = [5, 20, 15, 20, 25, 50, 20]
def removeValue(sampleList, val):
   return [value for value in sampleList if value != val]
resList = removeValue(list1, 20)
print(resList)
