
# Функція для обчислення чисел Фібоначчі з кешуванням
def caching_fibonacci(): 
    cache={} # Словник для збереження обчислених значень

    def fibonacci(n): # Внутрішня рекурсивна функція
        if n <= 0: # Базовий випадок
            return 0 
        elif n == 1: # Базовий випадок
            return 1
        
        if n in cache: # Перевірка наявності в кеші
            return cache[n]
        
        cache[n]= fibonacci(n - 1) + fibonacci(n - 2) # Збереження в кеш
        return cache[n]

    return fibonacci # Повернення внутрішньої функції


# Створення екземпляру функції з кешуванням
fib = caching_fibonacci() 

# Використання функції fibonacci для обчислення чисел Фібоначчі
print(fib(10)) # 55
print(fib(15)) # 610