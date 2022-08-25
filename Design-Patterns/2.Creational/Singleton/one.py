from main import SingletonObject


obj_1 = SingletonObject()
obj_1.file_name = "Obj value 1"
print('print obj_1: ', obj_1)

obj_2 = SingletonObject()
obj_2.file_name = "Obj value 2"
print('print obj_2: ', obj_2)
