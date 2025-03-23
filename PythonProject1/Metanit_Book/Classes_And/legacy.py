class Employee:
    def do(self):
        print("Employee works")


class Student:
    def do(self):
        print("Student studies")


# class WorkingStudent(Student,Employee):
class WorkingStudent(Employee, Student):
    pass
# if we have 2 metods do in inherited classes, викличиться за замовченням метод з першого наслід класу
#

tom = WorkingStudent()
tom.do()  # ?

print(WorkingStudent.mro())