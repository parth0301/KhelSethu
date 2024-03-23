from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Endpoint to serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to handle AJAX request from the front-end
@app.route('/get_students', methods=['GET'])
def get_students():
    year = request.args.get('year')
    filtered_students = filter_students_by_year(students, year)
    return jsonify(filtered_students)

# Your existing functions and data
students = [
    {"name": "Athulya", "Sport": "Table Tennis", "academic_year": "Second Year", "email": "athulya@gmail.com", "Ph.No": "5832149756"},
    {"name": "Parth", "Sport": "Cricket", "academic_year": "Third Year", "email": "parth@gmail.com", "Ph.No": "9867549323"},
    {"name": "Ritul", "Sport": "Rink Football", "academic_year": "Fourth Year", "email": "ritul@gmail.com", "Ph.No": "8975649875"},
    {"name": "Anish", "Sport": "Cricket", "academic_year": "First Year", "email": "anish@gmail.com", "Ph.No": "8769054987"},
    {"name": "Adarsh", "Sport": "Rink Football", "academic_year": "Fist Year", "email": "adarsh@gmail.com", "Ph.No": "9086549832"},
    {"name": "Sahil", "Sport": "Table Tennis", "academic_year": "First Year", "email": "sahil@gmail.com", "Ph.No": "8928671746"},
    {"name": "Kshitij", "Sport": "Cricket", "academic_year": "Third Year", "email": "kshitj@gmail.com", "Ph.No": "9365870428"},
    {"name": "Ayaan", "Sport": "Rink Football", "academic_year": "First Year", "email": "ayaan@gmail.com", "Ph.No": "7175648902"},
    {"name": "Kartik", "Sport": "Table Tennis", "academic_year": "First Year", "email": "kartik@gmail.com", "Ph.No": "8098653421"},
    {"name": "Tanvi", "Sport": "Rink Football", "academic_year": "Second Year", "email": "tanvi@gmail.com", "Ph.No": "9987087653"},
    {"name": "Riya", "Sport": "Table Tennis", "academic_year": "Fourth Year", "email": "riya@gmail.com", "Ph.No": "8879076504"},
    {"name": "Smriti", "Sport": "Cricket", "academic_year": "Third Year", "email": "smirit@gmail.com", "Ph.No": "8709532041"},
    {"name": "Arjun", "Sport": "Cricket", "academic_year": "Second Year", "email": "arjun@gmail.com", "Ph.No": "838760924"},
    {"name": "Aditya", "Sport": "Rink Football", "academic_year": "First Year", "email": "aditya@gmail.com", "Ph.No": "9076540923"},
    {"name": "Tripti", "Sport": "Table Tennis", "academic_year": "Third Year", "email": "tripti@gmail.com", "Ph.No": "6098438921"},
    {"name": "Mithul", "Sport": "Cricket", "academic_year": "Fourth Year", "email": "mithul@gmail.com", "Ph.No": "7689086571"},
    {"name": "Salman", "Sport": "Rink Football", "academic_year": "Second Year", "email": "salman@gmail.com", "Ph.No": "9065387291"},
    {"name": "Vinay", "Sport": "Table Tennis", "academic_year": "Third Year", "email": "vinay@gmail.com", "Ph.No": "8097216749"},
]

def filter_students_by_year(students_data, year):
    filtered_students = [student for student in students_data if student['academic_year'] == year]
    return filtered_students

def print_student_details(students_data):
    for student in students_data:
        print("Name:", student["name"])
        print("Sport:", student["Sport"])
        print("Academic Year:", student["academic_year"])
        print("Email:", student["email"])
        print("Phone Number:", student["Ph.No"])
        print()

def main():
    year = input("Enter the academic year (e.g., First Year, Second Year, Third Year, Fourth Year): ")

    filtered_students = filter_students_by_year(students, year)

    if filtered_students:
        print("\nStudents in", year, ":\n")
        print_student_details(filtered_students)
    else:
        print("\nNo students found for the given academic year.")

if __name__ == "__main__":
    main()