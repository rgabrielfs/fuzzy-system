from core.membership import TriangularMembership
from core.fuzzy_variable import FuzzyVariable
from core.fuzzy_rule import FuzzyRule
from core.inference_engine import InferenceEngine


class CartController:
    def __init__(self):
        self.position = FuzzyVariable("position")
        self.velocity = FuzzyVariable("velocity")

        self._create_memberships()

        self.engine = InferenceEngine(
            self._create_rules(),
            self._output_map()
        )

    def _create_memberships(self):
        self.position.add_set("N", TriangularMembership(-10, -5, 0))
        self.position.add_set("Z", TriangularMembership(-2, 0, 2))
        self.position.add_set("P", TriangularMembership(0, 5, 10))

        self.velocity.add_set("N", TriangularMembership(-10, -5, 0))
        self.velocity.add_set("Z", TriangularMembership(-2, 0, 2))
        self.velocity.add_set("P", TriangularMembership(0, 5, 10))

    def _output_map(self):
        return {
            "FN": -100,
            "N": -50,
            "LN": -20,
            "Z": 0,
            "LP": 20,
            "P": 50,
            "FP": 100
        }

    def _create_rules(self):
        return [
            FuzzyRule([("position", "N"), ("velocity", "N")], "FP"),
            FuzzyRule([("position", "N"), ("velocity", "Z")], "P"),
            FuzzyRule([("position", "N"), ("velocity", "P")], "Z"),

            FuzzyRule([("position", "Z"), ("velocity", "N")], "LP"),
            FuzzyRule([("position", "Z"), ("velocity", "Z")], "Z"),
            FuzzyRule([("position", "Z"), ("velocity", "P")], "LN"),

            FuzzyRule([("position", "P"), ("velocity", "N")], "Z"),
            FuzzyRule([("position", "P"), ("velocity", "Z")], "N"),
            FuzzyRule([("position", "P"), ("velocity", "P")], "FN")
        ]

    def compute_force(self, position_value, velocity_value):
        fuzzified = {
            "position": self.position.fuzzify(position_value),
            "velocity": self.velocity.fuzzify(velocity_value)
        }

        return self.engine.infer(fuzzified)