"""
Tests for the Chart class.
"""
from unittest.mock import MagicMock, patch

import numpy as np
import pytest

from lumina_viz.chart import Chart


@pytest.fixture
def chart_data():
    """
    Returns sample data for testing.
    """
    return np.array([[1, 2], [3, 4]])


@pytest.fixture
def chart(chart_data):
    """
    Returns a Chart instance for testing.
    """
    return Chart(chart_data, "Test Chart", "X-Axis", "Y-Axis")


def test_chart_init(chart, chart_data):
    """
    Tests that the Chart is initialized correctly.
    """
    assert np.array_equal(chart.data, chart_data)
    assert chart.title == "Test Chart"
    assert chart.xlabel == "X-Axis"
    assert chart.ylabel == "Y-Axis"
    assert chart.fig is None
    assert chart.ax is None


def test_chart_prepare_plot(chart):
    """
    Tests that the plot is prepared correctly.
    """
    with patch("matplotlib.pyplot.subplots", return_value=(MagicMock(), MagicMock())) as mock_subplots:
        chart._prepare_plot()
        mock_subplots.assert_called_once()
        chart.ax.set_title.assert_called_with("Test Chart")
        chart.ax.set_xlabel.assert_called_with("X-Axis")
        chart.ax.set_ylabel.assert_called_with("Y-Axis")


def test_chart_show(chart):
    """
    Tests that the chart is displayed correctly.
    """
    with patch("matplotlib.pyplot.show") as mock_show, \
         patch("matplotlib.pyplot.subplots", return_value=(MagicMock(), MagicMock())):
        chart.show()
        mock_show.assert_called_once()


def test_chart_save(chart):
    """
    Tests that the chart is saved correctly.
    """
    with patch("matplotlib.pyplot.subplots", return_value=(MagicMock(), MagicMock())):
        chart.save("test.png")
        chart.fig.savefig.assert_called_with("test.png", dpi=300)


def test_chart_set_figsize(chart):
    """
    Tests that the figure size is set correctly.
    """
    with patch("matplotlib.pyplot.subplots", return_value=(MagicMock(), MagicMock())):
        chart.set_figsize((10, 5))
        chart.fig.set_size_inches.assert_called_with((10, 5))


def test_chart_set_xlim(chart):
    """
    Tests that the x-axis limits are set correctly.
    """
    with patch("matplotlib.pyplot.subplots", return_value=(MagicMock(), MagicMock())):
        chart.set_xlim((0, 10))
        chart.ax.set_xlim.assert_called_with((0, 10))


def test_chart_set_ylim(chart):
    """
    Tests that the y-axis limits are set correctly.
    """
    with patch("matplotlib.pyplot.subplots", return_value=(MagicMock(), MagicMock())):
        chart.set_ylim((0, 20))
        chart.ax.set_ylim.assert_called_with((0, 20))
