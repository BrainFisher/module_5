def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."

    return inner


def parse_input(user_input):
    if not user_input:
        return "", []  # Повертаємо порожній рядок і порожній список аргументів
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


@input_error
def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        print("\nPlease choose an option:")
        print("1. Add a contact")
        print("2. Change a contact")
        print("3. Show phone number")
        print("4. Show all contacts")
        print("5. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            print(add_contact([name, phone], contacts))
        elif choice == "2":
            name = input("Enter the name: ")
            phone = input("Enter the new phone number: ")
            print(change_contact([name, phone], contacts))
        elif choice == "3":
            name = input("Enter the name: ")
            print(show_phone([name], contacts))
        elif choice == "4":
            show_all(contacts)
        elif choice == "5":
            print("Good bye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
