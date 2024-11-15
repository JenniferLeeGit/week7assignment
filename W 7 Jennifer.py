import csv

# Step 1: Read the CSV file into Python
total_grades = 0
grade_count = 0

with open('student-mat.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')  # Using semicolon as delimiter
    for row in reader:
        final_grade = int(row['G3'])  # Convert the 'G3' (final grade) to an integer
        total_grades += final_grade  # Sum up the grades
        grade_count += 1  # Count the number of students

# Step 2: Calculate the average grade
average_grade = total_grades / grade_count
print(f"Average final grade: {average_grade:.2f}")
