from src.domain.Entities import Book
from src.domain.Exceptions import NotUnicIdException, NonExistingIdException
from src.services.Handlers import UndoHandler
from src.services.Undo import UndoManager


class BookServices:
    def __init__(self, booksRepository):
        self.__booksRepository = booksRepository

    def addBook(self, bookId, title, author):
        if self.__booksRepository.findById(bookId) is not None:
            raise NotUnicIdException(bookId)
        newBook = Book(bookId, title, author)
        UndoManager.registerUndoOperation(self.__booksRepository, UndoHandler.ADD_ENTITY, newBook)
        self.__booksRepository.saveInList(newBook)

    def getAllBooks(self):
        return self.__booksRepository.getAll()

    def removeBook(self, bookId):
        if self.__booksRepository.findById(bookId) is None:
            raise NonExistingIdException(bookId)
        book = self.__booksRepository.findById(bookId)
        UndoManager.registerUndoOperation(self.__booksRepository, UndoHandler.DELETE_ENTITY, book)
        self.__booksRepository.removeFromList(bookId)

    def updateBook(self, bookId, title, author):
        if self.__booksRepository.findById(bookId) is None:
            raise NonExistingIdException(bookId)
        book = self.__booksRepository.findById(bookId)
        UndoManager.registerUndoOperation(self.__booksRepository, UndoHandler.UPDATE_ENTITY, book)
        updatedBook = Book(bookId, title, author)
        self.__booksRepository.updateList(updatedBook)

    def searchBook(self, bookInformation):
        booksMatchingInformation = []
        for book in self.__booksRepository.getAll():
            bookData = str(book.id) + str(book.title) + str(book.author)
            bookData = bookData.lower()
            if bookData.find(bookInformation) != -1:
                booksMatchingInformation.append(book)

        return booksMatchingInformation