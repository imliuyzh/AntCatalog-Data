# https://github.com/imliuyzh/AntCatalog-Data
+ AntCatalog only has the data for graduate classes
+ Classes from some departments like Law are omitted from processing due to higher efforts needed to parse the data
+ The span of data is from Fall 2013 to Spring 2021

## Getting Started
### Structure
+ `original_data`
  + Spreadsheets from PRO (Public Records Office) in UC Irvine
+ `processed_data`
  + Parsed version based on data from WebSOC services
+ `src`
  + A program to fetch the data from WebSOC services to clean the data from PRO (`clean_data.py`)
  + A program to create a SQLite database from the parsed data (`create_db.py`)

### Running the Application
#### Built With
+ Python v3.9+
  + openpyxl
  + beautifulsoup4
  + lxml
+ SQLite

### Steps


## Acknowledgments
This project is made possible by UC Irvine's Public Records Office. But the inspiration has its root from the ZotCurve project.