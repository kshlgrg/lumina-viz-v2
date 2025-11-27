# lumina-viz

A modern Python visualization library.

## Installation

```bash
pip install lumina-viz
```

## Usage

```python
import numpy as np
from lumina_viz import Scatter

data = np.random.rand(100, 2)
chart = Scatter(data, "My Scatter Plot", "X-Axis", "Y-Axis")
chart.show()
```
