import matplotlib.pyplot as plt
import numpy as np

class HistogramManager:

    def __init__(self, title, x_label, y_label, bins):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.bins = bins

    def show_histogram(self, data):
        max_value = np.max(np.abs(data))
        if max_value == 0:
            scale_factor = 1
        else:
            scale_factor = 10**(np.floor(np.log10(max_value)) - 1)

        scaled_data = np.array(data) / scale_factor

        plt.hist(scaled_data, bins=self.bins)

        plt.title(f"{self.title} (Data scaled by {scale_factor:.0e})")
        plt.xlabel(f"{self.x_label} (x{scale_factor:.0e})")
        plt.ylabel(self.y_label)

        plt.show()