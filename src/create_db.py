import sqlite3
import openpyxl
from pathlib import Path
from time import asctime

def create_index() -> None:
    '''Index several fields on the Course and Instructor table.'''
    connection = sqlite3.connect("../data.db")
    try:
        print(f"[{asctime()}] Begin creating index")
        connection.executescript(
            """
            CREATE INDEX TermIndex ON Course (term);
            CREATE INDEX CourseCodeIndex ON Course (course_code);
            CREATE INDEX DepartmentIndex ON Course (department);
            CREATE INDEX DepartmentCourseNumberIndex ON Course (department, course_number);
            CREATE INDEX InstructorNameIndex ON Instructor (name);
            """
        )
        print(f"[{asctime()}] Finished creating index")
        connection.commit()
    except sqlite3.Error as error:
        print(f"[{asctime()}] Failed to create index: {error}")
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

def load_data_per_year(workbook: openpyxl.workbook.workbook.Workbook) -> ([(str, int, str, str, str, int, int, int, int, int, int, int, float)], [(str, int, str)]):
    '''Return data in an academic year.'''
    all_courses, all_instructors = [], []
    for quarter in workbook.sheetnames:
        print(f"[{asctime()}] Processing data from {quarter}")
        sheet = workbook[quarter]
        
        for row in range(2, sheet.max_row + 1):
            department = str(sheet["C" + str(row)].value)
            course_number = str(sheet["D" + str(row)].value)
            course_code = int(sheet["E" + str(row)].value)
            course_title = str(sheet["F" + str(row)].value)
            grade_a_count = int(sheet["H" + str(row)].value)
            grade_b_count = int(sheet["I" + str(row)].value)
            grade_c_count = int(sheet["J" + str(row)].value)
            grade_d_count = int(sheet["K" + str(row)].value)
            grade_f_count = int(sheet["L" + str(row)].value)
            grade_p_count = int(sheet["M" + str(row)].value)
            grade_np_count = int(sheet["N" + str(row)].value)
            average_gpa = float(sheet["O" + str(row)].value) if sheet["O" + str(row)].value is not None else 0
            instructors = sheet["G" + str(row)].value.split("; ")
            
            all_courses.append((quarter, course_code, department, course_number, course_title, grade_a_count, grade_b_count, grade_c_count, grade_d_count, grade_f_count, grade_p_count, grade_np_count, average_gpa))
            for instructor in instructors:
                all_instructors.append((quarter, course_code, instructor))

        print(f"[{asctime()}] Finished processing data from {quarter}")
    return all_courses, all_instructors

def insert_data() -> None:
    '''Loop through the spreadsheets to parse and store all the course statistics into data.db.'''
    folder = Path(r"../processed_data")
    connection = sqlite3.connect("../data.db")
    
    try:
        for spreadsheet_path in folder.iterdir():
            print(f"[{asctime()}] Working with the file {spreadsheet_path}")
            courses, instructors = load_data_per_year(openpyxl.load_workbook(str(spreadsheet_path), data_only=True))
            connection.executemany("INSERT INTO Course VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", courses)
            connection.executemany("INSERT INTO Instructor VALUES (?, ?, ?);", instructors)
            connection.commit()
    except sqlite3.Error as error:
        print(f"[{asctime()}] Failed to insert data: {error}")
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

def create_table() -> None:
    '''Create a file named data.db and create two SQL tables.'''
    connection = sqlite3.connect("../data.db")
    try:
        print(f"[{asctime()}] Begin creating table")
        connection.executescript(
            """
            CREATE TABLE Course (
                term TEXT,
                course_code INTEGER,
                department TEXT NOT NULL,
                course_number TEXT NOT NULL,
                course_title TEXT NOT NULL,
                grade_a_count INTEGER NOT NULL,
                grade_b_count INTEGER NOT NULL,
                grade_c_count INTEGER NOT NULL,
                grade_d_count INTEGER NOT NULL,
                grade_f_count INTEGER NOT NULL,
                grade_p_count INTEGER NOT NULL,
                grade_np_count INTEGER NOT NULL,
                gpa_avg REAL NOT NULL,
                CONSTRAINT CoursePrimaryKey PRIMARY KEY (term, course_code)
            );

            CREATE TABLE Instructor (
                term TEXT,
                course_code INTEGER,
                name TEXT,
                CONSTRAINT InstructorPrimaryKey PRIMARY KEY (term, course_code, name),
                CONSTRAINT InstructorTermForeignKey FOREIGN KEY (term) REFERENCES Course(term),
                CONSTRAINT InstructorCourseCodeForeignKey FOREIGN KEY (course_code) REFERENCES Course(course_code) ON DELETE CASCADE
            );
            """
        )
        print(f"[{asctime()}] Finished creating table")
        connection.commit()
    except sqlite3.Error as error:
        print(f"[{asctime()}] Failed to create table: {error}")
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

if __name__ == "__main__":
    create_table()
    insert_data()
    create_index()
