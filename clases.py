class Parity:
    def __init__(self, num):
        self.num = num

    def check_parity(self):
        if self.num % 2 == 0:
            print("{} is even".format(self.num))
        else:
            print("{} is odd.".format(self.num))


x = Parity(42)
x.check_parity()
