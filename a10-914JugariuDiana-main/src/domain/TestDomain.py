import unittest

from src.domain.Entities import Book, Rental
from src.domain.Entities import Client
from src.domain.Validators import ValidateDate


class TestBook(unittest.TestCase):

    def testBook_bookInformations_bookInformations(self):
        book = Book(1, "Ion", 'Liviu Rebreanu')
        self.assertEqual(book.id, 1)
        self.assertEqual(book.author, "Liviu Rebreanu")
        self.assertEqual(book.title, "Ion")

    def testStrBook_bookInformation_string(self):
        book = Book(1, 'jsuhsf', 'sdfgsi')
        self.assertEqual(book.__str__(), '1 jsuhsf sdfgsi')

class TestClient(unittest.TestCase):

    def testBook_bookInformations_bookInformations(self):
        client = Client(1, 'Liviu Rebreanu')
        self.assertEqual(client.id, 1)
        self.assertEqual(client.name, "Liviu Rebreanu")

    def testStrClient_clientInformation_string(self):
        client = Client(1, 'sdhosci adh')
        self.assertEqual(client.__str__(), '1 sdhosci adh')


class TestRental(unittest.TestCase):

    def testBook_bookInformations_bookInformations(self):
        rental = Rental(1, 2, 3, '2/3/2002', '3/3/2003')
        self.assertEqual(rental.id, 1)
        self.assertEqual(rental.bookId, 2)
        self.assertEqual(rental.clientId, 3)
        self.assertEqual(rental.rentedDate, '2/3/2002')
        self.assertEqual(rental.returnedDate, '3/3/2003')

    def testStrRental_rentalInformation_string(self):
        rental = Rental(1, 2, 1, '2/12/2012', '22/12/2013')
        self.assertEqual(rental.__str__(), '1 2 1 2/12/2012 22/12/2013')


class TestValidateDate(unittest.TestCase):

    def testValidateDate_correctDate_True(self):
        self.assertEqual(ValidateDate.validateDate('22/12/2021'), True)

    def testValidateDate_missingYearDate_False(self):
        self.assertEqual(ValidateDate.validateDate('1/5/'), False)

    def testValidateDate_incorrectMonthDate_False(self):
        self.assertEqual(ValidateDate.validateDate('9/13/2002'), False)

    def testValidateDate_incorrectDayDate_False(self):
        self.assertEqual(ValidateDate.validateDate('31/02/2002'), False)
