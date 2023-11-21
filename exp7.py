# Define a list to store records
database = []

# Function to add a record to the database
def add_record(name, age, city):
    record = (name, age, city)
    database.append(record)
    print("Record added successfully!")

# Function to display all records in the database
def display_records():
    print("Database Records:")
    for record in database:
        print("Name: {}, Age: {}, City: {}".format(record[0], record[1], record[2]))

# Example usage
add_record("Alok", 20, "India")
add_record("Ujjwal", 24, "India")
add_record("Rakshit", 21, "India")

display_records()