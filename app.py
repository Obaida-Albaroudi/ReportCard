import csv 
from Student import Student 
from graph import Graph


"""
We run the application in this file
"""

# We give each of our four csv files a unique name so that it is easier to access.

students = "students.csv"
marks = "marks.csv"
tests = "tests.csv"
courses = "courses.csv"


# Array that will hold each of the students in the class
all_Students=[]


# We instantiate our Graph here. The overall goal with this is to be able to store the data from  the csv files in an effective way without needing to do multiple nested for loops. More information about the details of this class can be found in the graph class.

graphs = Graph()

# This is allowind us to read the csv files so we can access the data and pass them into the graph ZipFile The class for reading and writing ZIP files.  See section                
with open(students, 'r') as csvfile: 
    # creating a csv reader object 
    students_read = csv.reader(csvfile)
    marks_read = csv.reader(open(marks, 'r')) 
    tests_read = csv.reader(open(tests, 'r')) 
    courses_read = csv.reader(open(courses, 'r')) 

    #The next here allows us to skip the first rows of each table as we know what those are and  we only need to access the data in the rest of the csv files.
    next(students_read) 
    next(marks_read)
    next(tests_read)
    next(courses_read)

    #For looping through each of the rows found in each of the csv files and filling in the graph class accordingly.

    for student_row in students_read:
        graphs.add_students(student_row[0], student_row[1])

    for marks_row in marks_read:
        graphs.add_mark(marks_row[0], marks_row[1], marks_row[2])
             
    for test_row in tests_read:
        graphs.add_tests(test_row[0], test_row[1], test_row[2])

    for course_row in courses_read:
        graphs.add_courses(course_row[0], course_row[1], course_row[2])


#This is where we grab the Id of each student found in the array idOrder in graphs. The array is sorted ensuring we are looking at the students in order of their id.We pass in the ID and the name of the student into the student class. We then use the calculate method to receive back all the relevant information for that specific student and add this information to the student class. Afterwards we calculate the average  and append the student to the array of overall students we defined at the top of this file. (The methods are expanded on in their respective files)
for ID in graphs.idOrder:
    student=Student(graphs.studentsId[f"{ID}"],ID)
    calculations= graphs.calculate_grade(ID)
    for i in calculations[0]:
        if calculations[2][i] !=100:
            calculations[0][i]= "Weight does not equal 100. Error!!"

    student.add_array_Class_Info(calculations[0],calculations[1])
    student.calculate_average()
    all_Students.append(student)


# We are opening up the reportCard text file and filling out the information accordingly. We for loop through the arrray of students then fill in the information of each student. This information is stored in the students attributes.
with open("reportCard.txt", "w") as reportCard:
    for stud in all_Students:
        reportCard.write(f"Student Id: { stud.student_id}, name: {stud.name}\n")
        reportCard.write(f"Total Average:   {stud.total_average}%\n\n")
        for Class in stud.class_Teacher:
            reportCard.write(f"\t\tCourse: {Class}, Teacher: {stud.class_Teacher[Class]}\n")
            reportCard.write(f"\t\tFinal Grade:   {stud.class_Info[Class]}0%\n\n\n")
    reportCard.close()

