# Open the file in write mode
with open("My File.txt", "w") as file:
    # Prompt the user for three lines of input
    line1 = input("Enter the first line: ")
    line2 = input("Enter the second line: ")
    line3 = input("Enter the third line: ")

    # Write the input lines to the file
    file.write(line1 + "\n")
    file.write(line2 + "\n")
    file.write(line3 + "\n")

print("Lines written to 'My File.txt' successfully.")