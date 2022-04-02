from dataclasses import dataclass

from src.domain.Exceptions import EmptyListException
from src.services.Handlers import RedoHandler


@dataclass
class UndoOperation:
    targetObject: object
    handler: object
    arguments: object


class UndoManager:
    __undoOperations = []
    __redoOperations = []

    @staticmethod
    def registerUndoOperation(targetObject, handler, arguments):
        UndoManager.__undoOperations.append(UndoOperation(targetObject, handler, arguments))

    @staticmethod
    def registerRedoOperation(targetObject, handler, arguments):
        UndoManager.__redoOperations.append(UndoOperation(targetObject, handler, arguments))

    @staticmethod
    def undo():
        if len(UndoManager.__undoOperations) == 0:
            raise EmptyListException()
        undoOperation = UndoManager.__undoOperations.pop()
        redoOperationHandler, arguments = RedoHandler.findHandler(undoOperation.targetObject, undoOperation.handler, undoOperation.arguments)
        UndoManager.registerRedoOperation(undoOperation.targetObject, redoOperationHandler, arguments)
        undoOperation.handler(undoOperation.targetObject, undoOperation.arguments)

    @staticmethod
    def redo():
        if len(UndoManager.__redoOperations) == 0:
            raise EmptyListException()
        redoOperation = UndoManager.__redoOperations.pop()
        redoOperation.handler(redoOperation.targetObject, redoOperation.arguments)

    @staticmethod
    def emptyUndoList():
        UndoManager.__undoOperations.clear()

    @staticmethod
    def emptyRedoList():
        UndoManager.__redoOperations.clear()
