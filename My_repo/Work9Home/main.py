list_good_bye = ("good bye", "close", "exit")
phone_dict = dict()

def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "KeyError. This name is not in phone-book"
        except ValueError:
            return "ValueError. Phone number must be from digit"
        except TypeError:
            return "TypeError. Unknown command"
        except IndexError:
            return "IndexError. Give me name and phone please"
    return inner

@input_error    
def return_action(mode):
     
    if mode.lower() in list_good_bye:
        return good_bye
    elif mode.lower() == 'show all':
        return show_all
    
    id_command = mode.split()[0]
    return MODES[id_command.lower()]


def show_all(user_input):
     return phone_dict

@input_error
def add_phone(user_input):
    text = user_input.split()
    phone_dict[text[1]] = int(text[2])
    return f'Add {text[1]} - {text[2]}'

@input_error
def change_phone(user_input):
    text = user_input.split()
    elem = phone_dict[text[1]] 
    phone_dict[elem] = int(text[2])
    return f'Change {text[1]} - {text[2]}'

def hello(user_input):
    return "How can I help you?"

def good_bye(user_input):
    return "Good bye!"
    
@input_error
def phone(user_input):
    text = user_input.split()
    return f'Phone {text[1]} is {phone_dict[text[1]]}'

MODES = {
    'hello': hello,
    'add': add_phone,
    'change': change_phone,
    'phone': phone,
    'show_all': show_all,
    'exit': good_bye
    }


def get_function(command):
    return return_action(command)


def main():
    while True:
        user_input = input("Enter command: ")
        action = get_function(user_input)

        result = action(user_input)
        print(result)
        if action == good_bye:
            exit()
             

if __name__ == '__main__':
    main()