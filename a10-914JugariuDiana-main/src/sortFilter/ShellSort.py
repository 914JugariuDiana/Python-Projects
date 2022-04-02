from src.domain.Entities import Book


class ShellSort():
    def __init__(self, elements, key=None, reverse=False):
        self.__elements = elements
        self.__key = key
        self.__reverse = reverse

    def sort(self):
        lenghtList = len(self.__elements)
        interval = lenghtList // 2
        while interval > 0:
            for value in range(interval, lenghtList):
                temporary = self.__elements[value]
                currentValue = value
                while currentValue >= interval and not self.inOrder(self.__elements[currentValue - interval], temporary):
                    self.__elements[currentValue] = self.__elements[currentValue - interval]
                    currentValue = currentValue - interval
                self.__elements[currentValue] = temporary
            interval = interval // 2

        return self.__elements

    def getElements(self):
        return self.__elements

    def inOrder(self, element1, element2):
        if self.__key(element1) < self.__key(element2):
            return True
        return False


class Filter():
    def __init__(self, elements, key=None):
        self.__elements = elements
        self.__key = key

    def filter(self, value):
        element = 0
        filteredList = []
        while element < len(self.__elements):
            if self.__key(self.__elements[element]) == value:
                filteredList.append(self.__elements[element])
            element += 1
        return filteredList



"""
if __name__ == '__main__':
    book2 = Book(3, 'The Great Gatsby', 'Dodie Smith')
    book3 = Book(4, 'In Cold Blood', 'Truman Capote')
    book = Book(1, 'Pride and Prejudice', 'Jane Austen')
    book1 = Book(2, 'To Kill A Mockingbird', 'Aldous Huxley')
    list = [book2, book3, book, book1]
    sortAlgorithm = ShellSort(list, key=id)
    sortAlgorithm.sort()
    for element in sortAlgorithm.getElements():
        print(element)
"""
