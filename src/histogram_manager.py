import matplotlib.pyplot as plt
import numpy as np

class HistogramManager:

    def __init__(self, title: str, x_label: str, y_label: str, bins: int) -> None:
        """Initialize histogram manager with title, axis labels, and bin count."""
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.bins = bins

    def show_histogram(self, data: np.ndarray) -> None:
        """Display a histogram without scaling and indicate that the units are arbitrary."""
        plt.hist(data, bins=self.bins)
        plt.title(self.title)
        plt.xlabel(f"{self.x_label} (arbitrary units)")
        plt.ylabel(self.y_label)
        plt.show()
