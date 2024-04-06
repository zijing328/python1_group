#You Li

#fix the problems with each of these classes (1-3)
#(run them to see the traceback)

#1
class MyClass():
    def __init__(self, a, b):
        self.a = 10
        self.b = 20
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x

#2
class MyClass():
    def __init__(self):
        self.a = 10
        self.b = 20
        self.x = self.a + self.b
my_instance = MyClass()
my_instance.x

#3
class MyClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = self.a + self.b
def __init__(self, a, b):
        x = a + b
        return x
my_instance = MyClass(10, 20)
my_instance.x

#4 Create a class to hold all of the courses a student at Harris is enrolled in.
#  - The instance should take two arguments when created; student name, 
#    and student year
#  - At startup, each instance should have an empty list as an attribute 
#    named "enrolled_courses"
#  - Create a method named "enroll" that takes some arguments that describe
#    a course, e.g. name, course number, days, times
#  - When called, make the "enroll" method add a course to the "enrolled_courses"
#    list
#  - Finally, think about what other methods you could add. One to drop a course?
#    One to display the enrolled courses?  Or could you modify "enroll" to make
#    sure times don't overlap, or there aren't too many courses in the list?
#    Work on these if you would like an extra challenge.


class HarrisStudent:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.enrolled_courses = []
    def enroll(self, course):
        if len(self.enrolled_courses) >= 3:
            print('You already enrolled more than 3 courses, need to drop.')
        else:
            self.enrolled_courses.append(course)
            print(f'{course} has been successfully enrolled.')
    def showEnrolledCourses(self):
        for course in self.enrolled_courses:
            print(f'Enrolled courses: {course}')
            
student1 = HarrisStudent('Alice', "Year1")

student1.enroll('STAT1')
student1.enroll('MICRO1')
student1.enroll('AP1')
student1.enroll('AFM')
student1.enroll('CF')

student1.showEnrolledCourses()