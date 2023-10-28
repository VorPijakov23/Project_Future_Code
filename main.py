# Импортируем необходимые модули
import random
import string
from colorama import Fore  # Модуль для окрашивания вывода в консоль
#  Например, вывода ошибок красного цвета или паролей зелёного цвета


def generate_letters_password(length, quantity):
    """Функция для генерации паролей вида "Только буквы разного регистра\""""
    answer = []
    for i in range(quantity):
        letters = string.ascii_letters  # Вписываем необходимые символы для генерации пароля
        result = ''.join(random.choice(letters) for _ in range(length))  # Генерируем символ
        answer.append(result)  # Добавляем в список сгенерированный символ
    return answer


def generate_alphanumeric_password(length, quantity):
    """Функция для генерации паролей вида "Буквы разного регистра и цифры\""""
    answer = []
    for i in range(quantity):
        letters = string.ascii_letters + string.digits  # Вписываем необходимые символы для генерации пароля
        result = ''.join(random.choice(letters) for _ in range(length))  # Генерируем символ
        answer.append(result)  # Добавляем в список сгенерированный символ
    return answer


def generate_complex_password(length, quantity):
    """Функция для генерации паролей вида "Буквы, цифры и спецсимволы\""""
    answer = []
    for i in range(quantity):
        letters = string.ascii_letters + string.digits + string.punctuation  # Вписываем необходимые символы для
        # генерации пароля
        result = ''.join(random.choice(letters) for _ in range(length))  # Генерируем символ
        answer.append(result)  # Добавляем в список сгенерированный символ
    return answer


def router_password_generate(length, pass_type, quantity):
    """Функция определяющая какой тип пароля выбрал пользователь"""
    if pass_type == "1":  # Тип "Только буквы разного регистра"
        return generate_letters_password(length, quantity)
    elif pass_type == "2":  # Тип "Буквы разного регистра и цифры"
        return generate_alphanumeric_password(length, quantity)
    elif pass_type == "3":  # Тип "Буквы, цифры и спецсимволы"
        return generate_complex_password(length, quantity)
    else:  # Вывод ошибки
        return Fore.RED + 'Произошла ошибка!'


def main():
    """Главная функция выполняющая роль соединителя кода в одно целое"""
    try:  # Если код работает без ошибок, то код переходит в блок "try"
        print("Добро пожаловать в Генератор Сложных Паролей!")
        print("У нас есть несколько типов паролей, которые мы можем создать:")
        possible_commands = {  # Словарь необходимый для вывода возможных команд
            "1": "Только буквы разного регистра",
            "2": "Буквы разного регистра и цифры",
            "3": "Буквы, цифры и спецсимволы"
        }
        for key, value in possible_commands.items():
            print(f'{key}: {value}')  # Вывод словаря с командами

        user_choice = input('Введите тип пароля (1-3): ')  # Ввод типа пароля
        if user_choice in possible_commands:  # Проверка на корректность ввода
            long = int(input("Введите длину пароля (от 4 до 30 символов): "))  # Ввод длины пароля
            quantity = int(input("Введите количество генераций паролей (не больше 40): "))  # Ввод количества
            # генерация пароля

            if 4 <= long <= 30 and 1 <= quantity <= 40:  # Проверка на корректность ввода
                password = router_password_generate(long, user_choice, quantity)
                print("Сгенерированные пароли:")
                for i in password:
                    print(Fore.GREEN + i)  # Вывод сгенерированный паролей
            else:  # Выбор типа ошибки
                if not 4 <= long <= 30:
                    print(Fore.RED + "Длина не подходит под нужные параметры!")
                if not 1 <= quantity <= 40:
                    print(Fore.RED + "Количество генераций задано неправильно!")
        else:  # Вывод ошибки
            print(Fore.RED + 'Такой команды нет в списке!')
    except KeyboardInterrupt:
        """Блок "except" запускается когда пользователь досрочно закрывает программу. Тип ошибки KeyboardInterrupt"""
        print(Fore.RED + 'Преждевременный выход из программы')  # Вывод сообщения заменяющего ошибку досрочного
        # закрытия программы


if __name__ == '__main__':  # Этот блок кода выполняет функцию точки входа в программу
    """Конструкция "if name == 'main':" используется, чтобы определить, выполняется ли файл напрямую как основной 
    скрипт, или же он импортируется как модуль, и в зависимости от этого выполнить соответствующий код или действия."""
    main()  # Запускаем главную функцию "main"
