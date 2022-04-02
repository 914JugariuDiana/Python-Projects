from configparser import ConfigParser

from src.domain.Entities import Book, Client, Rental
from src.repository.binaryFileRepository.BinaryFileRepository import BinaryFileRepository
from src.repository.repository.Repository import Repository
from src.repository.textFileRepository.TextFileRepository import TextFileRepository


class Settings:
    def __init__(self):
        parser = ConfigParser()
        parser.read(r'C:\Users\Mihai\Documents\A9\src\settings\setting.properties')
        self._repositoryType = parser.get('options', 'repository')
        self._bookFile = parser.get('options', 'book')
        self._clientFile = parser.get('options', 'client')
        self._rentalFile = parser.get('options', 'rental')

    def setRepository(self):
        if self._repositoryType == "in-memory":
            bookRepository = Repository()
            clientRepository = Repository()
            rentalRepository = Repository()
            return bookRepository, clientRepository, rentalRepository
        if self._repositoryType == "text-file":
           bookRepository = TextFileRepository(self._bookFile, Book)
           clientRepository = TextFileRepository(self._clientFile, Client)
           rentalRepository = TextFileRepository(self._rentalFile, Rental)
           return bookRepository, clientRepository, rentalRepository
        if self._repositoryType == "binary-file":
            bookRepository = BinaryFileRepository(self._bookFile, Book)
            clientRepository = BinaryFileRepository(self._clientFile, Client)
            rentalRepository = BinaryFileRepository(self._rentalFile, Rental)
            return bookRepository, clientRepository, rentalRepository

    def getRepositoryType(self):
        return self._repositoryType
