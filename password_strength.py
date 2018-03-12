import re
import sys
from getpass import getpass


def get_blacklist_file(file_path):
    with open(file_path) as blacklist:
        return blacklist.read().split('\n')


def check_blacklist(blacklist, password):
    return password in blacklist


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


def check_not_phone_namber(password):
    if re.search(r'[7-8]\d{10}', password):
        return 0
    return 1


def check_not_date(password):
    if re.search(r'\d{1,2}[-.]\d{1,2}[-.]\d{2,4}', password):
        return 0
    return 1


def get_password_strength(password):
    if check_blacklist(blacklisted_words, password):
        return '0   "{}"-password from blacklist'.format(password)
    else:
        ball = sum([
            check_len_pass(password),
            check_low_and_upp(password),
            check_dig(password),
            check_special_char(password),
            check_not_phone_namber(password),
            check_not_date(password)
        ])
        return ball


if __name__ == '__main__':
    try:
        blacklisted_words = get_blacklist_file(sys.argv[1])
        password = getpass('Enter you password')
        print('password strength: {}'.format(get_password_strength(password)))
    except IndexError:
        exit('Not found blacklist')
