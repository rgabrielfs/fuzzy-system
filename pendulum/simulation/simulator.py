import matplotlib.pyplot as plt

from simulation.pendulum_model import PendulumModel
from controllers.pendulum_controller import PendulumController
from controllers.cart_controller import CartController


class Simulator:
    def __init__(self):
        self.model = PendulumModel()

        self.pendulum_controller = PendulumController()
        self.cart_controller = CartController()

        self.history_angle = []
        self.history_position = []

    def run(self, steps=500):
        for _ in range(steps):
            pendulum_force = self.pendulum_controller.compute_force(
                self.model.angle,
                self.model.angular_velocity
            )

            cart_force = self.cart_controller.compute_force(
                self.model.position,
                self.model.velocity
            )

            total_force = pendulum_force + cart_force

            self.model.update(total_force)

            self.history_angle.append(self.model.angle)
            self.history_position.append(self.model.position)

        self.plot()

    def plot(self):
        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        plt.title("Ângulo do Pêndulo")
        plt.plot(self.history_angle)
        plt.xlabel("Tempo")
        plt.ylabel("Ângulo")

        plt.subplot(1, 2, 2)
        plt.title("Posição do Carro")
        plt.plot(self.history_position)
        plt.xlabel("Tempo")
        plt.ylabel("Posição")

        plt.tight_layout()
        plt.show()