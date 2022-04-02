from src.sortFilter.IterableDataStructure import IterableDataStructure


class Repository:
    def __init__(self):
        self.__entities = IterableDataStructure()

    def findById(self, entityId):
        """
        Function finds an entity in a list of entities
        :param entityId: the id of the element we are looking for
        :return: the entity if we find it in the list
        """
        for entity in self.getAll():
            if entity.id == entityId:
                return entity
        return None

    def saveInList(self, entity):
        """
        Function saves an entity in a the list of entities
        :param entity: the entity we want to save
        :return: None
        """
        self.__entities.append(entity)

    def getAll(self):
        return self.__entities

    def removeFromList(self, entityId):
        """
        Function removes an entity from a list of entities
        :param entityId: the id of the entity we want to remove
        :return: None
        """
        entity = self.findById(entityId)
        self.__entities.remove(entity)

    def updateList(self, entity):
        """
        Function "updates" the information of a given entity
        :param entity: the entity we want to update
        :return: None
        """
        oldEntity = self.findById(entity.id)
        self.removeFromList(oldEntity.id)
        self.saveInList(entity)

    def findHighestIdInList(self):
        maximumId = 0

        for entity in (self.getAll()):
            if entity.id > maximumId:
                maximumId = entity.id

        return maximumId




