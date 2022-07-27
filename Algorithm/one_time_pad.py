"""  
One Time Pad
"""

import random


class OneTime:
    def encrypt(self, text):
        plain = [ord(i) for i in text]
        key = []
        cipher = []
        for i in plain:
            k = random.randint(1, 300)
            c = (i + k) * k
            cipher.append(c)
            key.append(k)
        return cipher, key

    def decrypt(self, cipher, key):
        plain = []
        for i in range(len(key)):
            p = int((cipher[i] - key[i] ** 2) / key[i])
            plain.append(chr(p))
        result = ''.join([i for i in plain])
        return result


if __name__ == '__main__':
    c, k = OneTime().encrypt('miyankouh')
    print(c)
    print(k)
    print(OneTime().decrypt(c, k))
