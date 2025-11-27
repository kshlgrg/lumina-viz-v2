"""
Tests for the Line class.
"""
from unittest.mock import MagicMock, patch

import numpy as np
import pytest

from lumina_viz.line import Line


@pytest.fixture
def line_data():
    """
    Returns sample data for testing.
    """
    return np.array([[1, 2], [3, 4]])


@pytest.fixture
def line(line_data):
    """
    Returns a Line instance for testing.
    """
    return Line(line_data, "Test Line", "X-Axis", "Y-Axis")


def test_line_init(line, line_data):
    """
    Tests that the Line is initialized correctly.
    """
    assert np.array_equal(line.data, line_data)
    assert line.title == "Test Line"
    assert line.xlabel == "X-Axis"
    assert line.ylabel == "Y-Axis"


def test_line_prepare_plot(line, line_data):
    """
    Tests that the plot is prepared correctly.
    """
    with patch("matplotlib.pyplot.subplots", return_value=(MagicMock(), MagicMock())):
        line._prepare_plot()
        line.ax.set_title.assert_called_with("Test Line")
        line.ax.set_xlabel.assert_called_with("X-Axis")
        line.ax.set_ylabel.assert_called_with("Y-Axis")
        line.ax.plot.assert_called_once()
        call_args = line.ax.plot.call_args[0]
        assert np.array_equal(call_args[0], line_data[:, 0])
        assert np.array_equal(call_args[1], line_data[:, 1])
