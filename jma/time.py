import datetime

dt_now = datetime.datetime.now()
datelist = []
datelist.append((dt_now - datetime.timedelta(hours=9)).strftime("%Y"))
datelist.append((dt_now - datetime.timedelta(hours=9)).strftime("%m"))
datelist.append((dt_now - datetime.timedelta(hours=9)).strftime("%d"))
timelag = dt_now -datetime.timedelta(minutes=3)
timelag = timelag - datetime.timedelta(minutes=timelag.minute % 5)
ftimelag = timelag - datetime.timedelta(minutes=timelag.minute%10)
print(timelag)
print(ftimelag)
