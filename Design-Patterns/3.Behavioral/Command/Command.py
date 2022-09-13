from abc import ABCMeta, abstractclassmethod

""" 
Command pattern
"""

# Command
class Order(metaclass = ABCMeta):
    @abstractclassmethod
    def execute(self):
        pass


# Concrete Command
class BuyHouse(Order):
    def __init__(self, house):
        self.house = house

    def execute(self):
        self.house.buy()


class SellHouse(Order):
    def __init__(self, house):
        self.house = house

    def execute(self):
        self.house.sell()


# Receiver
class HouseTread:

    def buy(self):
        print('buy the house')
    
    def sell(self):
        print("sell house")


# Invoker
class Agent():

    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()


# Client
if __name__ == "__main__":
    house = HouseTread()
    buy_house = BuyHouse(house)
    sell_house = SellHouse(house)

    # Invoker
    agent = Agent()
    agent.placeOrder(buy_house)
    agent.placeOrder(sell_house)
