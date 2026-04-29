from core.membership import TriangularMembership
from core.fuzzy_variable import FuzzyVariable
from core.fuzzy_rule import FuzzyRule
from core.inference_engine import InferenceEngine


class PendulumController:
    def __init__(self):
        self.angle = FuzzyVariable("angle")
        self.angular_velocity = FuzzyVariable("angular_velocity")

        self._create_memberships()
        self.engine = InferenceEngine(
            self._create_rules(),
            self._output_map()
        )

    def _create_memberships(self):
        self.angle.add_set("N", TriangularMembership(-30, -15, 0))
        self.angle.add_set("Z", TriangularMembership(-10, 0, 10))
        self.angle.add_set("P", TriangularMembership(0, 15, 30))

        self.angular_velocity.add_set("N", TriangularMembership(-10, -5, 0))
        self.angular_velocity.add_set("Z", TriangularMembership(-2, 0, 2))
        self.angular_velocity.add_set("P", TriangularMembership(0, 5, 10))

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
            FuzzyRule([("angle", "N"), ("angular_velocity", "N")], "FN"),
            FuzzyRule([("angle", "N"), ("angular_velocity", "Z")], "N"),
            FuzzyRule([("angle", "N"), ("angular_velocity", "P")], "Z"),

            FuzzyRule([("angle", "Z"), ("angular_velocity", "N")], "LN"),
            FuzzyRule([("angle", "Z"), ("angular_velocity", "Z")], "Z"),
            FuzzyRule([("angle", "Z"), ("angular_velocity", "P")], "LP"),

            FuzzyRule([("angle", "P"), ("angular_velocity", "N")], "Z"),
            FuzzyRule([("angle", "P"), ("angular_velocity", "Z")], "P"),
            FuzzyRule([("angle", "P"), ("angular_velocity", "P")], "FP")
        ]

    def compute_force(self, angle_value, angular_velocity_value):
        fuzzified = {
            "angle": self.angle.fuzzify(angle_value),
            "angular_velocity": self.angular_velocity.fuzzify(angular_velocity_value)
        }

        return self.engine.infer(fuzzified)