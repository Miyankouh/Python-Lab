from abc import ABCMeta, abstractmethod


#AbstractClass
class Travel(metaclass = ABCMeta):

    @abstractmethod
    def day_1(self):
        pass

    @abstractmethod
    def day_2(self):
        pass

    @abstractmethod
    def day_3(self):
        pass

    @abstractmethod
    def coming_back(self):
        pass

    #TemplateMethod
    def travel_program(self):
        self.day_1()
        self.day_2()
        self.day_3()
        self.coming_back()


#ConcreteClass
class SafareShiraz(Travel):

    def day_1(self):
        print("zyarate SHAHCHERAGH")

    def day_2(self):
        print("hafezie va saadie")

    def day_3(self):
        print("Baghe afifiabad va bagh eram")

    def coming_back(self):
        print("coming_back az Safare Shiraz")


class SafareEsfahan(Travel):

    def day_1(self):
        print("Midane naghshe jahan")

    def day_2(self):
        print("40 sotoon")

    def day_3(self):
        print("33 pol va pol khajoo")

    def coming_back(self):
        print("coming_back az Safare Esfahan")


class TravelAgency:

    def tartibDadaneSafar(self):
        maghsad = input("Kodoom shahr mikhayd berid? shiraz ya esfahan?")
        if maghsad == 'shiraz':
            self.safar = SafareShiraz()
            self.safar.travel_program()

        if maghsad == 'esfahan':
            self.safar = SafareEsfahan()
            self.safar.travel_program()


TravelAgency().tartibDadaneSafar()