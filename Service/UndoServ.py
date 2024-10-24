from src.repository.ErrorRepo import UndoException, RedoException

class Command:
    def __init__(self, fn, *fn_args):
        self._fn=fn
        self._fn_parameters=fn_args

    def execute(self):
        self._fn(*self._fn_parameters)

    def __str__(self):
        return "Function: " + str(self._fn) + "with parameters: " + str(self._fn_parameters)

class Operations:
    def __init__(self, undo_action:Command, redo_action: Command):
        self.__undo_action=undo_action
        self.__redo_action=redo_action

    def undo(self):
        self.__undo_action.execute()

    def redo(self):
        self.__redo_action.execute()

    def __str__(self):
        return "Functions: " + str(self.__undo_action) + "& " + str(self.__redo_action)

class UndoService:
    def __init__(self):
        self.__undo_stack=[]
        self.__redo_stack=[]
        self.__mode_undo=False

    def record_for_undo(self, operation:Operations):
        if self.__mode_undo:
            return
        self.__undo_stack.append(operation)

    def undo(self):
        if len(self.__undo_stack)==0:
            raise UndoException
        self.__mode_undo=True
        operation=self.__undo_stack.pop()
        operation.undo()
        self.__redo_stack.append(operation)
        self.__mode_undo=False

    def redo(self):
        if len(self.__redo_stack)==0:
            raise RedoException
        self.__mode_undo=True
        operation=self.__undo_stack.pop()
        operation.redo()
        self.__undo_stack.append(operation)
        self.__mode_undo=False

    def __str__(self):
        op_str = 'UNDO stack\n'
        for nr_op, op in enumerate(self.__undo_stack):
            op_str += str(nr_op) + " "
            op_str += str(op)
            op_str += '\n'

        op_str += 'REDO stack\n'
        for nr_op, op in enumerate(self.__redo_stack):
            op_str += str(nr_op) + " "
            op_str += str(op)
            op_str += '\n'

        return op_str






