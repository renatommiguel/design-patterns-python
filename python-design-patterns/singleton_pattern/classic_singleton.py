class ClassicSingleton(object):
    var = 1

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ClassicSingleton, cls).__new__(cls)
        return cls.instance


class SandBox:
    var = 10


if __name__ == '__main__':
    sing = ClassicSingleton()
    sing.var += 1
    print(sing.var)

    sing2 = ClassicSingleton()
    sing2.var += 1
    print(sing2.var)

    sb1 = SandBox()
    sb1.var += 1
    print(sb1.var) # 2

    sb2 = SandBox()
    sb2.var += 4
    print(sb2.var) # 5
    print('Done')
