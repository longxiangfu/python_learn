"""
类的基本演示
模块名即文件名
"""

import datetime #import 模块名
from dateutil import rrule #from 报名 import 模块名


class BetDate:
    def __init__(self, start_date, stop_date):
        self.start = datetime.datetime.strptime(start_date, "%Y %m %d")
        self.stop = datetime.datetime.strptime(stop_date, "%Y %m %d")

    def calculateDays(self):
        d = self.stop - self.start
        return d.days if d.days > 0 else False

    def calculateWeeks(self):
        weeks = rrule.rrule(rrule.WEEKLY, dtstart=self.start, until=self.stop)
        return weeks.count()


fir_twe = BetDate("2019 5 1", "2019 11 25")
d = fir_twe.calculateDays()
w = fir_twe.calculateWeeks()
print("Between 2019-5-1, 2019-11-25")
print("Days is:", d)
print("Weeks is;", w)
