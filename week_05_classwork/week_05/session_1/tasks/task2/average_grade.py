# Step 1: Open a file called 'student_data.csv' to read each student's grades.
# hint: skip the header row with data[1:]
# hint: you could handle file errors with try/except
def read_student_data(filename):
    students = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()[1:]  
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) != 5:
                    continue  
                _, name, maths, science, history = parts                
# Step 2: Read each student's grades and calculate their average grade           
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3
               try:
                    
                    avg = (int(maths) + int(science) + int(history)) / 3
                    students.append({'name': name, 'average': avg})
               except ValueError:
                    continue  
# Step 3: Sort the students by their average grade in descending order.
# hint: you might want to store each student as a dictionary with name and average
# hint: use the sorted() function with a key parameter, or list.sort()
def sort_students_by_average(students):  
    return sorted(students, key=lambda x: x['average'], reverse=True)
# Step 4: Open a file called 'report.txt'
# Write each student's name and their average grade to the report in order
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
def write_report(students, output_file):    
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("grade report\n")
            for student in students:
                file.write(f"{student['name']}: {student['average']:.2f}\n")
        print(f" '{output_file}'")
    except Exception as e:
        print(f"Error:{e}")

if __name__ == "__main__":
    input_file = "student_data.csv"
    output_file = "report.txt"

    student_data = read_student_data(input_file)
    if student_data:
        sorted_students = sort_students_by_average(student_data)
        write_report(sorted_students, output_file)
