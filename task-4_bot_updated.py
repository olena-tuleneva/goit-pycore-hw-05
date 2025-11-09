
def input_error(func): # Декоратор для обробки помилок введення
    def inner(*args, **kwargs): # Внутрішня функція-обгортка
        try: # Виклик оригінальної функції
            return func(*args, **kwargs) # Повернення результату
        except ValueError: # Обробка помилок
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
    return inner # Повернення внутрішньої функції


def parse_input(user_input): # Функція для розділення введеного користувачем рядка на команду і аргументи
    cmd, *args = user_input.split() # Поділ рядка на команду і аргументи
    cmd = cmd.strip().lower() # Нормалізація команди
    return cmd, *args # Повернення команди і аргументів


@input_error
def add_username_phone(args, contacts): # Функція для додавання контакту
    name, phone = args # Розпаковка аргументів
    contacts[name] = phone # Додавання контакту до словника
    return f"Contact '{name}' added."


@input_error
def change_username_phone(args, contacts): # Функція для зміни номера телефону контакту
    name, phone = args # Розпаковка аргументів
    if name not in contacts: # Перевірка наявності контакту
        raise KeyError
    contacts[name] = phone # Зміна номера телефону
    return f"Phone number for '{name}' updated."
    

@input_error
def phone_username(args, contacts): # Функція для отримання номера телефону за іменем контакту
    name = args[0] # Розпаковка аргументу
    if name not in contacts: # Перевірка наявності контакту
        raise KeyError
    return f"{name}: {contacts[name]}"
    

@input_error
def show_all(contacts): # Функція для відображення всіх контактів
    if not contacts: # Перевірка наявності контактів
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items()) # Форматування і повернення списку контактів


def main():
    contacts = {} # Ініціалізація словника контактів
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ") # Запит команди у користувача
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break # Вихід з програми при командах "close" та "exit"
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_username_phone(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()