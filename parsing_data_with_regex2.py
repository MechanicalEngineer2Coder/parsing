import re

def grades():
    file = "C:\\Users\\RemotingRobert\\Desktop\\grades.txt"#Put file location and name here
    with open (file, "r") as file:
        students = file.read()
        #print(students)
        students = students.split("\n")
        grades_list = list()
        for student in students:
            if re.findall("\:\sB", student):
                grades_list.append("{} {}".format(re.findall("[A-Z][a-z]+", student)[0],re.findall("[A-Z][a-z]+", student)[1]))
        print(grades_list)
        print(len(grades_list))
        
grades()
