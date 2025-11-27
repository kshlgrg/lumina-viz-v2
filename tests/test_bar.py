"""
Tests for the Bar class.
"""
from unittest.mock import MagicMock, patch

import numpy as np
import pytest

from lumina_viz.bar import Bar


@pytest.fixture
def bar_data():
    """
    Returns sample data for testing.
    """
    return np.array([[1, 2], [3, 4]])


@pytest.fixture
def bar(bar_data):
    """
    Returns a Bar instance for testing.
    """
    return Bar(bar_data, "Test Bar", "X-Axis", "Y-Axis")


def test_bar_init(bar, bar_data):
    """
    Tests that the Bar is initialized correctly.
    """
    assert np.array_equal(bar.data, bar_data)
    assert bar.title == "Test Bar"
    assert bar.xlabel == "X-Axis"
    assert bar.ylabel == "Y-Axis"


def test_bar_prepare_plot(bar, bar_data):
    """
    Tests that the plot is prepared correctly.
    """
    with patch("matplotlib.pyplot.subplots", return_value=(MagicMock(), MagicMock())):
        bar._prepare_plot()
        bar.ax.set_title.assert_called_with("Test Bar")
        bar.ax.set_xlabel.assert_called_with("X-Axis")
        bar.ax.set_ylabel.assert_called_with("Y-Axis")
        bar.ax.bar.assert_called_once()
        call_args = bar.ax.bar.call_args[0]
        assert np.array_equal(call_args[0], bar_data[:, 0])
        assert np.array_equal(call_args[1], bar_data[:, 1])
