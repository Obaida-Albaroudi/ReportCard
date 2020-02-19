"""
Class that holds the student and all their relevant information. The attributes will hold the information that 
needs to be showcased on the report card and the methods allow for the data to flow in seamlessly. 
"""

class Student:
    def __init__(self, name,student_id):

        # Unique of the student to keep track.
        self.student_id = student_id

        # Name of the student.
        self.name = name
        # This is the average across all the subjects. It will be calculated after we gather the grades in class info
        self.total_average = 0

        # This will hold the the class as the key and the relevant teacher as the value
        self.class_Teacher={}

        # Class info holds the class name as the key and the overall grade of that class as the value
        self.class_Info={}

    
    def add_array_Class_Info(self,grades, classes):
        """
        This function takes in two objects. One representing the grades for each class 
        as the value and the key is the course id. The classes holds the class name and
        the teachers name.
        """

        # Count is meant to keep track of all the keys in grades so we can access them.
        count=[]

        for index in grades:
            count.append(index)

        """
        We are creating and filling in the class_info and class_teacher attributes. 
        We are also removing the first index of count through each iteration
        """
        for class_name in classes:
            self.class_Info[class_name] = grades[count[0]]
            self.class_Teacher[class_name]=classes[class_name]
            count=count[1:]
    

    def calculate_average(self):
        """
        This takes in no arguments and just calculates the average when called. Important note is that we use try in case
        the student is missing some exames in the classes they may have registered in.
        """
        for information in self.class_Info:
            try:

                self.total_average+=self.class_Info[information]
            except:
                continue
        self.total_average= round(self.total_average/len(self.class_Info),2)


