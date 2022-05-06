import datetime
import time
import schedule


def print_time():
    print(datetime.datetime.now())

# schedule.every(5).seconds.do(print_time)

# schedule.every().minute.at(":20").do(print_time)

# schedule.every().hour.do(print_time)

schedule.every().day.at("18:14:40").do(print_time)

while True:
    schedule.run_pending()
    time.sleep(1)