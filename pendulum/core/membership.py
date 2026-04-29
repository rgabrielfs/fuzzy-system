class TriangularMembership:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def compute(self, x):
        if x <= self.a or x >= self.c:
            return 0.0

        if x == self.b:
            return 1.0

        if x < self.b:
            return (x - self.a) / (self.b - self.a)

        return (self.c - x) / (self.c - self.b)