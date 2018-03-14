import re
import sys
from getpass import getpass


def get_blacklist_data(file_path):
    with open(file_path) as blacklist:
        return blacklist.read().split('\n')


def is_in_blacklist(blacklisted_words, password):
    return password in blacklisted_words


def check_len_pass(password):
    min_len_pass = 6
    max_len_pass = 12
    if len(password) >= max_len_pass:
        return 2
    elif len(password) < min_len_pass:
        return 0
    return 1


def has_lower_and_upper(password):
    return 2*bool(re.search('[A-ZА-Я]', password) and
                  re.search('[a-zа-я]', password))


def has_digits(password):
    return 2*bool(re.search('\d+', password))


def has_special_char(password):
    return 2*bool(re.search('\W', password))


def has_not_phone_namber(password):
    return not bool(re.search(r'[7-8]\d{10}', password))


def has_not_date(password):
    return not bool(re.search(r'\d{1,2}[-.]\d{1,2}[-.]\d{2,4}', password))


def get_password_strength(password):
    score = sum([
        check_len_pass(password),
        has_lower_and_upper(password),
        has_digits(password),
        has_special_char(password),
        has_not_phone_namber(password),
        has_not_date(password)
    ])
    return score


if __name__ == '__main__':
    try:
        blacklisted_words = get_blacklist_data(sys.argv[1])
        password = getpass('Enter you password')
        if is_in_blacklist(blacklisted_words, password):
            print('"{}"-password from blacklist'.format(password))
        else:
            print('password strength: {}'.format(get_password_strength(password)))
    except (IndexError, FileNotFoundError):
        exit('Not found blacklist')
