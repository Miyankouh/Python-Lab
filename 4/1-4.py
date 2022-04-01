def secure_card_number(card_number):
    secure = "*" * 15  + card_number[-4:]
    return secure

print (secure_card_number("6037-5896-2547-3698"))

