class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        return sum([self.transform(i) for i in range(0, N + 1)])


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, N):
        return sum(i ** self.b for i in range(1, N + 1))


class SquareSummator(PowerSummator):
    def __init__(self, b):
        super().__init__(b)


class CubeSummator(PowerSummator):
    def __init__(self, b):
        super().__init__(b)
