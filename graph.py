from decimal import Decimal

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

        #To be able to access the name of students from their ids.
        self.studentsId={}

        # Stores the Marks csv file
        self.mark={}

        # Stores the Tests csv file
        self.tests={}

        # Stores the Courses csv file
        self.courses={}
        
        # Store the id's and sort so that it is from first to last
        self.idOrder=[]

    def add_students(self, ID,student):
        """
        Adding the student name as key and the ID as the value
        """
        self.students[student] = ID
        self.studentsId[ID] = student
        
        self.idOrder.append(int(ID))
        self.idOrder.sort()
      


    def add_mark(self, test_id,student_id, mark):
        """
        Saving a tuple of the test id and student id. This was effective in making sure we had unique keys 
        and were able to access each datapoint in the test csv. This is also where we set the student id 
        and mark as the values in an object.
        """
        self.mark[(test_id,student_id)] = {"student_id":student_id,"mark":mark}

    def add_tests(self, test_id, course_id, weight):
        """
        The test id alone is the key in this case as each id is unique. The values are the course id and weight also in an object.
        """
        self.tests[test_id] = {"course_id":course_id, "weight":weight}

    def add_courses(self, course_id, name, teacher):
        """
        The course id is the key and the name and teacher are the values in an object.
        """
        self.courses[course_id] = {"name":name, "teacher":teacher}
    
    def calculate_grade(self, student_id):
        """
        This is taking the student id as an input and is returning an array of three objects. The first object is the overall grades associated with each course id. In grades the key is the course id and the final score is the value. The second array is the classes which has the key as the course name and the value as the teachers name. The last object is the course id as the key and the overall weight per course as the value.
        """
        
        # The goal with this object is to check and see if a student fulfills the requirement to meet 100 for the weights of each of the classes they are enrolled in. 
        weightArr={}
        grades={}
        classes={}

        # We for loop through self.mark and use this as our launching pad since we can access this information first based off of the relationships that the csv files have with one another.
        for test_id in self.mark:

            # We check to ensure that the id we are looking at in self.mark matches up with the student we are looking into
            if int(self.mark[test_id]["student_id"]) == student_id:  

                # If the course id is in weightArr all we do is add the weight to the existing value found there if not create a new key value pair.
                if self.tests[test_id[0]]["course_id"] in weightArr:
                      weightArr[self.tests[test_id[0]]["course_id"]]+=int(self.tests[test_id[0]]["weight"])
                else:
                    weightArr[self.tests[test_id[0]]["course_id"]]=int(self.tests[test_id[0]]["weight"])
                 
                #If the course id is in grades all we do is add the mark * weight to the existing value found there to reach the final grade of a course. if not create a new key value pair for both the grades and classes object.
                if self.tests[test_id[0]]["course_id"] in grades:
                    total=Decimal(self.mark[test_id]["mark"])*Decimal(self.tests[test_id[0]]["weight"])/Decimal(100)
                    grades[self.tests[test_id[0]]["course_id"]] += total
            
                else:
                    total=Decimal(self.mark[test_id]["mark"])*Decimal(self.tests[test_id[0]]["weight"])/Decimal(100)
                    grades[self.tests[test_id[0]]["course_id"]]= total
                    classes[self.courses[self.tests[test_id[0]]["course_id"]]["name"]]=self.courses[self.tests[test_id[0]]["course_id"]]["teacher"]
        return [grades,classes,weightArr]