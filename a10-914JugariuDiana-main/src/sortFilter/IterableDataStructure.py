class IterableDataStructure:
    def __init__(self):
        self.__list = []

    def __getitem__(self, key):
        return self.__list[key]

    def __setitem__(self, key, value):
        self.__list[key] = value

    def __delitem__(self, key):
        self.__list.pop(key)

    def __iter__(self):
        iterator = IterableDataStructure.Iterator(self.__list, -1)
        return iterator

    def __len__(self):
        return len(self.__list)

    def append(self, entity):
        self.__list.append(entity)

    def remove(self, entity):
        self.__list.remove(entity)

    class Iterator:
        def __init__(self, list, position):
            self.__position = position
            self.__list = list

        def __next__(self):
            self.__position += 1
            if self.__position == len(self.__list):
                raise StopIteration
            return self.__list[self.__position]


class SimpleLinkedList:
    class Node:
        def __init__(self, element):
            self.__element = element
            self.__next = None

        @property
        def element(self):
            return self.__element

        @element.setter
        def element(self, element):
            self.__element = element

        @property
        def next(self):
            return self.__next

        @next.setter
        def next(self, next):
            self.__next = next

    class Iterator:
        def __init__(self, node):
            self.__node = node

        def __next__(self):
            if self.__node is None:
                raise StopIteration
            element = self.__node.element
            self.__node = self.__node.next
            return element

    def __init__(self):
        self.__first = None
        self.__count = 0

    def __iter__(self):
        return SimpleLinkedList.Iterator(self.__first)

    def __get_node_at_position(self, position):
        if position >= self.__count:
            raise IndexError()
        current = self.__first
        while position > 0:
            current = current.next
            position -= 1
        return current

    def __getitem__(self, key):
        return self.__get_node_at_position(key).element

    def __setitem__(self, key, value):
        self.__get_node_at_position(key).element = value

    def __delitem__(self, key):
        if key == 0:
            self.__first = self.__first.next
        node = self.__get_node_at_position(key-1)
        node.next = node.next.next

    def __len__(self):
        return self.__count

    def append(self, element):
        node = SimpleLinkedList.Node(element)
        node.next = self.__first
        self.__first = node
        self.__count += 1

    def remove(self, element):
        if self.__first.element == element:
            self.__first = self.__first.next
            self.__count -= 1
        prev = self.__first
        current = self.__first.next
        while current is not None:
            if current.element == element:
                prev.next = current.next
                self.__count -= 1
                return
            prev = current
            current = current.next

if __name__ == '__main__':
    l = SimpleLinkedList()
    l.append(4)
    l.append(5)
    l.append(3)
    l.append(10)

    for i in l:
        print(i)

    del l[2]

    for i in l:
        print(i)



