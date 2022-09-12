from abc import ABCMeta, abstractclassmethod


# Subject
class Pay(metaclass = ABCMeta):
    
    @abstractclassmethod
    def do_pay(self):
        pass


# RealSubject
class Bank(Pay):

    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card
        return self.account
    
    def __HaveInventory(self):
        print("Bank: ", self.__getAccount(), "")
        return False
    
    def setCard(self, card):
        self.card = card
    
    def do_pay(self):
        if self.__HaveInventory():
            print("ok")
            return True
        else:
            print("Bank: no")
            return False


# Proxy
class Card(Pay):

    def __init__(self) -> None:
        self.bank = Bank()
    
    def do_pay(self):
        card = input("card number : ")
        self.bank.setCard(card)
        return self.bank.do_pay()


# Client
class You():

    def __init__(self) -> None:
        print("You: I want to buy a t-shirt")
        self.card = Card()
        self.isPurchased = None

    def the_payment(self):
        self.isPurchased = self.card.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("You: ok")
        else:
            print("You: oh!!!!")


you = You()
you.the_payment()
