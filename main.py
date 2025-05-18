def add_numbers(a, b):
    return a + b

def div_numbers(a, b):
    return a / b

def safe_numbers():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        return num1, num2  # Возвращаем введённые числа
    except ValueError:
        print("Ошибка: введите числа!")

# Пример использования с вводом от пользователя
print("Сложение чисел:")
num1, num2 = safe_numbers()
result = add_numbers(num1, num2)
print(f"Результат сложения: {result}")

print("\nДеление чисел:")
num1, num2 = safe_numbers()
result = div_numbers(num1, num2)
print(f"Результат деления: {result}")