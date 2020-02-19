import csv 
from Student import Student 


students = "students.csv"
marks = "marks.csv"
tests = "tests.csv"
courses = "courses.csv"

all_Students=[]

fields = [] 
rows = [] 

students_store=[]
marks_store=[]
tests_store=[]
courses_store=[]

# reading csv file 
with open(students, 'r') as csvfile: 
    # creating a csv reader object 
    students_read = csv.reader(csvfile)
    marks_read = csv.reader(open(marks, 'r')) 
    tests_read = csv.reader(open(tests, 'r')) 
    courses_read = csv.reader(open(courses, 'r')) 



    # extracting field names through first row 
    next(students_read) 
    next(marks_read)
    next(tests_read)
    next(courses_read)

    for student_row in students_read:
        students_store.append(student_row) 

    for marks_row in marks_read:
        marks_store.append(marks_row)
             
    for test_row in tests_read:
        tests_store.append(test_row)

    for course_row in courses_read:
        courses_store.append(course_row)

for student_row in students_store: 
    student=Student(student_row[0],student_row[1])
    for marks_row in marks_store:
        if student_row[0]==marks_row[1]:
            
            for test_row in tests_store:
                if marks_row[0]==test_row[0]:
                
                    for course_row in courses_store:
                        if test_row[1]==course_row[0]:                           
                            mark_int=float(marks_row[2])
                            test_int=float(test_row[2])/100
                            student.add_array_Class_Info(mark_int,test_int,course_row[1],course_row[2])
    student.calculate_average()
    all_Students.append(student)


      
for i in all_Students:
    print("student_id", i.student_id, "name",i.name,"total_average",i.total_average, "class_Teacher",i.class_Teacher, "class_Info",i.class_Info)
  


with open("reportCard.txt", "w") as reportCard:
    for stud in all_Students:
        reportCard.write(f"Student Id:{ stud.student_id}, name: {stud.name}\n")
        reportCard.write(f"Total Average:   {stud.total_average}%\n\n")
        for Class in stud.class_Teacher:
            reportCard.write(f"\t\tCourse:{Class} , Teacher: {stud.class_Teacher[Class]}\n")
            reportCard.write(f"\t\tFinal Grade:   {stud.class_Info[Class]}0%\n\n\n")
    reportCard.close()