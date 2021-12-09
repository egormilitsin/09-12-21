#main project

class One(object):

    @staticmethod
    def metod1(a):
        l = [x for x in range(a) if x % 2 == 0]
        return l

    @staticmethod
    def metod2(a):
        l = [x for x in range(a) if x % 5 == 0]
        return l

l1=One.metod1(10)
l2=One.metod2(10)
print(l2)