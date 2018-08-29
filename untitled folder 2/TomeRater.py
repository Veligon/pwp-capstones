class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address

    def __repr__(self):
        books_read = 0
        for book in self.books.keys():
            books_read += 1
        return "User Information: \n Name: {} \n Email: {} \n Number of Books Read: {}".format(self.name, self.email, books_read)

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        num_of_ratings = 0
        rating_total = 0.0
        for rating in self.books.values():
            if rating == None:
                rating = 0
            num_of_ratings += 1
            rating_total += rating
        if num_of_ratings == 0:
            return 0.0
        return rating_total / float(num_of_ratings)

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "{} has had it's ISBN code updated to {}.".format(self.title, self.get_isbn())

    def add_rating(self, rating):
        if rating == None:
            return "Invalid Rating"
        if rating >= 0 and rating <= 4:
          self.ratings.append(rating)
        else:
          print("Invalid Rating.")

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_average_rating(self):
        num_of_ratings = 0
        rating_total = 0.0
        for rating in self.ratings:
            num_of_ratings += 1
            rating_total += rating
        if num_of_ratings == 0:
            return 0.0
        return rating_total / float(num_of_ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "{}".format(self.title)

class Fiction(Book):
    author = None
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

class Non_Fiction(Book):
    subject = None
    level = None
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {}.".format(self.title, self.level, self.subject)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        Book_Object = Book(title, isbn)
        self.books[Book_Object] = 0
        return Book_Object

    def create_novel(self, title, author, isbn):
        Fiction_Object = Fiction(title, author, isbn)
        self.books[Fiction_Object] = 0
        return Fiction_Object

    def create_non_fiction(self, title, subject, level, isbn):
        Non_Fiction_Object = Non_Fiction(title, subject, level, isbn)
        self.books[Non_Fiction_Object] = 0
        return Non_Fiction_Object

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            User.read_book(self.users[email], book, rating)
            Book.add_rating(book, rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            return "No user with email {}!".format(email)

    def add_user(self, name, email, user_books=None):
        self.users[email] = User(name, email)
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)
        return User(name, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def get_most_read_book(self):
        most_times_read = float("-inf")
        for times_read in self.books.values():
            if times_read > most_times_read:
                most_times_read = times_read
        for book in self.books.keys():
            if self.books[book] == most_times_read:
                return book

    def highest_rated_book(self):
        highest_average_rating = float("-inf")
        book_title = None
        for book in self.books.keys():
            rating_level = book.get_average_rating()
            if rating_level > highest_average_rating:
                highest_average_rating = rating_level
                book_title = book.title
        return book_title

    def most_positive_user(self):
        highest_rating = float("-inf")
        highest_user = None
        for user in self.users.values():
            rating_level = User.get_average_rating(user)
            if rating_level > highest_rating:
                highest_rating = rating_level
                highest_user = user
        return highest_user.name

    def __repr__(self):
        return "TomeRater"