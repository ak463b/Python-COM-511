def create_student_record(name, roll_number, marks):
    return {'Name': name, 'Roll Number': roll_number, 'Marks': marks}

def search_student(records, key, value):
    for record in records:
        if record[key] == value:
            return record
    return None

# Example usage:
student_records = []

# Adding some sample records
student_records.append(create_student_record('Alice', '001', 90))
student_records.append(create_student_record('Bob', '002', 85))
student_records.append(create_student_record('Charlie', '003', 92))

# Searching for a student by name
search_name = input("Enter the name of the student to search: ")
found_student_name = search_student(student_records, 'Name', search_name)

# Searching for a student by roll number
search_roll_number = input("Enter the roll number of the student to search: ")
found_student_roll = search_student(student_records, 'Roll Number', search_roll_number)

# Searching for a student by marks
search_marks = int(input("Enter the marks of the student to search: "))
found_student_marks = search_student(student_records, 'Marks', search_marks)

# Displaying results
print("\nSearch by Name:")
if found_student_name:
    print("Student found!")
    print("Name: ", found_student_name['Name'])
    print("Roll Number: ", found_student_name['Roll Number'])
    print("Marks: ", found_student_name['Marks'])
else:
    print("Student not found.")

print("\nSearch by Roll Number:")
if found_student_roll:
    print("Student found!")
    print("Name: ", found_student_roll['Name'])
    print("Roll Number: ", found_student_roll['Roll Number'])
    print("Marks: ", found_student_roll['Marks'])
else:
    print("Student not found.")

print("\nSearch by Marks:")
if found_student_marks:
    print("Student found!")
    print("Name: ", found_student_marks['Name'])
    print("Roll Number: ", found_student_marks['Roll Number'])
    print("Marks: ", found_student_marks['Marks'])
else:
    print("Student not found.")