"""
类的基本演示。类方法、静态方法
"""


class Date(object):

    def __init__(self, year=0, month=0, day=0):
        """
        初始化方法
        :param year:年
        :param month:月
        :param day:日
        """
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_as_string):
        """
        类方法
        :param date_as_string:
        :return:
        """
        year, month, day = map(int, date_as_string.split("-"))
        date1 = cls(year, month, day)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        """
        静态方法
        :param date_as_string:
        :return:
        """
        year, month, day = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 2038


d = Date.from_string('2019-11-11')
is_date = Date.is_date_valid('2019-11-11')
print(is_date)
