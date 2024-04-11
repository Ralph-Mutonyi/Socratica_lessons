import datetime

gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.month)
print(gvr.day)
print(gvr.year)

# timedelta

oddDay = datetime.date(200, 1, 1)
dt = datetime.timedelta(100)
print(oddDay + dt)

# format of the date

print(gvr.strftime("%A, %B %d, %Y"))

message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))

