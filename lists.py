chisla = [3, 5, 7, 9, 10.5]
print(chisla)

chisla = [3, 5, 7, 9, 10.5, "Python"]
print('Добавьте в конец списка строку "Python" - ', chisla)
print('Выведите длину списка на экран - ', len(chisla))

print('Выведите на экран начальный элемент списка - ', chisla[0])
print('Выведите на экран последний элемент списка - ', chisla[-1])
print('Напечатайте элементы списка со второго по четвертый включительно - ', chisla[1:4])
print('Удалите из списка строку "Python"')
chisla.remove("Python")
print(chisla)