# Python-Projects
Write an application for a book library. The application will store:

Book: book_id, title, author
Client: client_id, name
Rental: rental_id, book_id, client_id, rented_date, returned_date
Create an application to:

Manage clients and books. The user can add, remove, update, and list both clients and books.
Rent or return a book. A client can rent an available book. A client can return a rented book at any time. Only available books (those which are not currently rented) can be rented.
Search for clients or books using any one of their fields (e.g. books can be searched for using id, title or author). The search must work using case-insensitive, partial string matching, and must return all matching items.
Create statistics:
Most rented books. This will provide the list of books, sorted in descending order of the number of times they were rented.
Most active clients. This will provide the list of clients, sorted in descending order of the number of book rental days they have (e.g. having 2 rented books for 3 days each counts as 2 x 3 = 6 days).
Most rented author. This provides the list of book authors, sorted in descending order of the number of rentals their books have.
Unlimited undo/redo functionality. Each step will undo/redo the previous operation performed by the user. Undo/redo operations must cascade and have a memory-efficient implementation (no superfluous list copying).
You must implement two additional repository sets: one using text files for storage, and one using binary files (e.g. using object serialization with Pickle).

The program must work the same way using in-memory repositories, text-file repositories and binary file repositories.

The decision of which repositories are employed, as well as the location of the repository input files will be made in the program’s settings.properties file. An example is below:

a. settings.properties for loading from memory (input files are not required):

repository = inmemory
cars = “”
clients = “”
rentals = “”

Create a Python module that contains an iterable data structure, a sort method and a filter method, together with complete PyUnit unit tests (100% coverage). The module must be reusable in other projects.
What you will need to do
Implement an iterable data structure. Study the setItem,getitem, delItem, next and iter Python methods.
Implement a sorting algorithm that was not/will not be studied during the lecture or seminar (no bubble sort, cocktail sort, merge sort, insert sort, quicksort). You can use one of shell sort, comb sort, bingo sort, gnome sort, or other sorting method. Prove that you understand the sorting method implemented. The sort function will accept two parameters: the list to be sorted as well as a comparison function used to determine the order between two elements.
Implement a filter function that can be used to filter the elements from a list. The function will use 2 parameters: the list to be filtered, and an acceptance function that decided whether a given value passes the filter.
