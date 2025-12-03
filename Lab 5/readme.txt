# Campus Energy Dashboard

A comprehensive Python tool for analyzing and visualizing campus energy consumption across multiple buildings. This system processes meter readings, calculates energy statistics, and generates interactive dashboards and reports.

## Features

- **Multi-Building Data Loading**: Combine energy data from multiple CSV files
- **Manual Data Entry**: Add building meter readings interactively
- **Energy Analytics**: Daily, weekly, and building-wise consumption analysis
- **Visual Dashboard**: Interactive 4-panel dashboard with multiple charts
- **Automated Reports**: Generate summary reports with key insights
- **Data Cleaning**: Handles missing values and data validation
- **OOP Architecture**: Structured classes for MeterReading, Building, and BuildingManager
- **Flexible Output**: CSV exports, PNG dashboard, and text summaries

## Requirements

- Python 3.7+
- pandas
- matplotlib
- pathlib (standard library)

## Installation

1. Install Python 3.7 or higher
2. Install required packages:
```bash
pip install pandas matplotlib
```

3. Download `Lab 5.py`

## Quick Start

### Basic Usage (Load from CSV files)

```bash
python Lab 5.py
```

This assumes a `data/` folder in the current directory containing CSV files.

### Custom Data Folder

```bash
python Lab 5.py /path/to/data/folder
```

### Interactive Data Entry

After running the script, you'll be prompted to add manual entries.

## Input Data Format

### CSV File Structure

Each CSV file in the `data/` folder must contain:

```csv
timestamp,kwh
2024-01-01 00:00,45.2
2024-01-01 01:00,42.8
2024-01-01 02:00,38.5
```

**Required Columns:**
- `timestamp` - Date and time (any standard format)
- `kwh` - Energy consumption in kilowatt-hours

**File Naming:**
- File stem (name without extension) becomes the building name
- Example: `Building_A.csv` → Building_A

### Example File Structure

```
your_project/
├── Lab 5.py
└── data/
    ├── Building_A.csv
    ├── Building_B.csv
    └── Building_C.csv
```

## Usage Workflow

1. **Prepare Data**: Place CSV files in `data/` folder
2. **Run Script**: Execute `python Lab 5.py`
3. **Optional Manual Entry**: Add additional readings if prompted
4. **Review Outputs**: Check generated files and dashboard

## Output Files

The tool generates the following files in the current directory:

### 1. **cleaned_energy_data.csv**
Merged and cleaned dataset with all meter readings
- Columns: timestamp, kwh, building
- Sorted by timestamp
- Invalid entries removed

### 2. **building_summary.csv**
Building-wise energy consumption statistics
- Columns: mean (avg kWh), min, max, total_kwh
- Sorted by total consumption (descending)

