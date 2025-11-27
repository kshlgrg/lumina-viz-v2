"""
The core chart object in the lumina-viz library.
"""

from typing import Optional, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np


class Chart:
    """
    A base class for creating beautiful and insightful charts.
    """

    def __init__(self, data: np.ndarray, title: str, xlabel: str, ylabel: str):
        """
        Initializes the Chart object.

        Args:
            data: The data to be plotted.
            title: The title of the chart.
            xlabel: The label for the x-axis.
            ylabel: The label for the y-axis.
        """
        self.data = data
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.fig = None
        self.ax = None

    def _init_fig_ax(self):
        """
        Initializes the figure and axes if they don't exist.
        """
        if self.fig is None:
            self.fig, self.ax = plt.subplots()

    def _prepare_plot(self):
        """
        Prepares the plot by setting the title and labels.
        """
        self._init_fig_ax()
        self.ax.set_title(self.title)
        self.ax.set_xlabel(self.xlabel)
        self.ax.set_ylabel(self.ylabel)

    def show(self):
        """
        Displays the chart.
        """
        self._prepare_plot()
        plt.show()

    def save(self, path: str, dpi: int = 300):
        """
        Saves the chart to a file.

        Args:
            path: The path to save the chart to.
            dpi: The resolution of the saved chart.
        """
        self._prepare_plot()
        self.fig.savefig(path, dpi=dpi)

    def set_figsize(self, figsize: Tuple[int, int]):
        """
        Sets the figure size.

        Args:
            figsize: The figure size as a tuple of (width, height).
        """
        self._init_fig_ax()
        self.fig.set_size_inches(figsize)
        return self

    def set_xlim(self, xlim: Tuple[Union[int, float], Union[int, float]]):
        """
        Sets the x-axis limits.

        Args:
            xlim: The x-axis limits as a tuple of (min, max).
        """
        self._init_fig_ax()
        self.ax.set_xlim(xlim)
        return self

    def set_ylim(self, ylim: Tuple[Union[int, float], Union[int, float]]):
        """
        Sets the y-axis limits.

        Args:
            ylim: The y-axis limits as a tuple of (min, max).
        """
        self._init_fig_ax()
        self.ax.set_ylim(ylim)
        return self
