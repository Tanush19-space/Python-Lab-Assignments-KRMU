# GradeBook Analyzer CLI

A command-line tool for analyzing student marks and generating statistical reports with grade assignments.

## Features

- **Flexible Data Input**: Enter student data manually or load from CSV file
- **Statistical Analysis**: Calculate average, median, highest, and lowest scores
- **Grade Assignment**: Automatically assign grades based on marks
- **Grade Distribution**: View the count of each grade (A-F)
- **Pass/Fail Analysis**: Identify passing and failing students
- **Results Table**: Display a formatted table with all results
- **Interactive CLI**: User-friendly menu-driven interface

## Grading Scale

| Grade | Marks Range |
|-------|-------------|
| A     | 90 - 100    |
| B     | 80 - 89     |
| C     | 70 - 79     |
| D     | 60 - 69     |
| F     | Below 60    |

**Pass Requirement**: Marks ≥ 40

## Installation

No external dependencies required! This tool uses only Python's built-in libraries:
- `csv` - for reading CSV files
- `statistics` - for calculating median

Requires Python 3.x

## Usage

### Running the Program

```bash
python "Grade book.py"
```

### Input Methods

#### Option 1: Manual Entry
```
Enter your choice (1 or 2): 1
How many students? 3
Enter name of student 1: Alice
Enter marks for Alice: 95
Enter name of student 2: Bob
Enter marks for Bob: 78
Enter name of student 3: Charlie
Enter marks for Charlie: 85
```

#### Option 2: Load from CSV
```
Enter your choice (1 or 2): 2
Enter CSV filename (with .csv extension): data.csv
```

**CSV File Format**:
```csv
Student Name,Marks
Alice,95
Bob,78
Charlie,85
```

### Sample Output

```
--- Statistical Summary ---
Average Marks: 86.00
Median Marks:  85.00
Highest Marks: 95.00
Lowest Marks:  78.00

--- Grade Distribution ---
Grade A: 2 student(s)
Grade B: 1 student(s)
Grade C: 0 student(s)
Grade D: 0 student(s)
Grade F: 0 student(s)

--- Pass/Fail Summary ---
Passed Students (3): Alice, Bob, Charlie
Failed Students (0): None

Name            Marks   Grade
---------------------------------
Alice           95.00   A
Bob             78.00   C
Charlie         85.00   B
---------------------------------
```

## Functions

### Core Functions

- **`load_data()`** - Loads student data from manual input or CSV file
- **`calculate_average(marks_dict)`** - Returns average of all marks
- **`calculate_median(marks_dict)`** - Returns median of all marks
- **`find_max_score(marks_dict)`** - Returns highest mark
- **`find_min_score(marks_dict)`** - Returns lowest mark
- **`assign_grades(marks)`** - Assigns letter grades to all students
- **`grade_distribution(grades)`** - Displays count of each grade
- **`pass_fail_summary(marks)`** - Lists passing and failing students
- **`display_results_table(marks, grades)`** - Shows formatted results table

## Features in Detail

### Statistical Summary
Provides comprehensive statistics:
- Average (mean) marks
- Median marks
- Highest score
- Lowest score

### Grade Assignment
Automatically assigns grades based on the grading scale above.

### Grade Distribution
Shows how many students received each grade (A through F).

### Pass/Fail Analysis
- Lists all passing students (≥ 40 marks)
- Lists all failing students (< 40 marks)
- Shows count for each category

### Results Table
Displays all students with their marks and assigned grades in an organized table format.

## Example Workflow

1. Run the program
2. Choose input method (manual or CSV)
3. Enter or load student data
4. View comprehensive analysis including:
   - Statistical summaries
   - Grade distribution
   - Pass/fail status
   - Detailed results table
5. Optionally analyze another dataset

## CSV File Requirements

- First row must be headers (e.g., "Student Name,Marks")
- Each subsequent row should contain: `name,marks`
- Marks should be numeric values
- File must have `.csv` extension

## Error Handling

The program includes error handling for:
- File not found errors when loading CSV
- Invalid input choices
- Empty datasets

## Tips

- Save your data in CSV format for easy reuse
- The tool supports multiple analysis sessions without restarting
- Marks can be decimal values (e.g., 85.5)
- Student names can include spaces

## Example CSV File

Create a file named `data.csv`:

```csv
Student Name,Marks
Ayush Raj,90
Vishnu Shankar,87
Angad Singh,92
Gourav Sen,88
Sunil Kumar,85
Rajesh Kumar,91
Ankit Tiwari,89
```

Then load it using Option 2 in the program.

## License

This project is provided as-is for educational purposes.

## Contributing

Feel free to fork, modify, and improve this project!

## Support

For issues or suggestions, please create an issue or submit a pull request.

