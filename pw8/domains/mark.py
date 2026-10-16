import math

class Mark:
    def __init__(self, student_id, course_id, mark_value):
        self.__student_id = student_id
        self.__course_id = course_id
        self.__mark_value = math.floor(mark_value * 10) / 10

    def get_student_id(self):
        return self.__student_id

    def get_course_id(self):
        return self.__course_id

    def get_mark_value(self):
        return self.__mark_value