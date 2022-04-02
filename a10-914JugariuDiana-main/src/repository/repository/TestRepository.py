import unittest
from src.domain.Entities import Book
from src.repository.repository.Repository import Repository

class TestRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.repository = Repository()

    def tearDown(self) -> None:
        pass

    def testSaveInList_entity_listLenght(self):
        self.assertEqual(len(self.repository.getAll()),  0)
        book = Book(12, "Ion", "Liviu Rebreanu")
        self.repository.saveInList(book)
        self.assertEqual(len(self.repository.getAll()),  1)

    def testFindById_entityId_entityInformation(self):
        book = Book(12, "Ion", "Liviu Rebreanu")
        self.repository.saveInList(book)
        self.assertEqual(self.repository.findById(12),  book)

    def testFindHighestIdInList_listOfEntities_highestId(self):
        book = Book(12, "Ion", "Liviu Rebreanu")
        self.repository.saveInList(book)
        self.assertEqual(self.repository.findHighestIdInList(),  12)

    def testUpdateList_entityId_entityWithNewInformation(self):
        book = Book(12, "Ion", "Liviu Rebreanu")
        self.repository.saveInList(book)
        book = Book(12, "Iskdjfh", "Liviu Rebreanu")
        self.repository.updateList(book)
        self.assertEqual(self.repository.findById(12),  book)

    def testRemoveFromList_list_listLenght(self):
        book = Book(12, "Ion", "Liviu Rebreanu")
        self.repository.saveInList(book)
        self.assertEqual(len(self.repository.getAll()),  1)
        self.repository.removeFromList(12)
        self.assertEqual(len(self.repository.getAll()),  0)

    def testFindById_nonExistentId_None(self):
        self.assertEqual(self.repository.findById(5), None)

