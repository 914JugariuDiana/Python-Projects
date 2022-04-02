class NotUnicIdException(Exception):
    def __init__(self, id, message="duplicate id {0}"):
        self.id = id
        self.message = message
        super().__init__(self.message.format(self.id))

class NonExistingIdException(Exception):
    def __init__(self, id, message="non exiting id {0}"):
        self.id = id
        self.message = message
        super().__init__(self.message.format(self.id))

class RentalException(Exception):
    def __init__(self, id, message="book with id {0} not available"):
        self.id = id
        self.message = message
        super().__init__(self.message.format(self.id))

class RentalExceptionUnavailableRantal(Exception):
    def __init__(self, id, message="client with id {0} does not exist"):
        self.id = id
        self.message = message
        super().__init__(self.message.format(self.id))

class EmptyListException(Exception):
    def __init__(self, message="no more operations to undo"):
        self.message = message
        super().__init__(self.message.format())
