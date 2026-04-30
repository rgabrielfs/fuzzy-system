from simulation.pendulum_model import PendulumModel

from controllers.pendulum_controller import PendulumController
from controllers.cart_controller import CartController

from utils.plotter import Plotter


class Simulator:

    def __init__(self):

        self.model = PendulumModel()

        self.pendulum_controller = PendulumController()
        self.cart_controller = CartController()

        self.history_angle = []
        self.history_position = []
        self.history_force = []

    def run(self, steps=500):

        for _ in range(steps):

            pendulum_force = (
                self.pendulum_controller.compute_force(
                    self.model.angle,
                    self.model.angular_velocity
                )
            )

            cart_force = (
                self.cart_controller.compute_force(
                    self.model.position,
                    self.model.velocity
                )
            )

            total_force = pendulum_force + cart_force

            self.model.update(total_force)

            self._store_history(total_force)

        self._render_results()

    def _store_history(self, force):

        self.history_angle.append(self.model.angle)

        self.history_position.append(self.model.position)

        self.history_force.append(force)

    def _render_results(self):

        Plotter.plot_all(
            self.history_angle,
            self.history_position
        )