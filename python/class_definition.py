class Num():
    '''
        Various numerical activities
    '''

    def __init__(self, num):
        self.number = num

    def square(self):
        return self.number ** 2

if __name__ == '__main__':
    n = Num(2)
    print(n.square())