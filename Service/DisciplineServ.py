from src.domain.Discipline import Discipline
from src.services.UndoServ import Command, Operations


class DisciplineService:
    def __init__(self, repository, undo_service, grade_service):
        self.__repository=repository
        self.__undo_service=undo_service
        self.__grade_service=grade_service

    def save_to_file(self):
        try:
            self.__repository.save_file()
        except:
            pass

    def add_discipline(self, id: int, name: str):
        discipline = Discipline(id, name)
        self.__repository.add(discipline)
        undo_command = Command(self.delete_discipline, id)
        redo_command = Command(self.add_discipline, id, name)
        operation = Operations(undo_command, redo_command)
        self.__undo_service.record_for_undo(operation)
        self.save_to_file()

    def delete_discipline(self, id: int):
        deleted_discipline = self.__repository.remove(id)
        undo_command = Command(self.add_discipline, id, deleted_discipline.name)
        redo_Command = Command(self.delete_discipline, id)
        operation = Operations(undo_command, redo_Command)
        self.__undo_service.record_for_undo(operation)

        deleted_grades=[]
        for grade in self.__grade_service.get_list():
            if grade.discipline_id==id:
                deleted_grades.append(grade)
                self.__grade_service.remove_discipline_grades(id)


        # FIXME
    def get_list_serv(self):
        return self.__repository.get_list()

    def sample_serv(self):
        return self.__repository.sample_date_dis()

    def update(self, id:int, name:str):
        discipline=self.__repository.get(id)
        undo_action= Command(self.update, id, discipline.name)
        redo_action= Command(self.update, id, name)
        operation=Operations(undo_action, redo_action)
        self.__undo_service.record_for_undo(operation)
        self.__repository.update(id, Discipline(id, name))
        self.save_to_file()

    def get_student_list(self):
        return self.__repository.get_list()

    def search_discipline_after_name(self, name):
        return self.__repository.find_after_name(name)

    def search_discipline_after_id(self, id):
        return self.__repository.find_after_id(id)


    def load_from_file(self):
        try:
            self.__repository.load_from_file()
        except:
            pass








