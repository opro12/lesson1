from pprint import pprint

#product = {
#    "name": "iPhone 12",
#    "stock": 24,
#    "price": 65432.1
#}
#pprint(product)
#chisla = [3, 5, 7, 9, 10.5, "Python"]
#product["recomended"] = chisla
#pprint(product)

#stock = [
#    {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1, 
#       'recomended': ['Samsung Galaxy S21', 'iPhone 12']},
#    {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0, 'discount': 5000},
#    {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}
#]

#print(type(stock[1]))

##########Задание_1
#Создайте словарь:
my_dict = {
    "city": "Москва", 
    "temperature": "20"
}
#Выведите на экран значение ключа city
print('Выведите на экран значение ключа city -', my_dict["city"])

#Уменьшите значение "temperature" на 5
print('Уменьшите значение "temperature" на 5 =', int(my_dict['temperature']) - 5)

#Выведите на экран весь словарь
print('Выведите на экран весь словарь -', my_dict)

########Задание_2
#Проверьте, есть ли в словаре ключ country
print('Проверьте, есть ли в словаре ключ country -', my_dict.get('country'))

#Выведите значение по-умолчанию "Россия" для ключа country
print('Выведите значение по-умолчанию "Россия" для ключа country -', my_dict.get('country','Россия'))

#Добавьте в словарь элемент date со значением "27.05.2019"
my_dict["date"] = "27.05.2019"
print('Добавьте в словарь элемент date со значением "27.05.2019" -', my_dict)

#Выведите на экран длину словаря
print('Выведите на экран длину словаря -', len(my_dict))