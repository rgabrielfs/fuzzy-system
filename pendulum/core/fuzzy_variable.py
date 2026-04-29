class FuzzyVariable:
    def __init__(self, name):
        self.name = name
        self.sets = {}

    def add_set(self, label, membership_function):
        self.sets[label] = membership_function

    def fuzzify(self, value):
        memberships = {}

        for label, mf in self.sets.items():
            memberships[label] = mf.compute(value)

        return memberships