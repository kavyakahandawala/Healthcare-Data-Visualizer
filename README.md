# Medical Data Visualizer

This project analyzes the freeCodeCamp medical examination dataset. It adds an
overweight indicator, normalizes cholesterol and glucose risk values, and
creates:

- `catplot.png`: feature counts split by cardiovascular disease outcome.
- `heatmap.png`: correlations after filtering invalid blood pressure and
  extreme height and weight measurements.

## Run

The official `medical_examination.csv` is included in the project.

```bash
python main.py
```

The command generates both plots and runs the unit tests. To run only the tests:

```bash
python -m unittest test_module
```

Dependencies are listed in `pyproject.toml`.
