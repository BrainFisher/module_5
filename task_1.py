def caching_fibonacci():
    # Створення порожнього словника для кешування
    cache = {}

    # Внутрішня функція fibonacci
    def fibonacci(n):
        # Базові випадки: 0-й елемент - 0, 1-й елемент - 1
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # Перевірка, чи результат вже збережений у кеші
        if n in cache:
            return cache[n]
        else:
            # Обчислення числа Фібоначчі за допомогою рекурсії
            result = fibonacci(n - 1) + fibonacci(n - 2)
            # Збереження результату у кеші
            cache[n] = result
            return result

    # Повернення внутрішньої функції fibonacci
    return fibonacci


# Отримання функції fibonacci з використанням замикання
fib = caching_fibonacci()

# Використання функції fibonacci для обчислення чисел Фібоначчі
print(fib(10))
print(fib(15))
