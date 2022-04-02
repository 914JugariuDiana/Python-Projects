import unittest

from src.domain.Entities import Book, Client
from src.domain.Exceptions import NotUnicIdException, NonExistingIdException, RentalException
from src.repository.repository.Repository import Repository
from src.services.BookService import BookServices
from src.services.ClientService import ClientServices
from src.services.RentalServices import RentalServices


class TestBookServices(unittest.TestCase):
    def setUp(self) -> None:
        self.bookRepository = Repository()
        self.bookServices = BookServices(self.bookRepository)

    def tearDown(self) -> None:
        pass

    def testAddBook_validBookInformation_listLenghtIncreased(self):
        self.assertEqual(len(self.bookServices.getAllBooks()), 0)
        self.bookServices.addBook(15, "Mara", "Ioan Slavici")
        self.assertEqual(len(self.bookServices.getAllBooks()), 1)

    def testAddBook_bookInformationAlreadyExistingId_NotUnicIdException(self):
        self.bookServices.addBook(15, "Mara", "Ioan Slavici")
        with self.assertRaises(NotUnicIdException) as ide:
            self.bookServices.addBook(15, "Ion", "shdbfi")
        self.assertEqual(str(ide.exception), "duplicate id 15")

    def testRemoveBook_validBookId_listLenghtDecresed(self):
        self.bookServices.addBook(15, "Mara", "Ioan Slavici")
        self.assertEqual(len(self.bookServices.getAllBooks()), 1)
        self.bookServices.removeBook(15)
        self.assertEqual(len(self.bookServices.getAllBooks()), 0)

    def testRemoveBook_nonExistentBookId_NonExistingIdException(self):
        with self.assertRaises(NonExistingIdException) as nonid:
            self.bookServices.removeBook(15)
        self.assertEqual(str(nonid.exception), "non exiting id 15")

    def testUpdateBook_newBookData_updatedBook(self):
        self.bookServices.addBook(15, "Mara", "Ioan Slavici")
        self.bookServices.updateBook(15, "Ion", "shdbfi")
        self.assertEqual(self.bookServices.getAllBooks(), [self.bookRepository.findById(15)])

    def testSearchBook_partialBookInformation_booksHavingMentionedInformation(self):
        self.bookServices.addBook(15, "Mara", "Ioan Slavici")
        book = self.bookServices.getAllBooks()
        self.assertEqual(self.bookServices.searchBook('ma'), book)

    def testSearchBook_nonExistentInformation_emptyList(self):
        self.assertEqual(self.bookServices.searchBook('ma'), [])


class TestClientServices(unittest.TestCase):
    def setUp(self) -> None:
        self.clientRepository = Repository()
        self.clientServices = ClientServices(self.clientRepository)

    def tearDown(self) -> None:
        pass

    def testAddClient_validClientInformation_listLenghtIncreased(self):
        self.assertEqual(len(self.clientServices.getAllClients()), 0)
        self.clientServices.addClient(15, "Ioan Slavici")
        self.assertEqual(len(self.clientServices.getAllClients()), 1)

    def testAddClient_clientInformationAlreadyExistingId_NotUnicIdException(self):
        self.clientServices.addClient(15, "Mara")
        with self.assertRaises(NotUnicIdException) as ide:
            self.clientServices.addClient(15, "Ion")
        self.assertEqual(str(ide.exception), "duplicate id 15")

    def testRemoveClient_validClientId_listLenghtDecreased(self):
        self.clientServices.addClient(15, "Ioan Slavici")
        self.assertEqual(len(self.clientServices.getAllClients()), 1)
        self.clientServices.removeClient(15)
        self.assertEqual(len(self.clientServices.getAllClients()), 0)

    def testRemoveClient_nonExistentClientId_NonExistingIdException(self):
        with self.assertRaises(NonExistingIdException) as nonid:
            self.clientServices.removeClient(15)
        self.assertEqual(str(nonid.exception), "non exiting id 15")

    def testUpdateClient_newClientData_updatedClient(self):
        self.clientServices.addClient(15, "Mara")
        self.clientServices.updateClient(15, "Ion")
        self.assertEqual(self.clientServices.getAllClients(), [self.clientRepository.findById(15)])

    def testSearchClient_validClientInformation_clientsHavingMentionedInformation(self):
        self.clientServices.addClient(15, "Ioan Slavici")
        client = self.clientServices.getAllClients()
        self.assertEqual(self.clientServices.searchClient('oa'), client)

    def testSearchClient_nonExistentInformation_emptyList(self):
        self.assertEqual(self.clientServices.searchClient('ma'), [])

