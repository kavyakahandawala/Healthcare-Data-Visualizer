# Healthcare Data Visualizer

A Python data analysis and visualization project developed as part of the [freeCodeCamp Data Analysis with Python Certification](https://www.freecodecamp.org/learn/data-analysis-with-python/).

This project analyzes medical examination data using **Pandas, NumPy, Matplotlib, Seaborn, and SciPy** to explore relationships between health indicators and cardiovascular disease.

## Project Overview

The project processes medical examination data and creates two visualizations to investigate health-related patterns:

- **Categorical Plot:** Compares the distribution of health indicators between individuals with and without cardiovascular disease.
- **Correlation Heatmap:** Displays correlations between medical features to identify relationships within the dataset.

## Key Features

- Calculated Body Mass Index (BMI) and classified individuals as overweight or not.
- Normalized cholesterol and glucose values into binary categories.
- Filtered out incorrect data using specified health-related conditions.
- Generated a categorical plot to compare medical indicators.
- Created a correlation heatmap to visualize relationships between variables.
- Tested the implementation using the freeCodeCamp challenge test cases.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

## Project Structure

```text
medical-data-visualizer/
│
├── medical_data_visualizer.py
├── main.py
├── test_module.py
├── medical_examination.csv
├── catplot.png
├── heatmap.png
├── requirements.txt
└── README.md
```

## Installation and Execution

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd medical-data-visualizer
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the project:

   ```bash
   python main.py
   ```

The script generates the categorical plot (`catplot.png`) and correlation heatmap (`heatmap.png`).

## Testing

The project includes test cases based on the freeCodeCamp challenge requirements.

**Verification:** All 5 tests passed in the Replit environment.

## Learning Outcomes

- Practiced data cleaning and preprocessing using Pandas.
- Applied conditional transformations to medical datasets.
- Explored relationships between health indicators using statistical analysis.
- Developed data visualizations using Matplotlib and Seaborn.
- Strengthened Python data analysis and testing skills.

## Acknowledgements

- [freeCodeCamp](https://www.freecodecamp.org/) – Data Analysis with Python Certification.
- Dataset and challenge requirements provided by freeCodeCamp.
