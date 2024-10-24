import pickle

from src.domain.Student import Student


class StudentRepository:
    def __init__(self):
        self.__student_list=[]

    def sample_data(self):
        for id in range(1, 21):
            self.__student_list.append(Student(id, f"Student {id}"))

    def add(self, student):
        self.__student_list.append(student)

    def display_list(self):
        return self.__student_list


    def remove(self, id:int):
        deleted_student=None
        for student in self.__student_list:
            if student.id==id:
                deleted_student=student
                break

        self.__student_list=[student for student in self.__student_list if student.id!=id]
        return  deleted_student

    def find_after_id(self, id):
        for student in self.__student_list:
            if student.id==id:
                return student

    # def find_after_name(self, name):
    #     for student in self.__student_list:
    #         print(student.name.lower(), type(student.name.lower()), name.lower())
    #     new_list= [student for student in self.__student_list if name.lower() in student.name.lower()]
    #     for student in new_list:
    #         print(student)

    def update_student(self ,new_student: Student):
        student = self.find_after_id(new_student.id)
        student.name=new_student.name
        student.id=new_student.id

    def get_list(self):
        return self.__student_list

    def get_len_list(self):
        return len(self.__student_list)

    def get(self, id):
        for student in self.__student_list:
            if student.id==id:
                return student



class SdudentTextRepo(StudentRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename=filename

    def read_from_file(self):
        self.get_list().clear()
        try:
            file = open(self.__filename, mode='r')
            lines = file.readlines()
            for line in lines:
                elements = line.split(',')
                elements = [element.strip() for element in elements]
                id = int(elements[0])
                name = elements[1]
                student = Student(id, name)
                self.get_list().append(student)
            file.close()
        except EOFError:
            pass
        except FileNotFoundError:
            pass

    def save_file(self):
        with open(self.__filename, mode='w') as file:
            for student in self.get_list():
                student_elements = [student.id, student.name]
                student_elements = [str(element) for element in student_elements]
                line = ", ".join(student_elements) + '\n'
                file.write(line)


class StudentBinaryRepo(StudentRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename=filename

    def read_from_file(self):
        try:
            with open(self.__filename, mode='rb') as file:
                while True:
                    students=pickle.load(file)
                    self.add(students)
        except EOFError:
            pass
        except FileNotFoundError:
            pass

    def save_file(self):
        with open(self.__filename, mode='wb') as file:
            for student in self.get_list():
                pickle.dump(student, file)

























