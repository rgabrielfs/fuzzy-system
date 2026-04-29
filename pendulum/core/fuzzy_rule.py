class FuzzyRule:
    def __init__(self, antecedents, consequent):
        self.antecedents = antecedents
        self.consequent = consequent

    def evaluate(self, fuzzified_inputs):
        values = []

        for variable_name, set_name in self.antecedents:
            values.append(
                fuzzified_inputs[variable_name][set_name]
            )

        return min(values)