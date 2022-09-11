from  abc import ABCMeta, abstractclassmethod

"""  
Factory method pattern
"""

class Section(metaclass = ABCMeta): # Abstract class 
    
    @abstractclassmethod
    def describe(self):
        pass


class PersonalInformation(Section):

    def describe(self):
        print("personal Information")


class AlbumSection(Section):

    def describe(self):
        print("Album section ")


class PatentSection(Section):

    def describe(self):
        print("Patent Section  ")


class PublicationSection(Section):

    def describe(self):
        print("Publication section ")

    
# Creator
class Profile(metaclass = ABCMeta):

    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractclassmethod
    def createProfile(self):
        pass

    def getSection(self):
        return self.sections
    
    def addSection(self, section):
        self.sections.append(section)


class Linkedin(Profile):

    def createProfile(self):
        self.addSection(PersonalInformation())
        self.addSection(PatentSection())
        self.addSection(PublicationSection())


class NewNetwork(Profile):

    def createProfile(self):
        self.addSection(PersonalInformation())
        self.addSection(AlbumSection())


# Client
if __name__ =='__main__':
    profile_input = input('choice your profile : [ Linkedin Or NewNetwork ] -> ')
    profile = eval(profile_input)()
    print('your Profile: ', type(profile).__name__)
    print('Feature : ', profile.getSection())
