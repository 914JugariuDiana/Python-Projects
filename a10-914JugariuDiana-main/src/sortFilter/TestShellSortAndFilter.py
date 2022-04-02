import unittest

from src.domain.Entities import Book
from src.repository.repository.Repository import Repository
from src.services.BookService import BookServices
from src.sortFilter.IterableDataStructure import SimpleLinkedList
from src.sortFilter.ShellSort import ShellSort, Filter


class TestShellSortAndFilter(unittest.TestCase):
    def setUp(self) -> None:
        self.bookRepository = Repository()
        self.bookServices = BookServices(self.bookRepository)

    def tearDown(self) -> None:
        pass

    def testShellSort_listOfObjectsAndKey_sortedListAfterKeyValue(self):
        self.bookServices.addBook(1, 'Pride and Prejudice', 'Jane Austen')
        self.bookServices.addBook(3, 'The Great Gatsby', 'Dodie Smith')
        self.bookServices.addBook(4, 'In Cold Blood', 'Truman Capote')
        self.bookServices.addBook(2, 'To Kill A Mockingbird', 'Aldous Huxley')
        shellSort = ShellSort(self.bookServices.getAllBooks(), key=lambda book: book.id)
        sortedList = shellSort.sort()
        for element in range(1, len(sortedList)):
            self.assertTrue(sortedList[element - 1].id < sortedList[element].id)

    def testFilter_listOfObjectesAndKey_filteredListAfterKey(self):
        self.bookServices.addBook(1, 'Pride and Prejudice', 'Jane Austen')
        self.bookServices.addBook(3, 'The Great Gatsby', 'Dodie Smith')
        self.bookServices.addBook(4, 'Pride and Prejudice', 'Truman Capote')
        self.bookServices.addBook(2, 'To Kill A Mockingbird', 'Aldous Huxley')
        filter = Filter(self.bookServices.getAllBooks(), key=lambda book: book.title)
        filteredList = filter.filter('Pride and Prejudice')
        for element in range(0, len(filteredList)):
            self.assertTrue(filteredList[element].title == 'Pride and Prejudice')

    def testFilter_SimpleLinkedList(self):
        simpleList = SimpleLinkedList()
        simpleList.append(Book(1, 'Pride and Prejudice', 'Jane Austen'))
        simpleList.append(Book(3, 'The Great Gatsby', 'Dodie Smith'))
        simpleList.append(Book(4, 'Pride and Prejudice', 'Truman Capote'))
        simpleList.append(Book(2, 'To Kill A Mockingbird', 'Aldous Huxley'))
        filter = Filter(simpleList, key=lambda book: book.title)
        filteredList = filter.filter('Pride and Prejudice')
        for element in range(0, len(filteredList)):
            self.assertTrue(filteredList[element].title == 'Pride and Prejudice')
