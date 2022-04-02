from datetime import datetime
from src.domain.Entities import Rental
from src.domain.Exceptions import RentalException, RentalExceptionUnavailableRantal, NotUnicIdException, \
    NonExistingIdException
from src.domain.Validators import ValidateDate
from src.services.Handlers import UndoHandler
from src.services.Undo import UndoManager


class RentalServices:
    def __init__(self, rentalsRepository, booksRepository, clientsRepository):
        self.__rentalsRepository = rentalsRepository
        self.__booksRepository = booksRepository
        self.__clientsRepository = clientsRepository

    def checkBookAvailability(self, bookIdToCheck):
        for rental in self.getAllRentals():
            if rental.bookId == bookIdToCheck and rental.returnedDate == '0':
                return rental
        return None

    def addRental(self, rentalId, bookId, clientId, rentedDate, returnedDate):
        if self.__rentalsRepository.findById(rentalId) is not None:
            raise NotUnicIdException(rentalId)
        if ValidateDate.validateDate(rentedDate):
            pass
        if self.checkBookAvailability(bookId) is None:
            newRental = Rental(rentalId, bookId, clientId, rentedDate, returnedDate)
            UndoManager.registerUndoOperation(self.__rentalsRepository, UndoHandler.ADD_ENTITY, newRental)
            self.__rentalsRepository.saveInList(newRental)
        else:
            raise RentalException(bookId)

    def updateRental(self, rentalId, returnDate):
        if self.__rentalsRepository.findById(rentalId) is None:
            raise NonExistingIdException(rentalId)
        rental = self.__rentalsRepository.findById(rentalId)
        if rental is not None:
            rental = self.__rentalsRepository.findById(rentalId)
            UndoManager.registerUndoOperation(self.__rentalsRepository, UndoHandler.UPDATE_ENTITY, rental)
            updatedRental = Rental(rental.id, rental.bookId, rental.clientId, rental.rentedDate, returnDate)
            self.__rentalsRepository.updateList(updatedRental)
        else:
            raise RentalExceptionUnavailableRantal(rentalId)

    def booksStatistics(self):
        """
        Function looks through rentals list and memorizes the number of apparitions of every book then creates a new
        list with the books in the order of their popularity.
        :return: a list containing all the books in the order of their popularity
        """
        maximBookId = self.__booksRepository.findHighestIdInList()
        rentalsList = self.getAllRentals()
        booksList = self.__booksRepository.getAll()
        numberOfTimesBooksWereRented = []
        topRentedBooks = []

        for position in range(0, maximBookId + 1):
            if self.__booksRepository.findById(position) is None:
                numberOfTimesBooksWereRented.append(-1)
            else:
                numberOfTimesBooksWereRented.append(0)

        for rental in (rentalsList):
            numberOfTimesBooksWereRented[rental.bookId] = numberOfTimesBooksWereRented[rental.bookId] + 1

        for position in range(1, len(booksList) + 1):
            maximOfTimesBookWasRented = max(numberOfTimesBooksWereRented)
            bookPosition = numberOfTimesBooksWereRented.index(maximOfTimesBookWasRented)
            numberOfTimesBooksWereRented[bookPosition] = -1
            book = str(self.__booksRepository.findById(bookPosition))
            topRentedBooks.append(book)

        return topRentedBooks

    def authorsStatistics(self):
        """
        Function looks through rentals list and memorizes the number of apparitions of every author then creates a new
        list with the authors in the order of their popularity.
        :return: a list containing all the authors in the order of their popularity
        """
        rentalsList = self.getAllRentals()
        listOfAuthors = self.getListOfAuthors()
        booksList = self.__booksRepository.getAll()
        numberOfTimesAuthorBooksWereRented = []
        topRentedAuthors = []

        for position in range(0, len(listOfAuthors) + 1):
            numberOfTimesAuthorBooksWereRented.append(0)

        for rental in (rentalsList):
            book = self.__booksRepository.findById(rental.bookId)
            author = book.author
            authorPositionInList = listOfAuthors.index(author)
            numberOfTimesAuthorBooksWereRented[authorPositionInList] = numberOfTimesAuthorBooksWereRented[
                                                                           authorPositionInList] + 1

        for i in range(0, len(listOfAuthors)):
            maximOfTimesAuthorWasRented = max(numberOfTimesAuthorBooksWereRented)
            authorPosition = numberOfTimesAuthorBooksWereRented.index(maximOfTimesAuthorWasRented)
            numberOfTimesAuthorBooksWereRented[authorPosition] = -1
            topRentedAuthors.append(str(i + 1) + ' ' + listOfAuthors[authorPosition])

        return topRentedAuthors

    def getListOfAuthors(self):
        listOfAuthors = []
        for book in self.__booksRepository.getAll():
            if book.author not in listOfAuthors:
                listOfAuthors.append(book.author)

        return listOfAuthors

    def clientsStatistics(self):
        """
        Function looks through rentals list and memorizes the number of days each rental has borrowed books then creates
        a new list with the clients in the order of their activity.
        :return: a list containing all the clients in the order of their activity
        """
        clientsList = self.__clientsRepository.getAll()
        rentalsList = self.getAllRentals()
        maximClientId = self.__clientsRepository.findHighestIdInList()
        clientRentalDaysList = []
        topRentingClients = []

        for position in range(0, maximClientId + 1):
            if self.__booksRepository.findById(position) is None:
                clientRentalDaysList.append(-1)
            else:
                clientRentalDaysList.append(0)

        for rental in (rentalsList):
            if rental.returnedDate != '0':
                numberOfDaysClientRented = RentalServices.calculateNumberOfDaysBetweenDates(str(rental.rentedDate),
                                                                                            str(rental.returnedDate))
                numberOfDaysClientRented = int(numberOfDaysClientRented)
                clientRentalDaysList[rental.clientId] = clientRentalDaysList[rental.clientId] + numberOfDaysClientRented

        for position in range(0, len(clientsList)):
            maximTimeClientRented = max(clientRentalDaysList)
            clientPosition = clientRentalDaysList.index(maximTimeClientRented)
            clientRentalDaysList[clientPosition] = -1
            client = self.__clientsRepository.findById(clientPosition)
            topRentingClients.append(client)

        return topRentingClients

    def getAllRentals(self):
        return self.__rentalsRepository.getAll()

    @staticmethod
    def calculateNumberOfDaysBetweenDates(startDate, endDate):
        date_format = "%d/%m/%Y"
        a = datetime.strptime(startDate, date_format)
        b = datetime.strptime(endDate, date_format)
        delta = b - a

        return delta.days
