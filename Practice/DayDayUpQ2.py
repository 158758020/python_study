#DayDayUpQ2.py
dayfactor=0.05
dayup=pow(1+dayfactor,7)*20
daydown=pow(1-dayfactor,7)*20
print("向上:{:.2f},向下:{:.2f}".format(dayup,daydown))
