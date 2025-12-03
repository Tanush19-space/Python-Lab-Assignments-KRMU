# Weather Data Analyzer

A Python-based command-line tool for analyzing and visualizing weather data from CSV files. This tool processes weather data (temperature, humidity, rainfall) and generates comprehensive statistics, seasonal analysis, and visualizations.

## Features

- **Data Cleaning**: Automatically handles missing values, date parsing, and type coercion
- **Statistical Analysis**: Calculates mean, max, min, and standard deviation for temperature
- **Monthly Analysis**: Aggregates weather metrics by month
- **Seasonal Analysis**: Computes seasonal averages for temperature, rainfall, and humidity
- **Data Visualization**: Generates 4 different plots:
  - Daily temperature trend line chart
  - Monthly rainfall bar chart
  - Humidity vs temperature scatter plot
  - Combined temperature and rainfall visualization
- **Persistent Output**: Saves cleaned data to CSV, plots to PNG, and summary to TXT
- **Flexible Execution**: Command-line arguments for input/output customization

## Requirements

- Python 3.7+
- pandas
- numpy
- matplotlib

## Installation

1. Install Python 3.7 or higher
2. Install dependencies:
```bash
pip install pandas numpy matplotlib
```

3. Download `Weather data analyzer.py`

## Usage

### Basic Usage

```bash
python "Weather data analyzer.py"
```

This assumes a `weather.csv` file in the current directory.

### Custom Input/Output

```bash
python "Weather data analyzer.py" --input data/weather.csv --out-dir ./results
```

### Without Display (Headless Mode)

```bash
python "Weather data analyzer.py" --no-show
```

## Command-Line Arguments

| Argument | Short | Default | Description |
|----------|-------|---------|-------------|
| `--input` | `-i` | `weather.csv` | Path to input CSV file |
| `--out-dir` | `-o` | `.` (current directory) | Output directory for plots and cleaned CSV |
| `--no-show` | - | False | Skip interactive plot display (useful for headless/server environments) |

## Input CSV Format

The input CSV file must contain the following columns:

```csv
Date,Temperature,Humidity,Rainfall
2024-01-01,15.2,65,0
2024-01-02,16.1,62,2.5
2024-01-03,14.8,68,0
...
```

**Required Columns:**
- `Date` - Date in any standard format (e.g., YYYY-MM-DD)
- `Temperature` - Temperature in Celsius
- `Humidity` - Humidity percentage (0-100)
- `Rainfall` - Rainfall in millimeters

## Output Files

The tool generates the following files in the output directory:

1. **cleaned_weather_data.csv** - Cleaned and processed data with Month and Season columns
2. **temperature_trend.png** - Line chart showing daily temperature over time
3. **monthly_rainfall.png** - Bar chart of total rainfall per month
4. **humidity_vs_temperature.png** - Scatter plot showing humidity and temperature relationship
5. **combined_plot.png** - Combined visualization of temperature trend and monthly rainfall
6. **weather_summary.txt** - Text summary of key statistics and file locations

## Output Display

### Console Output

The program prints the following to console:

#### Cleaned Data Sample
Shows the first few rows of processed data

#### Temperature Statistics
- Mean temperature
- Maximum temperature
- Minimum temperature
- Standard deviation

#### Monthly Temperature Statistics
Table showing monthly mean, min, max, and standard deviation for temperature

#### Seasonal Averages
Table showing average temperature, rainfall, and humidity by season

### Generated Plots

All plots are saved as PNG files and displayed interactively (unless `--no-show` is used).

## Data Cleaning

The tool automatically:

- Parses dates in various formats
- Removes rows with invalid dates
- Converts temperature, humidity, and rainfall to numeric values
- Fills missing temperature/humidity values with column mean
- Fills missing rainfall values with 0
- Extracts month and season information

## Seasonal Mapping

Seasons are defined as:
- **Winter**: December, January, February
- **Spring**: March, April, May
- **Summer**: June, July, August
- **Autumn**: September, October, November

## Example Workflow

```bash
# Analyze weather data and generate visualizations
python "Weather data analyzer.py" -i weather_data.csv -o ./weather_reports

# Run without displaying plots (for batch processing)
python "Weather data analyzer.py" -i weather_data.csv -o ./weather_reports --no-show
```

## Error Handling

The program provides error messages for:
- Missing input CSV file
- Missing required columns (Date, Temperature, Humidity, Rainfall)
- Invalid date formats
- Non-numeric values for measurements

## Example CSV File

```csv
Date,Temperature,Humidity,Rainfall
2024-01-01,12.5,68,0
2024-01-02,13.2,65,2.3
2024-01-03,11.8,72,0
2024-01-04,14.1,60,0
2024-02-01,14.5,58,1.5
2024-02-02,15.3,55,0
2024-03-01,18.2,52,0
2024-06-01,25.1,45,0
2024-12-01,8.9,75,3.2
```

## Tips & Best Practices

1. **Large datasets**: For datasets with thousands of rows, the `--no-show` flag is recommended for faster processing
2. **Date formats**: Ensure dates are consistent (e.g., all YYYY-MM-DD)
3. **Units**: Verify that temperature is in Celsius, humidity in %, and rainfall in mm
4. **Missing data**: It's okay to have some missing values—the tool handles them gracefully
5. **Output organization**: Create a separate directory for each analysis run with `--out-dir`

## Troubleshooting

**Q: I get "Error: input file not found"**  
A: Make sure the CSV file exists in the specified path. Use absolute path or ensure the file is in the current directory.

**Q: "Error: missing required columns in CSV"**  
A: Verify your CSV has exactly these columns: Date, Temperature, Humidity, Rainfall

**Q: Plots don't appear**  
A: Try running without `--no-show` flag, or ensure you have a display environment (not headless server).

**Q: Date parsing fails**  
A: The program will attempt various date formats. If it still fails, ensure dates are in YYYY-MM-DD or MM/DD/YYYY format.

**Q: Missing values in output**  
A: The tool fills missing temperature/humidity with mean values and missing rainfall with 0. This is by design.

## Limitations

- Handles only CSV format input (not Excel, JSON, etc.)
- Assumes temperature is in Celsius
- Single-year seasonal analysis (Winter spans Dec-Jan-Feb across year boundary)
- No interpolation for time-series data (uses mean filling only)

## Future Enhancements

- Support for multiple file formats (Excel, JSON, Parquet)
- Advanced time-series analysis (moving averages, trends)
- Anomaly detection for outliers
- Interactive dashboard (with Streamlit or Plotly)
- Export summary reports to PDF
- Comparison across multiple years
- Forecasting capabilities

## License

Educational project - for learning purposes.

## Contact & Contributing

Feel free to fork, modify, and improve this project!

---

**Last Updated**: December 2025  
**Version**: 1.0

