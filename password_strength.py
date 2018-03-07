import re
from getpass import getpass


def get_blacklist_file(file_path):
    if not os.path.exists(blacklist):
        return 0
    with open(file_path) as blacklist:
        return blacklist.read()


def check_blacklist(password):
    if password in blacklist:
        return -3
    return 0


def check_len_pass(password):
    if len(password) >= 12:
        return 2
    elif len(password) < 6:
        return 0
    return 1


def check_low_and_upp(password):
    if re.search('[A-ZА-Я]', password) and re.search('[a-zа-я]', password):
        return 2
    return 0


def check_dig(password):
    if re.search('\d+', password):
        return 2
    return 0


def check_special_char(password):
    if re.search('\W', password):
        return 2
    return 0


def check_repeat(password):
    if(max(password.count(symbol) for symbol in password)) < 3:
        return 2
    return 0


def get_password_strength(password):
    ball = sum([check_blacklist(password),
               check_len_pass(password),
               check_low_and_upp(password),
               check_dig(password),
               check_special_char(password),
               check_repeat(password)
               ])
    return ball


if __name__ == '__main__':
    try:
        blacklist = input("Enter filepath to the blacklist: \n")
        password = getpass('Enter you password')
        print('password complexity: {}'.format(get_password_strength(password)))
    except (ValueError, FileNotFoundError):
        exit('Not found password')

