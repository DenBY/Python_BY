import random 

list = [i for i in range(1, 50)] # Здесь генерируем список значений, я выбрал от (1 до 49)
print(result := random.choices(list, k=6)) 

# Символ моржа ":=" дает возможность присвоить переменной  значения, включая переменные, которых еще не существует и возвращать это значение
# в переменной "k" задаем количество выводимых чисел 