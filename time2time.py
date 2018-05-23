# -*- coding: utf-8 -*-
import datetime
import pytz
import time

tz = pytz.timezone('Asia/Shanghai')


def nowdatetime() -> str:
    """获取utc时间的时间字符串
    :return 2012-10-21 18:51:50
    """
    return ('%s' % datetime.datetime.now(tz)).split('.')[0]


def utcnowdatetime2time() -> float:
    """获取utc时间的时间戳"""
    return time.mktime(datetime.datetime.now(tz).timetuple())


def time2datatime(seconds: float) -> str:
    """将时间戳转换时间字符串
    :param seconds: 1350816710.8050799
    :return 2012-10-21 18:51:50
    """
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(seconds))


def datetime2time(datetimes: str, strtime='%Y-%m-%d %H:%M:%S') -> float:
    """将时间字符串转换成时间戳
    :param datetimes: 2012-10-21 18:51:50
    :param strtime: 需要格式话字符串的格式
    :return: 1350816710.8050799
    """
    return time.mktime(time.strptime(datetimes, strtime))


if __name__ == '__main__':
    print(time2datatime(seconds=1350816710.8050799))
    print(type(utcnowdatetime2time()))
    print(datetime2time('2012-10-21 18:51:50'))
    print(nowdatetime())
