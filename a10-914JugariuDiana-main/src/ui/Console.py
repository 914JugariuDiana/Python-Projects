from datetime import date
import random
import datetime
from src.domain.Exceptions import *
from src.services.RentalServices import RentalException
from src.services.RentalServices import RentalExceptionUnavailableRantal
from src.services.Undo import UndoManager
from src.settings.settings import Settings


class Console:
    def __init__(self, bookServices, clientServices, rentalServices):
        self.__commands = {"1": self.addBook, "2": self.printAllBooks, "3": self.addClient, "9": self.removeBook,
                           "6": self.removeClient, "8": self.rentBook, "11": self.returnBook,  "10": self.updateBook,
                           "5": self.updateClient, "4": self.printAllClients, "~": self.printAllRentals,
                           "12": self.findBook, "7": self.findClient, "13": self.booksStatistics,
                           "14": self.clientsStatistics, "15": self.authorsStatistics, "16": self.undo, "17": self.redo}
        self.__bookServices = bookServices
        self.__clientServices = clientServices
        self.__rentalServices = rentalServices

    def printMenu(self):
        print('     1 to add a book')
        print('     2 to print the list of books')
        print('     3 to add a rental')
        print('     4 to print the list of clients')
        print('     5 to update a rental')
        print('     6 to remove a rental')
        print('     7 find rental')
        print('     8 to rent a book')
        print('     9 to remove a book')
        print('     10 to update a book')
        print('     11 to return a book')
        print('     12 find book')
        print('     13 books statistic')
        print('     14 clients statistics')
        print('     15 author statistics')
        print('     16 undo')
        print('     17 redo')
        print('     x to exit the program')

    def runConsole(self):
        settings = Settings()
        if settings.getRepositoryType() == 'in-memory':
            self.addElements()
        UndoManager.emptyUndoList()

        self.printMenu()
        while True:
            print('> ', end='')
            command = input()
            if command == 'x':
                return False

            if command not in self.__commands:
                print("Bad command")
            else:
                try:
                    if command == "1" and command == "3" and command == "5" and command == "6" and command == "8"\
                            and command == "9" and command == "10" and command == "11":
                        UndoManager.emptyRedoList()
                    self.__commands[command]()
                except NotUnicIdException as ide:
                    print("error - " + str(ide))
                except NonExistingIdException as nonid:
                    print("error - " + str(nonid))
                except RentalException as re:
                    print("error - " + str(re))
                except RentalExceptionUnavailableRantal as ru:
                    print("error - " + str(ru))
                except EmptyListException as ee:
                    print("error - " + str(ee))


    def printAllBooks(self):
        booksList = self.__bookServices.getAllBooks()
        self.printList(booksList)

    def printAllClients(self):
        clientsList = self.__clientServices.getAllClients()
        self.printList(clientsList)

    def printAllRentals(self):
        rentalList = self.__rentalServices.getAllRentals()
        self.printList(rentalList)

    def printList(self, list):
        for element in list:
            print(element)

    def addBook(self):
        print('Write the books information: ', end='')
        print('Id: ', end='')
        bookId = int(input())
        print('Name: ', end='')
        bookName = input()
        print('Author: ', end='')
        bookAuthor = input()

        self.__bookServices.addBook(bookId, bookName, bookAuthor)

    def addClient(self):
        print('Write the rental information: ', end='')
        print('Id: ', end='')
        clientId = int(input())
        print('Name: ', end='')
        clientName = input()

        self.__clientServices.addClient(clientId, clientName)

    def removeBook(self):
        print('Book id: ', end='')
        bookId = int(input())
        self.__bookServices.removeBook(bookId)

    def removeClient(self):
        print('Client id: ', end='')
        clientId = int(input())
        self.__clientServices.removeClient(clientId)

    def updateBook(self):
        print('Id of book to be modified: ', end='')
        bookId = int(input())
        print('New name: ', end='')
        bookName = input()
        print('New author: ', end='')
        bookAuthor = input()
        self.__bookServices.updateBook(bookId, bookName, bookAuthor)

    def updateClient(self):
        print('Id of rental to be modified: ', end='')
        clientId = int(input())
        print('New name: ', end='')
        clientName = input()
        self.__clientServices.updateClient(clientId, clientName)

    def rentBook(self):
        print('Rental id: ', end='')
        rentalId = int(input())
        print('Book id: ', end='')
        bookId = int(input())
        print('Client id: ', end='')
        clientId = int(input())
        print('Date of client (dd/mm/yy):', end='')
        rentedDate = input()
        self.__rentalServices.addRental(rentalId, bookId, clientId, rentedDate, '0')

    def returnBook(self):
        today = date.today()
        returnDate = today.strftime("%d/%m/%Y")
        print('Date of return: ', returnDate)
        print('Rental id: ', end='')
        rentalId = int(input())
        self.__rentalServices.updateRental(rentalId, returnDate)

    def findBook(self):
        print("Write information: ", end='')
        bookInformation = input(str())
        bookInformation = bookInformation.lower()
        booksMatchingInformation = self.__bookServices.searchBook(bookInformation)
        self.printList(booksMatchingInformation)

    def findClient(self):
        print("Write information: ", end='')
        clientInformation = input(str())
        clientInformation = clientInformation.lower()
        clientMatchingInformation = self.__clientServices.searchClient(clientInformation)
        self.printList(clientMatchingInformation)

    def booksStatistics(self):
        topRentedBooks = self.__rentalServices.booksStatistics()
        self.printList(topRentedBooks)

    def authorsStatistics(self):
        topRentedAuthors = self.__rentalServices.authorsStatistics()
        self.printList(topRentedAuthors)

    def clientsStatistics(self):
        topRentingClients = self.__rentalServices.clientsStatistics()
        self.printList(topRentingClients)

    def undo(self):
        UndoManager.undo()

    def redo(self):
        UndoManager.redo()

    def addBooks(self):
        bookList = ["Pride and Prejudice", "To Kill A Mockingbird", "The Great Gatsby", "In Cold Blood", "Brave New World"
                    "One Hundred Years of Solitude", "Wide Sargasso Sea", "I Capture the Castle", "The Dark Hours",
                    "The Stranger in the Lifeboat", "The Judge's List", "The Wish", "Never", "Better off Dead", "Game On",
                    "The Lincoln Highway", "Ugly Love", "These Violent Delights", "The Final Revival of Opal & Nev",
                    "Yellow Wife"]
        authorList = ["Jane Austen", "Aldous Huxley", "Dodie Smith", "Jean Rhys", "Truman Capote", "Harper Lee"
                      "Gabriel Garcia Marquez", "Mitch Albom", "Michael Connelly", "John Grisham", "Nicholas Sparks",
                      "Ken Follett", "Lee Child", "Janet Evanovich", "Andrew Child", "Amor Towles", "Colleen Hoover",
                      "Chloe Gong", "Dawnie Walton", "Sadeqa Johnson"]
        for id in range(1, 21):
            bookName = random.choice(bookList)
            authorName = random.choice(authorList)
            self.__bookServices.addBook(id, bookName, authorName)

    def addClients(self):
        clientFirstNameList = ["Hugh", "Tom", "Chris", "Henry", "Christian", "Vin", "Leonardo", "Robert", "Idris",
                               "Benedict", "Daniel", "Naomie", "Helen", "Thandie", "Chiwetel", "Michaela", "Eddie",
                               "Bruce", "Arnold", "Tommy"]
        clientSecondNameList = ["Jackman", "Cruise", "Hemsworth", "Cavill", "Downey", "Elba", "Cumberbatch", "Evans",
                                "Dicaprio", "Diesel", "Radcliffe", "Harris", "Mirren", "Newton", "Ejiofor", "Coel",
                                "Murphy", "Willis", "Schwarzenegger", "Hanks"]
        for id in range(1, 21):
            clientFirstName = random.choice(clientFirstNameList)
            clientSecondName = random.choice(clientSecondNameList)
            clientName = str(clientFirstName) + ' ' + str(clientSecondName)
            self.__clientServices.addClient(id, clientName)

    def addRentals(self):
        listBooksIds = [book.id for book in self.__bookServices.getAllBooks()]
        rentedBooksIdList = [0]
        listClientsId = [client.id for client in self.__clientServices.getAllClients()]
        for bookId in range (0, len(listBooksIds) + 2):
            rentedBooksIdList.append(0)

        for id in range(1, 21):
            randomBookId = random.choice(listBooksIds)
            rentedBooksIdList[randomBookId] = rentedBooksIdList[randomBookId] + 1
            randomClientId = random.choice(listClientsId)
            randomDate = Console.randomDate(datetime.date(2002, 2, 1), datetime.date(2022, 1, 1))
            randomRentDate = Console.strDate(randomDate)
            self.__rentalServices.addRental(id, randomBookId, randomClientId, randomRentDate, '0')
            randomReturnDate = Console.strDate(Console.randomDate(randomDate, datetime.date(2022, 1, 1)))
            self.__rentalServices.updateRental(id, randomReturnDate)

    @staticmethod
    def randomDate(startDate, endDate):
        timeBetweenDates = endDate - startDate
        days_between_dates = timeBetweenDates.days
        randomNumberOfDays = random.randrange(days_between_dates)
        randomDate = startDate + datetime.timedelta(days=randomNumberOfDays)

        return randomDate
    @staticmethod
    def strDate(randomDate):
        date = str(randomDate.day) + '/' + str(randomDate.month) + '/' + str(randomDate.year)

        return date

    def addElements(self):
        self.addBooks()
        self.addClients()
        self.addRentals()