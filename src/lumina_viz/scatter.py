"""
A scatter plot chart.
"""
from typing import Optional

import numpy as np

from .chart import Chart


class Scatter(Chart):
    """
    Creates a scatter plot.
    """

    def __init__(self, data: np.ndarray, title: str, xlabel: str, ylabel: str, color: Optional[str] = None, size: Optional[int] = None):
        """
        Initializes the Scatter object.

        Args:
            data: The data to be plotted.
            title: The title of the chart.
            xlabel: The label for the x-axis.
            ylabel: The label for the y-axis.
            color: The color of the markers.
            size: The size of the markers.
        """
        super().__init__(data, title, xlabel, ylabel)
        self.color = color
        self.size = size

    def _prepare_plot(self):
        """
        Prepares the plot by setting the title and labels and plotting the data.
        """
        super()._prepare_plot()
        self.ax.scatter(self.data[:, 0], self.data[:, 1], c=self.color, s=self.size)
