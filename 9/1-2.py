from khayyam import JalaliDatetime, JalaliDate
from rtl import rtl


print(JalaliDatetime.now())


print(JalaliDate.today())


print(rtl(JalaliDate.today().strftime("%A %d %B %Y")))


print(JalaliDate(1401, 1, 20).todate())


da_time = JalaliDatetime(1401, 1, 20, 13, 41, 0, 0)
print(da_time.todatetime())
