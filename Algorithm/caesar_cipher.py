from string import ascii_letters


def encrypt(string, key):
    alpha = ascii_letters
    result =  ''

    for ch in string:
        if ch not in alpha:
            result += ch
        else:
            new_key = (alpha.index(ch) + key) % len(alpha)
            result += alpha[new_key]
    return result


def decrypt(string, key):
    key *= -1
    return encrypt(string, key)


def brut_force(string):
    alpha = ascii_letters
    key = 1
    result = ''
    brut_force_data = {}

    while key <= len(alpha):
        result = decrypt(string, key)
        brut_force_data[key] = result
        result = ''
        key += 1
    return brut_force_data


if __name__ == '__main__':
    print(encrypt('Sohrab', 4))   # Wslvef
    print(decrypt('Wslvef', 4))   # Sohrab
    print(brut_force('Wslvef'))   # Sohrab
