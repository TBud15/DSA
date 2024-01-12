# Создание хеш-карты с некоторыми начальными парами ключ-значение
my_dict = {
    'name': 'Алексей',  # 'name' - ключ, 'Алексей' - значение
    'age': 30,          # 'age' - ключ, 30 - значение
    'city': 'Киев'      # 'city' - ключ, 'Киев' - значение
}

# В этом словаре три пары ключ-значение. Ключи уникальны и используются для доступа к значениям.

# Добавление новой пары ключ-значение
my_dict['job'] = 'Программист'  
# 'job' - новый ключ, 'Программист' - соответствующее значение. Эта строка добавляет новую пару в словарь.

# Получение значения по ключу
print("Имя:", my_dict['name'])  
# Доступ к значению по ключу 'name'. Выведет 'Имя: Алексей'. Если ключ не найден, Python выдаст KeyError.

# Обновление существующего значения
my_dict['age'] = 31  
# Обновление значения для ключа 'age'. Теперь, если вы обратитесь к my_dict['age'], получите 31.

# Удаление пары ключ-значение
del my_dict['city']  
# Удаление пары с ключом 'city'. Теперь в словаре не будет ключа 'city' и соответствующего значения 'Киев'.

# Проверка наличия ключа
if 'age' in my_dict:
    print("Возраст:", my_dict['age'])  
    # Выведет 'Возраст: 31'. Этот блок проверяет, есть ли 'age' в словаре, и если да, выводит его значение.

# Итерация по ключам и значениям
for key, value in my_dict.items():
    print(f"{key} -> {value}")
# Метод items() возвращает пары ключ-значение в словаре. 
# Цикл for проходит по этим парам, и вы можете использовать их в своем коде.