"""
A bar plot chart.
"""
from typing import Optional

import numpy as np

from .chart import Chart


class Bar(Chart):
    """
    Creates a bar plot.
    """

    def __init__(self, data: np.ndarray, title: str, xlabel: str, ylabel: str, color: Optional[str] = None, width: Optional[float] = None):
        """
        Initializes the Bar object.

        Args:
            data: The data to be plotted.
            title: The title of the chart.
            xlabel: The label for the x-axis.
            ylabel: The label for the y-axis.
            color: The color of the bars.
            width: The width of the bars.
        """
        super().__init__(data, title, xlabel, ylabel)
        self.color = color
        self.width = width

    def _prepare_plot(self):
        """
        Prepares the plot by setting the title and labels and plotting the data.
        """
        super()._prepare_plot()
        plot_kwargs = {"color": self.color, "width": self.width}
        filtered_kwargs = {k: v for k, v in plot_kwargs.items() if v is not None}
        self.ax.bar(self.data[:, 0], self.data[:, 1], **filtered_kwargs)
