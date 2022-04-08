import datetime

# print(dir(datetime))

# all classes in datetime:

# ['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__','__doc__', '__file__',
#  '__loader__', '__name__', '__package__','__spec__', 'date', 'datetime', 'datetime_CAPI',
# 'sys', 'time','timedelta', 'timezone', 'tzinfo']


# d = datetime.date.today()
# delta = datetime.timedelta(days=21)
# 
# print(d+delta)
# print(d-delta)


# dt = datetime.datetime(2022,4,9,13,2,0,0)
# print(dt)
# print(dt.year)
# print(dt.time())


d1 = datetime.datetime(2022,4,7,10,2,0,)
print(datetime.datetime.today()-d1)