class WeightedAverageDefuzzifier:
    def defuzzify(self, outputs):
        numerator = 0.0
        denominator = 0.0

        for strength, value in outputs:
            numerator += strength * value
            denominator += strength

        if denominator == 0:
            return 0.0

        return numerator / denominator