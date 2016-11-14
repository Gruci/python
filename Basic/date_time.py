import datetime

print(datetime.datetime.now())

start_time = datetime.datetime.now()
type(start_time)

start_time = datetime.datetime(2016,11,16)
how_long = start_time - datetime.datetime.now()

print(how_long.days)
print(how_long.seconds)

hundred = datetime.timedelta(days = 100)
print(datetime.datetime.now() + hundred)
hundred_bf = datetime.timedelta(days = -100)
print(datetime.datetime.now() + hundred_bf)
print(datetime.datetime.now() - hundred)

tomorrow = datetime.datetime.now().replace(hour = 9, minute = 0, second = 0) + datetime.timedelta(days = 1)
print(tomorrow)