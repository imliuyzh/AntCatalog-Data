# AntCatalog-Data
+ AntCatalog only processes graduate classes
  + Classes from some departments like Law are omitted from processing due to higher efforts needed to parse the data

## Getting Started
### Built With
+ Python v3.10
  + openpyxl
  + beautifulsoup4
  + lxml
+ SQLite

### Steps
1. `cd` into `src` and follow https://www.ics.uci.edu/~thornton/ics32/Notes/ThirdPartyLibraries/ to set up a virtual environment
2. Activate the virtual environment
   + Linux
     1. `cd Scripts`
     2. `source activate`
   + Windows
     1. `cd Scripts`
     2. `activate`
3. `pip -r requirements.txt`
4. Create a `temp` folder in the project root directory
5. Take the data in the `original_data` folder, separate them based on academic years, and put them into the `temp` folder 
   + Check out the `processed_data` folder to have an idea on how the spreadsheets in the `temp` folder will look like (or check below)
6. Run the parsing script (`python clean_data.py` or `python3 clean_data.py`) if you want
   + List the files you want to process in the `SPREADSHEET_FILES` line under `clean_data.py`
   + The result will show up on the `processed_data` folder
     + Courses that cannot be processed will have "F" in the `Processed` column
     + The reason is recorded in `src/log.txt`
   + Remember to change the name of the file in `clean_data.py`
7. Run the database script (`python create_db.py` or `python3 create_db.py`) if you want

| AcadYr | AcadTerm | DepartmentNameByCourseCode | CourseNumber | CourseCode | CourseTitle | Instructors | GradeACount | GradeBCount | GradeCCount | GradeDCount | GradeFCount | GradePCount | GradeNPCount | GPAAvg | Processed |
|--------|----------|----------------------------|--------------|------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|--------------|--------|-----------|
| ...    | ...      | ...                        | ...          | ...        | ...         | ...         | ...         | ...         | ...         | ...         | ...         | ...         | ...          | ...    | ...       |

## Structure
+ `original_data`
  + Spreadsheets from PRO (Public Records Office) in UC Irvine
+ `processed_data`
  + Parsed version based on data from WebSOC services
+ `src`
  + A program to fetch the data from WebSOC services to clean the data from PRO (`clean_data.py`)
  + A program to create a SQLite database from the parsed data (`create_db.py`)

## Acknowledgments
This project is made possible by UC Irvine's Public Records Office. But the inspiration has its root from the ZotCurve project.
