"""
A line plot chart.
"""
from typing import Optional

import numpy as np

from .chart import Chart


class Line(Chart):
    """
    Creates a line plot.
    """

    def __init__(self, data: np.ndarray, title: str, xlabel: str, ylabel: str, color: Optional[str] = None, linestyle: Optional[str] = None):
        """
        Initializes the Line object.

        Args:
            data: The data to be plotted.
            title: The title of the chart.
            xlabel: The label for the x-axis.
            ylabel: The label for the y-axis.
            color: The color of the line.
            linestyle: The style of the line.
        """
        super().__init__(data, title, xlabel, ylabel)
        self.color = color
        self.linestyle = linestyle

    def _prepare_plot(self):
        """
        Prepares the plot by setting the title and labels and plotting the data.
        """
        super()._prepare_plot()
        self.ax.plot(self.data[:, 0], self.data[:, 1], color=self.color, linestyle=self.linestyle)
