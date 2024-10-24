

class Discipline:
    def __init__(self, discipline_id:int, name:str):
        self.__discipline_id=discipline_id
        self.__name=name
    @property
    def id(self):
        return self.__discipline_id
    @property
    def name(self):
        return self.__name

    @id.setter
    def id(self, new_id):
        self.__discipline_id=new_id

    @name.setter
    def name(self, new_name):
        self.__name=new_name

    def __repr__(self):
        return f"Discipline id: {self.id} , Name: {self.name}"


