from core.defuzzifier import WeightedAverageDefuzzifier


class InferenceEngine:
    def __init__(self, rules, output_map):
        self.rules = rules
        self.output_map = output_map
        self.defuzzifier = WeightedAverageDefuzzifier()

    def infer(self, fuzzified_inputs):
        outputs = []

        for rule in self.rules:
            strength = rule.evaluate(fuzzified_inputs)
            crisp_output = self.output_map[rule.consequent]

            outputs.append((strength, crisp_output))

        return self.defuzzifier.defuzzify(outputs)