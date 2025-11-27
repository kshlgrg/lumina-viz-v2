"""
Tests for the Scatter class.
"""
from unittest.mock import MagicMock, patch

import numpy as np
import pytest

from lumina_viz.scatter import Scatter


@pytest.fixture
def scatter_data():
    """
    Returns sample data for testing.
    """
    return np.array([[1, 2], [3, 4]])


@pytest.fixture
def scatter(scatter_data):
    """
    Returns a Scatter instance for testing.
    """
    return Scatter(scatter_data, "Test Scatter", "X-Axis", "Y-Axis")


def test_scatter_init(scatter, scatter_data):
    """
    Tests that the Scatter is initialized correctly.
    """
    assert np.array_equal(scatter.data, scatter_data)
    assert scatter.title == "Test Scatter"
    assert scatter.xlabel == "X-Axis"
    assert scatter.ylabel == "Y-Axis"


def test_scatter_prepare_plot(scatter, scatter_data):
    """
    Tests that the plot is prepared correctly.
    """
    with patch("matplotlib.pyplot.subplots", return_value=(MagicMock(), MagicMock())):
        scatter._prepare_plot()
        scatter.ax.set_title.assert_called_with("Test Scatter")
        scatter.ax.set_xlabel.assert_called_with("X-Axis")
        scatter.ax.set_ylabel.assert_called_with("Y-Axis")
        scatter.ax.scatter.assert_called_once()
        call_args = scatter.ax.scatter.call_args[0]
        assert np.array_equal(call_args[0], scatter_data[:, 0])
        assert np.array_equal(call_args[1], scatter_data[:, 1])
