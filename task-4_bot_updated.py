import re
from typing import Callable, Generator

def input_error(func):
    """
    Декоратор для обробки типових помилок введення користувача:
    ValueError (неправильна кількість аргументів), 
    KeyError (контакт не знайдено), 
    IndexError (відсутній аргумент).
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            # Обробляє помилки розпакування аргументів (неправильна кількість)
            return "Give me name and phone, please."
        except KeyError:
            # Обробляє, коли ключ (ім'я) не знайдено у словнику контактів
            return "Contact not found."
        except IndexError:
            # Обробляє, коли для команд, як-от 'phone', не надано жодного аргументу
            return "Enter user name."
    return inner

def parse_input(user_input):
    """
    Розділяє введений користувачем рядок на команду і аргументи.
    Повертає команду у нижньому регістрі та список аргументів.
    """
    user_input = user_input.strip()
    if not user_input:
        return "", []
    cmd, *args = user_input.split()
    return cmd.lower(), args

@input_error
def add_contact(args, contacts):
    """Додає новий контакт до словника."""
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added."

@input_error
def change_phone(args, contacts):
    """Змінює номер телефону існуючого контакту. Викликає KeyError, якщо контакт не існує."""
    name, phone = args
    
    # Викликає KeyError, якщо контакт відсутній, який буде оброблений декоратором
    _ = contacts[name] 
    
    contacts[name] = phone
    return f"Phone number for '{name}' updated."

@input_error
def get_phone(args, contacts):
    """Повертає номер телефону за іменем контакту. Викликає KeyError, якщо контакт не існує."""
    name = args[0]
    # Викликає KeyError, якщо ім'я не знайдено
    return f"{name}: {contacts[name]}"

@input_error
def show_all_contacts(contacts):
    """Відображає всі контакти у відформатованому вигляді."""
    if not contacts:
        return "Contacts not found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    """Головна функція, що реалізує логіку бота-помічника."""
    contacts = {}
    print("Welcome to the assistant bot! Type 'hello' for assistance.")

    # Використання лямбда-функцій-обгорток для уніфікації виклику
    commands = {
        # Всі функції у словнику приймають (args, contacts)
        "hello": lambda args, contacts: "How can I help you?",
        "add": add_contact,
        "change": change_phone,
        "phone": get_phone,
        # Обгортка, щоб show_all_contacts отримувала лише словник контактів
        "all": lambda args, contacts: show_all_contacts(contacts),
    }

    while True:
        user_input = input("Enter a command:")
        command, args = parse_input(user_input)

        if not command:
            print("Please enter a command.")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command in commands:
            func = commands[command]
            # Уніфікований виклик: всі функції/лямбди приймають (args, contacts)
            print(func(args, contacts))
        else:
            print("Invalid command. Available commands: hello, add, change, phone, all, close, exit.")

if __name__ == "__main__":
    main()