from enum import Enum


def addEntityHandler(entityRepository, entity):
    entityRepository.removeFromList(entity.id)


def removeEntityHandler(entityRepository, entity):
    entityRepository.saveInList(entity)


def updateEntityHandler(entityRepository, entity):
    entityRepository.updateList(entity)


class UndoHandler(Enum):
    ADD_ENTITY = addEntityHandler
    DELETE_ENTITY = removeEntityHandler
    UPDATE_ENTITY = updateEntityHandler

class RedoHandler(Enum):
    ADD_ENTITY = removeEntityHandler
    DELETE_ENTITY = addEntityHandler
    UPDATE_ENTITY = updateEntityHandler

    @staticmethod
    def findHandler(entityRepository, undoOperationHandler, entity):
        if undoOperationHandler == removeEntityHandler:
            return RedoHandler.DELETE_ENTITY, entity
        if undoOperationHandler == addEntityHandler:
            return RedoHandler.ADD_ENTITY, entity
        if undoOperationHandler == updateEntityHandler:
            entity = entityRepository.findById(entity.id)
            return RedoHandler.UPDATE_ENTITY, entity