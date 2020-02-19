"""
The goal of this file is to allow us to store the data accordingly. By storing the data we are then able to maneuver 
and grab what we need when we need it. The structure of this class also allows us to search for data fast, 
especially since we are using objects to store the data and not lists. 

Each of the attributes will hold data for one of the csv files.
"""

class Graph:
    def __init__(self):

        # Stores the Student csv file
        self.students={}

        # Stores the Marks csv file
        self.mark={}

        # Stores the Tests csv file
        self.tests={}

        # Stores the Courses csv file
        self.courses={}

    def add_students(self, ID,student):
        """
        Adding the student name as key and the ID as the value
        """
        self.students[student] = ID

    def add_mark(self, test_id,student_id, mark):
        """
        Saving a tuple of the test id and student id. This was effective in making sure we had unique keys and were able to access each datapoint in the test csv. This is also where we set the student id and mark as the values in an object.
        """
        self.mark[(test_id,student_id)] = {"student_id":student_id,"mark":mark}

    def add_tests(self, test_id, course_id, weight):
        """
        """
        self.tests[test_id] = {"course_id":course_id, "weight":weight}

    def add_courses(self, course_id, name, teacher):
        """
        """
        self.courses[course_id] = {"name":name, "teacher":teacher}
    
    def calculate_grade(self, student_id):
        """
        """
        weightArr={}
        grades={}
        classes={}
        for test_id in self.mark:
            if int(self.mark[test_id]["student_id"]) == student_id:  
                if self.tests[test_id[0]]["course_id"] in weightArr:
                      weightArr[self.tests[test_id[0]]["course_id"]]+=int(self.tests[test_id[0]]["weight"])
                else:
                    weightArr[self.tests[test_id[0]]["course_id"]]=int(self.tests[test_id[0]]["weight"])
                if self.tests[test_id[0]]["course_id"] in grades:
                    grades[self.tests[test_id[0]]["course_id"]] += float(self.mark[test_id]["mark"])*float(self.tests[test_id[0]]["weight"])/100
                else:
                    grades[self.tests[test_id[0]]["course_id"]]= float(self.mark[test_id]["mark"])*float(self.tests[test_id[0]]["weight"])/100
                    classes[self.courses[self.tests[test_id[0]]["course_id"]]["name"]]=self.courses[self.tests[test_id[0]]["course_id"]]["teacher"]

        return [grades,classes,weightArr]