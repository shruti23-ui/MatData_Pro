# MatData Pro

**MatData Pro** is a web-based data analysis tool for material science data. Built using Streamlit, this app allows users to upload CSV files, filter data, and visualize results through various plots. It also provides the option to download the processed data.

## Features

- **Data Upload**: Upload CSV files to analyze material science data.
- **Data Preview**: View the first few rows of the uploaded data.
- **Data Summary**: Get basic statistics about the dataset.
- **Data Filtering**: Filter data based on selected columns and values.
- **Visualizations**:
  - **Histogram**: Generate and view histograms of selected data columns.
  - **Bar Plot**: Create bar plots to visualize categorical data.
  - **Scatter Plot**: Plot scatter plots to observe relationships between two variables.
  - **Correlation Heatmap**: View a heatmap to understand relationships between multiple variables.
- **Download Processed Data**: Download the filtered and processed data as a CSV file.

## Technologies Used

- **Streamlit**: For building the user interface.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For creating static, animated, and interactive visualizations.
- **Seaborn**: For statistical data visualization.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shruti23-ui/MatData_Pro.git
   ```
2. Navigate to the project directory
   ```bash
   cd MatData_Pro
   ```
3. Set up a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

   ```
5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- **Upload CSV**: Click on the "Upload your CSV file" button to upload your material science data in CSV format.
- **Data Preview**: The first few rows of the uploaded data will be displayed.
- **Data Summary**: Basic statistics of the data will be shown.
- **Filter Data**: Select a column to filter and enter the value to filter the data.
- **Visualizations**:
  - Select columns to generate and view histograms, bar plots, and scatter plots.
  - View a correlation heatmap to understand relationships between variables.
- **Download Processed Data**: Download the filtered and processed data as a CSV file.

## Contribution

Feel free to contribute by opening issues or submitting pull requests. 

## License

This project is licensed under the MIT License.

---
