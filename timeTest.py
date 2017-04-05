import datetime
now = datetime.datetime.now()
date = now + datetime.timedelta(days = 1)
print(date.strftime('%m/%d/%Y'))
