"""  
    cipher: a1z26
        miyankouh <=> [1, 13, 9, 18]

        use unicode:
        print(ord('a')) # 97
        print(ord('/')) # 48

        print(chr(91)) # [
        print(chr(98)) # b
        print(chr(86)) # v

"""

def encode(plain):
    return [ord(elm) - 92 for elm in plain]


def decode(encode):
    return "".join(chr(elm + 92)  for elm in encode)


if __name__ == "__main__":
    print(encode('miyankouh'))
    print(decode([17, 13, 29, 5, 18, 15, 19, 25, 12]))
