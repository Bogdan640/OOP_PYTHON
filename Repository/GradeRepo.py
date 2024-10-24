import pickle

from src.domain.Grade import Grade


class GradeRepository:
    def __init__(self):
        self.__grade_list=[]

    def add(self, grade:Grade):
        self.__grade_list.append(grade)

    def remove_for_discipline(self, id):
        self.__grade_list=[grade for grade in self.__grade_list if grade.discipline_id!=id]

    def remove_for_student(self, id):
        self.__grade_list=[grade for grade in self.__grade_list if grade.student_id!=id]

    def get_list(self):
        return self.__grade_list

    def grade_sample(self):
        import random
        for i in range(1, 11):
            for j in range(1, 4):
                student_id = i
                discipline_id = j
                grade_value = random.randint(10, 100)
                self.__grade_list.append(Grade(student_id, discipline_id, grade_value))




class GradeTextRepository(GradeRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename=filename

    def read_from_file(self):
        self.get_list().clear()
        try:
            file= open(self.__filename, mode='r')
            lines=file.readlines()
            for line in lines:
                elements= line.split(',')
                elements= [element.strip() for element in elements]
                id_stu=int(elements[0])
                id_dis= int(elements[1])
                value= int(elements[2])
                grade=Grade(id_stu, id_dis, value)
                self.get_list().append(grade)

            file.close()

        except EOFError:
            pass
        except FileNotFoundError:
            pass

    def save_file(self):
        with open(self.__filename, mode='w') as file:
            for grade in self.get_list():
                elements=[grade.student_id, grade.discipline_id, grade.grade_value]
                elements= [str(element) for element in elements]
                line= ", ".join(elements)
                file.write(line)

class GradeBinaryRepo(GradeRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename=filename

    def read_from_file(self):
        try:
            with open(self.__filename ,mode='rb') as file:
                while True:
                    grades=pickle.load(file)
                    self.add(grades)
        except EOFError:
            pass
        except FileNotFoundError:
            pass












