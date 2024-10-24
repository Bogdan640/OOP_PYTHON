from src.domain.Student import Student
from src.repository.StudentRepo import StudentRepository
from src.services.UndoServ import UndoService, Command, Operations


class StudentServ:
    def __init__(self, repository, undo_service, grade_service):
        self.__repository=repository
        self.__undo_service=undo_service
        self.__grade_service=grade_service

    def save_to_file(self):
        try:
            self.__repository.save_file()
        except:
            pass

    def add_student(self, id:int, name:str):
        student=Student(id, name)
        self.__repository.add(student)
        undo_command=Command(self.delete_student, id)
        redo_command= Command(self.add_student, id, name )
        operation=Operations(undo_command, redo_command)
        self.__undo_service.record_for_undo(operation)
        self.save_to_file()

    def delete_student(self, id:int):
        deleted_student= self.__repository.remove(id)
        undo_command= Command(self.add_student, id, deleted_student.name)
        redo_Command =Command(self.delete_student, id)
        operation=Operations(undo_command, redo_Command)
        self.__undo_service.record_for_undo(operation)

        deleted_grades=[]
        for grade in self.__grade_service.get_list():
            if grade.student_id == id:
                deleted_grades.append(grade)
                self.__grade_service.remove_student_grades(id)

        #list=self.__grade_service.get_specific_grades(id)
        #self.__repository.

        #FIXME

    def sample_list_s(self):
        self.__repository.sample_data()

    def display_list_s(self):
         return self.__repository.display_list()


    def update(self, id:int, name:str):
        student=self.__repository.get(id)
        undo_action= Command(self.update, id, student.name)
        redo_action= Command(self.update, id, name)
        operation=Operations(undo_action, redo_action)
        self.__undo_service.record_for_undo(operation)
        self.__repository.update_student(Student(id, name))
        self.save_to_file()

    def get_student_list(self):
        return self.__repository.get_list()


    def search_students_name(self, given_name):
        new_list=[student for student in self.get_student_list() if given_name.lower() in student.name.lower()]
        return new_list


    def search_student_id(self, id):
        return self.__repository.find_after_id(id)

    def load_from_file(self):
        try:
            self.__repository.read_from_file()
        except:
            pass









