# problem4
class Book:
    def __init__(self):
        self.__bookId = ""
        self.__title = ""
        self.__author = ""

    def __init__(self, bookId, title, author):
        self.__bookId = bookId
        self.__title = title
        self.__author = author

    @property
    def id(self):
        return self.__bookId

    @id.setter
    def id(self, bookId):
        self.__bookId = bookId

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    def __str__(self):
        return str(self.id) + ' ' + str(self.title) + ' ' + str(self.author)

    def __repr__(self):
        return str(self.id) + ',' + str(self.title) + ',' + str(self.author)

    @staticmethod
    def readFrom(line):
        bookData = line.split(",")
        book = Book(int(bookData[0]), bookData[1], bookData[2])
        return book


class Client:
    def __init__(self, clientId, name):
        self.__clientId = clientId
        self.__name = name

    @property
    def id(self):
        return self.__clientId

    @id.setter
    def id(self, clientId):
        self.__clientId = clientId

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return str(self.id) + ' ' + str(self.name)

    def __repr__(self):
        return str(self.id) + ',' + str(self.name)

    @staticmethod
    def readFrom(line):
        clientData = line.split(",")
        client = Client(int(clientData[0]), clientData[1])
        return client


class Rental:
    def __init__(self, rentalId, bookId, clientId, rentedDate, returnedDate):
        self.__rentalId = rentalId
        self.__bookId = bookId
        self.__clientId = clientId
        self.__rentedDate = rentedDate
        self.__returnedDate = returnedDate

    @property
    def id(self):
        return self.__rentalId

    @id.setter
    def id(self, rentalId):
        self.__rentalId = rentalId

    @property
    def bookId(self):
        return self.__bookId

    @bookId.setter
    def bookId(self, bookId):
        self.__bookId = bookId

    @property
    def clientId(self):
        return self.__clientId

    @clientId.setter
    def clientId(self, clientId):
        self.__clientId = clientId

    @property
    def rentedDate(self):
        return self.__rentedDate

    @rentedDate.setter
    def rentedDate(self, rentedDate):
        self.__rentedDate = rentedDate

    @property
    def returnedDate(self):
        return self.__returnedDate

    @returnedDate.setter
    def returnedDate(self, returnedDate):
        self.__returnedDate = returnedDate

    def __str__(self):
        return str(self.id) + ' ' + str(self.bookId) + ' ' + str(self.clientId) + ' ' + str(
            self.rentedDate) + ' ' + str(self.returnedDate)

    def __repr__(self):
        return str(self.id) + ',' + str(self.bookId) + ',' + str(self.clientId) + ',' + str(
            self.rentedDate) + ',' + str(self.returnedDate)

    @staticmethod
    def readFrom(line):
        rentalData = line.split(",")
        rental = Rental(int(rentalData[0]), rentalData[1], rentalData[2], rentalData[3], rentalData[4])
        return rental