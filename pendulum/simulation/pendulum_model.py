import numpy as np


class PendulumModel:
    def __init__(self):
        self.angle = 10.0
        self.angular_velocity = 0.0

        self.position = 0.0
        self.velocity = 0.0

        self.dt = 0.02

    def update(self, force):
        gravity = 9.81
        length = 1.0

        angular_acceleration = (
            gravity * np.sin(np.radians(self.angle))
            + force * 0.01
        )

        self.angular_velocity += angular_acceleration * self.dt
        self.angle += self.angular_velocity * self.dt

        linear_acceleration = force * 0.05

        self.velocity += linear_acceleration * self.dt
        self.position += self.velocity * self.dt