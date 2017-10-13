import sys

import zxcvbn


def get_password_strength(password):
    return [0, 3, 5, 7, 10][zxcvbn.zxcvbn(password)['score']]


if __name__ == '__main__':
    a = get_password_strength(sys.argv[1])
    print('Password strength in (0, 10) range is: %s' % a)
