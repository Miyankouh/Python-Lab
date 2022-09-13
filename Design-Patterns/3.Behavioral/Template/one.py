from abc import ABCMeta, abstractclassmethod

# AbstractClass
class Compiler(metaclass = ABCMeta):

    @abstractclassmethod
    def collectSource(self):
        pass

    @abstractclassmethod
    def compileToObject(self):
        pass

    @abstractclassmethod
    def run(self):
        pass
    
    # TemplateMethod
    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()
    

# Concrete class
class IosCompiler(Compiler):

    def collectSource(self):
        print("collecting Source code")
    
    def compileToObject(self):
        print("compiling source code tp Object code")

    def run(self):
        print("program running")


ios = IosCompiler()
ios.compileAndRun()