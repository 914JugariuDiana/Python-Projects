from src.domain.Entities import Client
from src.domain.Exceptions import NotUnicIdException, NonExistingIdException
from src.services.Handlers import UndoHandler
from src.services.Undo import UndoManager


class ClientServices:
    def __init__(self, clientsRepository):
        self.__clientsRepository = clientsRepository

    def addClient(self, clientId, name):
        if self.__clientsRepository.findById(clientId) is not None:
            raise NotUnicIdException(clientId)
        newClient = Client(clientId, name)
        UndoManager.registerUndoOperation(self.__clientsRepository, UndoHandler.ADD_ENTITY, newClient)
        self.__clientsRepository.saveInList(newClient)

    def getAllClients(self):
        return self.__clientsRepository.getAll()

    def removeClient(self, clientId):
        if self.__clientsRepository.findById(clientId) is None:
            raise NonExistingIdException(clientId)
        client = self.__clientsRepository.findById(clientId)
        UndoManager.registerUndoOperation(self.__clientsRepository, UndoHandler.DELETE_ENTITY, client)
        self.__clientsRepository.removeFromList(clientId)

    def updateClient(self, clientId, name):
        if self.__clientsRepository.findById(clientId) is None:
            raise NonExistingIdException(clientId)
        client = self.__clientsRepository.findById(clientId)
        UndoManager.registerUndoOperation(self.__clientsRepository, UndoHandler.UPDATE_ENTITY, client)
        updatedClient = Client(clientId, name)
        self.__clientsRepository.updateList(updatedClient)

    def searchClient(self, clientInformation):
        clientsMatchingInformation = []
        for client in self.__clientsRepository.getAll():
            clientData = str(client.id) + str(client.name)
            clientData = clientData.lower()
            if clientData.find(clientInformation) != -1:
                clientsMatchingInformation.append(client)

        return clientsMatchingInformation