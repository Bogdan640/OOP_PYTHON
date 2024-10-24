import pickle

from src.domain.Discipline import Discipline

class DisciplineRepository:
    def __init__(self):
        self.__discipline_list=[]

    def add(self, discipline:Discipline):
        self.__discipline_list.append(discipline)

    def get(self, id):
        for discipline in self.__discipline_list:
            if discipline.id==id:
                return discipline


    def remove(self, id):
            self.__discipline_list= [discipline for discipline in self.__discipline_list if discipline.id==id ]

    def update(self,id, new_discipline:Discipline):
        for discipline in self.__discipline_list:
            if discipline.id==id:
                discipline.name=new_discipline.name
                discipline.id=new_discipline.id

    def get_list(self):
        return self.__discipline_list

    def sample_date_dis(self):
        for id in range(1,6):
            self.__discipline_list.append(Discipline(id, f"Discipline {id}"))

    def get_len_list(self):
        return self.__discipline_list

    def find_after_id(self, id):
        for discipline in self.__discipline_list:
            if discipline.id==id:
                return discipline

    def find_after_name(self, name):
        new_list = [discipline for discipline in self.get_list() if name.lower() in discipline.name.lower()]
        return new_list





class DisciplineTextRepo(DisciplineRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename=filename


    def load_from_file(self):
        self.get_list().clear()
        try:
            file= open(self.__filename, mode ='r')
            discipline_list=[]
            lines=file.readlines()
            for line in lines:
                elements= line.split(',')
                elements= [element.strip() for element in elements]
                id=int(elements[0])
                name= elements[1]
                discipline=Discipline(id, name)
                discipline_list.append(discipline)
            file.close()
            return discipline_list
        except EOFError:
            pass
        except FileNotFoundError:
            pass


    def save_file(self):
        with open(self.__filename, mode='w') as file:
            for discipline in self.get_list():
                elements=[discipline.id, discipline.name]
                elements= [str(element) for element in elements]
                line= ", ".join(elements) + '\n'
                file.write(line)





class DisciplineBinaryRepo(DisciplineRepository):
    def __init__(self, filename):
        super().__init__()
        self.__filename=filename

    def read_from_file(self):
        try:
            with open(self.__filename, mode='rb') as file:
                while True:
                    disciplines=pickle.load(file)
                    self.add(disciplines)
        except EOFError:
            pass
        except FileNotFoundError:
            pass


    def save_file(self):
        with open(self.__filename, mode='wb') as file:
            for discipline in self.get_list():
                pickle.dump(discipline, file)











