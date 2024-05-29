"""Book store."""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author and price.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price}, rating={self.rating})"

class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor.

        Each book store has name.
        There also should be an overview of all books present in store

        :param name: book store name
        :param rating: raamatu miinimumhinne kauplusele
        """
        self.name = name 
        self.rating = rating
        self.books =[]

    def can_add_book(self, book: Book) -> bool:
        """
        Check if book can be added.

        It is possible to add book to book store if:
        1. The book with the same author and title is not yet present in this book store
        2. book's own rating is >= than store's rating
        :param book: Book
        :return: bool
        """
        for i in self.books:
            if i.title==book.title and i.author==book.author:
                return False
        return book.rating>=self.rating


    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        if self.can_add_book(book):
            self.books.append(book)

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if book can be removed from store.

        Book can be successfully removed if it is actually present in store
        :param book: Book
        :return: bool
        """
        return book in self.books

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything

        :param book: Book
        """
        if self.can_remove_book(book):
            self.books.remove(book)

    def get_all_books(self) -> list:
        """
        Return a list of all books in current store.

        :return: list of Book objects
        """
        return self.books

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        return sorted(self.books, key=lambda x: x.price)

    def get_most_popular_book(self) -> list:
        """
        Return a list of book (books) with the highest rating.

        :return: list of Book objects
        """
        if not self.books:
            return []
        highest_rating=max(book.rating for book in self.books) 
        return [book for book in self.books if book.rating==highest_rating] 
    
if __name__=='__main__':
    book1 = Book("Harry Potter ja filosoofiline kivi", "Robert Helbrey", 14.59, 4.8)
    book2 = Book("Munk. Anakonda. Veneetsia mõrvar", "Matthew Gregory Lewise", 16.99, 4.7)
    book3 = Book("Koraan", "Muhammad Hussein Tabatabai", 17.59, 4.5)
    book4 = Book("Sinuga olen kodus.", "Olga Primatšenko", 7.19, 3.8)
    book5 = Book("Imelikud mängud", "Mike Omer", 10.29, 5.0)

    store = Store("Raamatupood", 4.9)

    store.add_book(book1)  
    store.add_book(book2)  
    store.add_book(book3)
    store.add_book(book4)
    store.add_book(book5)

    print(store.get_all_books()) # -> [Book(title='Imelikud mängud', author='Mike Omer', price=10.29, rating=5.0)]
    print(store.get_books_by_price()) # -> [Book(title='Imelikud mängud', author='Mike Omer', price=10.29, rating=5.0)]
    print(store.get_most_popular_book()) # -> [Book(title='Imelikud mängud', author='Mike Omer', price=10.29, rating=5.0)]
    store.remove_book(book2) 
    print(store.get_all_books()) # -> [Book(title='Imelikud mängud', author='Mike Omer', price=10.29, rating=5.0)]


