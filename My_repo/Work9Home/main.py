list_good_bye = ("good bye", "close", "exit")
phone_dict = dict()

def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "KeyError"
        except ValueError:
            return "ValueError"
        except TypeError:
            return "IndexError"
        except TypeError:
            return "IndexError"
    return inner

    #"Enter user name", 
    #"Give me name and phone please" 
    
    #обробляти винятки, що виникають у функціях-handler (KeyError, ValueError, IndexError) та повертати відповідну відповідь користувачеві.


def return_action(mode):
     
    if mode.lower() in list_good_bye:
        return good_bye
    elif mode.lower() == 'show all':
        return show_all
    
    id_command = mode.split()[0]
    return MODES[id_command.lower()]

def show_all(user_input):
     return phone_dict

def add_phone(user_input):
    text = user_input.split()
    phone_dict[text[1]] = text[2]
    return f'Add {text[1]} - {text[2]}'

def change_phone(user_input):
    text = user_input.split()
    phone_dict[text[1]] = text[2]
    return f'Change {text[1]} - {text[2]}'

def hello(user_input):
    return "How can I help you?"

def good_bye(user_input):
    return "Good bye!"
    

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

@input_error
def get_function(command):
    return return_action(command)


def main():
    while True:
        user_input = input("Enter command: ")
        action = get_function(user_input)
        print(action(user_input))
        if action == good_bye:
            exit()
             

if __name__ == '__main__':
    main()