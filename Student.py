class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.total_average = 0
        self.class_Teacher={}
        self.class_Info={}

    
    def add_array_Class_Info(self,mark,weight,class_name,name):

        if class_name in self.class_Info:
            self.class_Info[class_name] += round(mark*weight,2)

        else:

            self.class_Info[class_name] = round(mark*weight,2)
            self.class_Teacher[class_name]=name
    
    def calculate_average(self):
        for information in self.class_Info:
            self.total_average+=self.class_Info[information]
        self.total_average= round(self.total_average/len(self.class_Info),2)


