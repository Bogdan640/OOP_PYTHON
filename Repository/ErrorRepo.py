

class RepositoryError(Exception):
    def __init__(self, message):
        self.__message=message

    @property
    def message(self):
        return self.__message

    def __str__(self):
        return "Repository error: " + str(self.__message)


class UndoException(RepositoryError):
    def __init__(self):
        RepositoryError.__init__(self, "There is nothing left to undo.")

class RedoException(RepositoryError):
    def __init__(self):
        RepositoryError.__init__(self, "There is nothing left to redo.")