### 3. **dashboard.png**
4-panel visualization containing:
- **Top-left**: Daily consumption trend line chart
- **Top-right**: Summary statistics (# buildings, date range)
- **Bottom-left**: Bar chart of total consumption per building
- **Bottom-right**: Scatter plot of individual meter readings

### 4. **summary.txt**
Human-readable energy consumption report including:
- Total campus consumption
- Highest consuming building
- Peak load and timestamp
- Daily/weekly insights
- File references

## Console Output

The program provides real-time feedback:

```
[START] Campus Energy Dashboard pipeline
[INFO] Loaded: Building_A.csv (8760 rows)
[INFO] Loaded: Building_B.csv (8760 rows)
[INFO] Combined DataFrame shape: (17520, 3)
[INFO] Final dataset size after merging: (17520, 3)
[INFO] Cleaned data saved to /path/to/cleaned_energy_data.csv
[INFO] Building summary saved to /path/to/building_summary.csv
[INFO] Dashboard saved to /path/to/dashboard.png
[INFO] Summary report written to /path/to/summary.txt
[DONE] All outputs created successfully.
```

## Data Processing Steps

1. **Loading**: Reads all CSV files from data folder
2. **Validation**: Checks for required columns (timestamp, kwh)
3. **Type Coercion**: Converts timestamps and values to proper types
4. **Cleaning**: Removes rows with missing/invalid data
5. **Merging**: Combines file data with user input (if provided)
6. **Sorting**: Orders by timestamp
7. **Analysis**: Calculates daily, weekly, and building summaries
8. **Visualization**: Creates dashboard
9. **Reporting**: Generates text summary

## Classes

### MeterReading
Represents a single meter reading

```python
reading = MeterReading("2024-01-01 12:00", 45.2)
```

### Building
Represents a building with multiple meter readings

```python
building = Building("Building_A")
building.add_reading(reading)
total = building.calculate_total_consumption()
```

### BuildingManager
Manages multiple buildings and provides summaries

```python
manager = BuildingManager()
manager.load_from_dataframe(df)
totals = manager.summary_totals()
```

## Core Functions

### Data Loading
- `load_and_combine_data(data_folder)` - Loads and combines CSV files
- `collect_user_input()` - Interactively collects meter readings

### Analysis
- `calculate_daily_totals(df)` - Aggregates kWh by day
- `calculate_weekly_aggregates(df)` - Aggregates kWh by week
- `building_wise_summary(df)` - Creates building statistics

### Visualization
- `create_dashboard()` - Generates 4-panel dashboard
- `plot_line()` - Daily trend chart
- `plot_bar()` - Building comparison chart
- `plot_scatter()` - Individual reading scatter plot

### Output
- `save_outputs()` - Saves cleaned data and summaries
- `create_summary_file()` - Generates text report

## Manual Data Entry

When prompted, you can add meter readings interactively:

```
Enter building name: Building_D
Enter timestamp (YYYY-MM-DD HH:MM): 2024-01-01 12:00
Enter kWh value: 52.5
[Added]
```

Type `done` to exit manual entry mode.

## Example Workflow

### Scenario: Analyze 3 Buildings + Add Manual Data

```bash
# File structure
data/
├── Building_A.csv  (12 months of hourly data)
├── Building_B.csv  (12 months of hourly data)
└── Building_C.csv  (12 months of hourly data)

# Run analysis
python Lab 5.py

# When prompted
Would you like to add manual entries? (y/N): y

# Add new building data manually
Enter building name: Building_D
Enter timestamp (YYYY-MM-DD HH:MM): 2024-01-15 14:00
Enter kWh value: 48.3
[Added]
-----------------------
...
```

## Error Handling

The program handles:
- **Missing data folder**: Shows error and exits gracefully
- **Empty CSV files**: Warns and skips
- **Missing columns**: Skips invalid files with warning
- **Invalid timestamps**: Removes rows with invalid dates
- **Invalid kWh values**: Removes rows with non-numeric values
- **Manual entry errors**: Re-prompts for invalid numeric input

## Tips & Best Practices

1. **Data Organization**: Keep all meter CSV files in one `data/` folder
2. **Naming**: Use descriptive building names (no special characters recommended)
3. **Timestamps**: Use consistent format (YYYY-MM-DD HH:MM works best)
4. **Frequency**: Hourly data works best; daily is also supported
5. **File Size**: No hard limits, but 1M+ rows may require more memory
6. **Manual Entry**: Best for adding current/recent readings, not large datasets

## Dashboard Interpretation

- **Daily Trend**: Shows consumption patterns over time
- **Building Comparison**: Identifies high-consuming buildings for efficiency focus
- **Peak Readings**: Highlights when maximum load occurs
- **Statistics Panel**: Quick reference for date range and building count

## Sample Summary Output

```
Campus Energy Consumption Report
----------------------------------------
Total Campus Consumption: 1,234,567.89 kWh

Highest Consuming Building:
- Building_A: 456,789.23 kWh

Peak Load:
- Timestamp: 2024-07-15 16:45:00
- kWh: 89.34

Insights:
- Day with highest consumption: 2024-07-15 (8,945.67 kWh)
- Week with highest consumption ending on: 2024-07-21 (62,340.56 kWh)

Dashboard file: /path/to/dashboard.png
Cleaned data file: /path/to/cleaned_energy_data.csv
Building summary file: /path/to/building_summary.csv
```

## Troubleshooting

**Q: "Data folder not found"**  
A: Ensure `data/` folder exists in the same directory as Lab 5.py, or pass the correct path.

**Q: "No CSV files found"**  
A: Place CSV files in the data folder. Check file extensions are `.csv`.

**Q: "missing required columns"**  
A: CSV files must have `timestamp` and `kwh` columns exactly as named.

**Q: Dashboard not generated**  
A: Ensure matplotlib can render (may need display environment). Use headless mode if on server.

**Q: Manual entry not working**  
A: Use format YYYY-MM-DD HH:MM for timestamps and numeric values for kWh.

## Limitations

- Single data source at a time (pass one folder path)
- Assumes hourly or daily meter readings (not instantaneous data)
- No timezone handling (uses local time)
- Building names derived from filename (can't have special characters)
- Fixed seasonal analysis (no custom period support)

## Future Enhancements

- Real-time data streaming support
- Database integration (PostgreSQL, MongoDB)
- Predictive analytics and forecasting
- Anomaly detection for unusual consumption
- Mobile dashboard/web interface
- Multi-year comparison
- Demand response automation
- Carbon footprint calculations
- Integration with smart meters/IoT devices

## License

Educational project - for learning purposes.

## Contact & Contributing

Feel free to fork, modify, and improve this project!

---

**Last Updated**: December 2025  
**Version**: 1.0  
**Python Compatibility**: 3.7+

