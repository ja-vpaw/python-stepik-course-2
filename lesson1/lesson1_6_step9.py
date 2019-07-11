import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, object):
        super().append(object)
        self.log(self[-1])


a = LoggableList()
a.append('1')
