class Borg(object):
    _shared_state = {}
    var = 1

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class Child(Borg):
    pass

if __name__ == '__main__':
    borg = Borg()
    borg1 = Borg()
    print(borg is borg1)
    borg.var += 2
    print(borg1.var)
    child = Child()
    borg1.var += 3
    print(child is borg)
    print(child.var)