class TestRentalServices(unittest.TestCase):
    def setUp(self) -> None:
        self.rentalRepository = Repository()
        self.bookRepository = Repository()
        self.clientRepository = Repository()
        self.rentalServices = RentalServices(self.rentalRepository, self.bookRepository, self.clientRepository)

    def tearDown(self) -> None:
        pass

    def testCheckBookAvailability_idOfBookRented_rental(self):
        self.rentalServices.addRental(1, 2, 3, "2/2/2002", '0')
        rental = self.rentalServices.getAllRentals()
        self.assertEqual([self.rentalServices.checkBookAvailability(2)], rental)

    def testCheckBookAvailability_idOfBookNotRented_none(self):
        self.assertEqual(self.rentalServices.checkBookAvailability(15), None)

    def testAddRental_validRentalInformations_listLenghtIncreased(self):
        self.assertEqual(len(self.rentalServices.getAllRentals()), 0)
        self.rentalServices.addRental(1, 2, 3, "2/2/2002", '0')
        self.assertEqual(len(self.rentalServices.getAllRentals()), 1)

    def testAddRental_rentalInformationBookAlreadyRented_rentalException(self):
        self.rentalServices.addRental(1, 2, 3, "2/2/2002", '0')
        with self.assertRaises(RentalException) as re:
            self.rentalServices.addRental(5, 2, 3, "2/5/2002", '0')
        self.assertEqual(str(re.exception), "book with id 2 not available")

    def testAddRental_duplicateRentalId_NotUnicIdException(self):
        self.rentalServices.addRental(1, 2, 3, "2/2/2002", '0')
        with self.assertRaises(NotUnicIdException) as ide:
            self.rentalServices.addRental(1, 5, 6, "2/3/2002", '0')
        self.assertEqual(str(ide.exception), "duplicate id 1")

    def testUpdateRental_newReturnedDate_newReturnDateInRental(self):
        self.rentalServices.addRental(1, 2, 3, "2/2/2002", '0')
        self.rentalServices.updateRental(1, "3/3/2005")
        rental = self.rentalRepository.findById(1)
        self.assertEqual(rental.returnedDate, "3/3/2005")

    def testBooksStatistics_bookRespository_orderedListOfBooksAfterPopularity(self):
        book = Book(12, "Ion", "Liviu Rebreanu")
        self.bookRepository.saveInList(book)
        self.rentalServices.addRental(1, 12, 3, "2/2/2002", '0')
        self.assertEqual(self.rentalServices.booksStatistics(), ['12 Ion Liviu Rebreanu'])

    def testAuthorsStatistics_bookRespository_orderedListOfBooksAfterPopularity(self):
        book = Book(12, "Ion", "Liviu Rebreanu")
        self.bookRepository.saveInList(book)
        self.rentalServices.addRental(1, 12, 3, "2/2/2002", '0')
        self.assertEqual(self.rentalServices.authorsStatistics(), ['1 Liviu Rebreanu'])

    def testBooksStatistics_clientRespository_orderedListOfBooksAfterPopularity(self):
        client = Client(12, "Liviu Rebreanu")
        self.clientRepository.saveInList(client)
        self.rentalServices.addRental(1, 12, 12, "2/2/2002", '2/2/2003')
        self.assertEqual(self.rentalServices.clientsStatistics(), [client])