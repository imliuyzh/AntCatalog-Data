# https://github.com/imliuyzh/AntCatalog-Data
+ AntCatalog only has the data for graduate classes
+ Classes from some departments like Law are omitted from processing due to higher efforts needed to parse the data
+ The span of data is from Fall 2013 to Spring 2021

## Getting Started
### Project Structure
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

#### Steps
1. `cd` into `src` and follow https://www.ics.uci.edu/~thornton/ics32/Notes/ThirdPartyLibraries/ to set up a virtual environment
2. Activate the virtual environment
   + Linux
     1. `cd Scripts`
     2. `source activate`
   + Windows
     1. `cd Scripts`
     2. `activate`
3. `pip -r requirements.txt`

##### `clean_data.py`
Run the parsing script (`python clean_data.py` or `python3 clean_data.py`) if you want

##### `create_db.py`
Run the database script (`python create_db.py` or `python3 create_db.py`) if you want

## Acknowledgments
This project is made possible by UC Irvine's Public Records Office. But the inspiration has its root from the ZotCurve project.