def add_numbers(a, b):
    return a + b

def safe_add_numbers():
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        result = add_numbers(num1, num2)
        print(f"Результат сложения: {result}")
    except ValueError:
        print("Ошибка: введите числа!")

# Пример использования
num1 = 5
num2 = 3
result = add_numbers(num1, num2)
print(f"Результат сложения: {result}")