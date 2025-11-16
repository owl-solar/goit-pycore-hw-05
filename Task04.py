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

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"Error: Contact '{name}' already exists."
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    contacts[name] = new_phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


def show_all(contacts):
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

   
def parse_input(user_input):
    parts = user_input.split(maxsplit=1)
    if not parts:
        return "", []

    cmd = parts[0].strip().lower()
    args = parts[1].split() if len(parts) > 1 else []
    return cmd, args


def main():
    contacts = {}                                         
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break                                           
        elif command == "hello":
            print("How can I help you?")                    
        elif command == "add":
            print(add_contact(args, contacts))            
        elif command == "change":
            print(change_contact(args, contacts))          
        elif command == "phone":
            print(show_phone(args, contacts))               
        elif command == "all":
            print(show_all(contacts))                       
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()                                                  
