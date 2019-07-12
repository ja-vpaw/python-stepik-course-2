class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, object):
        if object > 0:
            super().append(object)
        else:
            raise NonPositiveError()

a = PositiveList()
a.append(1)
print(a)
a.append(0)
print(a)
