from src.repository.repository.Repository import Repository


class TextFileRepository(Repository):
    def __init__(self, fileName, entityClass):
        super().__init__()
        self.__fileName = fileName
        self.__entityClass = entityClass
        self.__loadData()

    def __loadData(self):
        with open(self.__fileName) as filePointer:
            for line in filePointer:
                line = line.strip()
                entity = self.__entityClass.readFrom(line)
                super().saveInList(entity)
        filePointer.close()

    def saveInList(self, entity):
        super().saveInList(entity)
        self.__saveToFile()

    def __saveToFile(self):
        with open(self.__fileName, "wt") as filePointer:
            enitiesList = super().getAll()
            for entity in enitiesList:
                filePointer.write(entity.__repr__() + '\n')
        filePointer.close()

    def removeFromList(self, entityId):
        super().removeFromList(entityId)
        self.__saveToFile()

    def updateList(self, entity):
        super().updateList(entity)
        self.__saveToFile()

