

class Grade:
    def __init__(self, student_id:int, discipline_id:int, grade_value:float):
        self.__student_id=student_id
        self.__discipline_id=discipline_id
        self.__grade_value=grade_value

    @property
    def student_id(self):
        return self.__student_id

    @property
    def discipline_id(self):
        return self.__discipline_id

    @property
    def grade_value(self):
        return self.__grade_value

    @student_id.setter
    def student_id(self, new_id):
        self.__student_id=new_id

    @discipline_id.setter
    def discipline_id(self, new_id):
        self.__discipline_id=new_id

    @grade_value.setter
    def grade_value(self, new_grade):
        self.__grade_value=new_grade


    def __repr__(self):
        return f"Student {self.student_id} , Discipline: {self.discipline_id} , Grade: {self.grade_value}"

