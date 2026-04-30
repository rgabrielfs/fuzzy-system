import matplotlib.pyplot as plt


class Plotter:

    @staticmethod
    def plot_angle(history):
        plt.figure(figsize=(8, 4))
        plt.title("Ângulo do Pêndulo")
        plt.plot(history)
        plt.xlabel("Tempo")
        plt.ylabel("Ângulo")
        plt.grid(True)
        plt.show()

    @staticmethod
    def plot_position(history):
        plt.figure(figsize=(8, 4))
        plt.title("Posição do Carro")
        plt.plot(history)
        plt.xlabel("Tempo")
        plt.ylabel("Posição")
        plt.grid(True)
        plt.show()

    @staticmethod
    def plot_all(angle_history, position_history):
        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        plt.title("Ângulo do Pêndulo")
        plt.plot(angle_history)

        plt.subplot(1, 2, 2)
        plt.title("Posição do Carro")
        plt.plot(position_history)

        plt.tight_layout()
        plt.show()