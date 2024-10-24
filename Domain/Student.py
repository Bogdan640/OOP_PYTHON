
class Student:
    def __init__(self, student_id:int, name:str):
        self.__student_id=student_id
        self.__name=name

    @property
    def id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @id.setter
    def id(self, new_id):
        self.__student_id=new_id

    @name.setter
    def name(self, new_name):
        self.__name=new_name


    def __repr__(self):
        return f"Student id: {self.id},  Name: {self.name}"
