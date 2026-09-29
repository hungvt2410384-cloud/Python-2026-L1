import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}
        self.__gpa = 0.0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def add_mark(self, course_id, mark):
        self.__marks[course_id] = math.floor(mark * 10) / 10.0

    def get_marks(self):
        return self.__marks

    def calculate_gpa(self, courses):
        if not self.__marks:
            self.__gpa = 0.0
            return self.__gpa

        marks_list = []
        credits_list = []

        for course in courses:
            c_id = course.get_id()
            if c_id in self.__marks:
                marks_list.append(self.__marks[c_id])
                credits_list.append(course.get_credits())

        if not marks_list:
            self.__gpa = 0.0
            return self.__gpa

        marks_arr = np.array(marks_list)
        credits_arr = np.array(credits_list)

        self.__gpa = round(np.sum(marks_arr * credits_arr) / np.sum(credits_arr), 2)
        return self.__gpa

    def get_gpa(self):
        return self.__gpa