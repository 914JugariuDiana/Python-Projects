from src.repository.repository.Repository import Repository
import pickle


class BinaryFileRepository(Repository):
    def __init__(self, fileName, entityClass):
        super().__init__()
        self.__fileName = fileName
        self.__entityClass = entityClass
        self.__loadData()

    def __loadData(self):
        file = open(self.__fileName, "rb")
        entities = pickle.load(file)
        for entity in entities:
            super().saveInList(entity)
        file.close()


    def saveInList(self, entity):
        super().saveInList(entity)
        self.__saveToFile()


    def __saveToFile(self):
        with open(self.__fileName, "wb") as filePointer:
            pickle.dump(super().getAll(), filePointer)


    def removeFromList(self, entityId):
        """
        Function removes an entity from a list of entities
        :param entityId: the id of the entity we want to remove
        :return: None
        """
        super().removeFromList(entityId)
        self.__saveToFile()


    def updateList(self, entity):
        """
        Function "updates" the information of a given entity
        :param entity: the entity we want to update
        :return: None
        """
        super().updateList(entity)
        self.__saveToFile()
