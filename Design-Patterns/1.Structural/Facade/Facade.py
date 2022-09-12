"""  
Facade Pattern
"""

# Facade
class EventManager():

    def __init__(self):
        print('EventManager: Let me coordinate with everyone\n')
    
    def arrange(self):
        self.presenter = Presenter()
        self.presenter.setPresentation()

        self.theaterGroup = TheaterGroup()
        self.theaterGroup.setTheater()

        self.caterer = Caterer()
        self.caterer.setCatering()

        self.lecturer = Lecturer()
        self.lecturer.setLecturer() 

        self.musicGroup = MusicGroup()
        self.musicGroup.setMusic()


# Subsystem
class Presenter():

    def __init__(self):
        print('[time] [day]')

    def setPresentation(self):
        print('2h, 4 day')


class TheaterGroup():

    def __init__(self):
        print('[real] [jok]')

    def setTheater(self):
        print('jok')


class Caterer():

    def __init__(self):
        print('[food]')

    def setCatering(self):
        print('Donuts, Oreo Cookies, French Fries, Salmon')


class Lecturer():

    def __init__(self):
        print('[The topic of the speech]')

    def setLecturer(self):
        print('jok')


class MusicGroup():

    def __init__(self):
        print('[music]')

    def setMusic(self):
        print('traditional music')


# Client
class You():
    
    def __init__(self) -> None:
        print('You: Celebrating is hard work')
    
    def askEventManager(self):
        print('yes')
        em = EventManager()
        em.arrange()

    def __del__(self):
        print('You: Tank you!!!!')


you = You()
you.askEventManager()
