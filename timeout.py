from threading import Timer


def timeout(interval):
    """函数超时装饰器
    :param interval: 超时时间
    :return:
    """
    def wraps(func):
        def time_out():
            raise TimeoutError("func {} run timeout, timetou {} S".format(func.__name__, interval))

        def deco(*args, **kwargs):
            timer = Timer(interval, time_out)
            timer.start()
            res = func(*args, **kwargs)
            timer.cancel()
            return res

        return deco

    return wraps
