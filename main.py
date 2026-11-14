"""Run the challenge visualizations and its unit tests."""

import medical_data_visualizer
from unittest import main as run_tests


if __name__ == "__main__":
    medical_data_visualizer.draw_cat_plot()
    medical_data_visualizer.draw_heat_map()
    run_tests(module="test_module", exit=False)
