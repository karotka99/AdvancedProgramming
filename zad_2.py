import datetime
from zad_1 import Student
from typing import List

class Library:
    def __init__( self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"""
        Library in {self.city} ({self.zip_code}), {self.street}, 
        Opening hours: {self.open_hours}, 
        Contact number: {self.phone} 
        """

class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: datetime.date, birth_date: datetime.date, city: str, street: str, zip_code: str, phone: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f"""
        Employee: {self.first_name} {self.last_name}, 
        Born: {self.birth_date}, 
        Hired: {self.hire_date}, 
        Living in: {self.city} ({self.zip_code}), {self.street}, 
        Contact number: {self.phone}
        """

class Book:
    def __init__(self, library: Library, publication_date: datetime.date, author_name: str, author_surname: str, number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"""
        Book written by: {self.author_name} {self.author_surname}, 
        Published: {self.publication_date}, 
        Number of pages: {self.number_of_pages}, 
        Localization: {self.library.__str__()}
        """

class Order:
    def __init__(self, employee: Employee, student: Student, books: List[Book], order_date: datetime.date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        ordered_books = "; ".join([" ".join(book.__str__().replace("\n", "").split()) for book in self.books])

        return f"""
        Ordered by: {self.student}, 
        Books:{ordered_books}, 
        Order date: {self.order_date}, 
        Employee: {self.employee}
        """


library_1 = Library("Wodzislaw Slaski", "Szkolna 35", "40-342", "8:30-16:00", "+48000111000")
library_2 = Library("Jastrzebie Zdroj", "Centralna 123", "13-632", "9:10-15:00", "+48098765432")

book_1 = Book(library_1, datetime.date(2002, 8, 13), "Johan", "Boots", 123)
book_2 = Book(library_1, datetime.date(1998, 12, 1), "Joanna", "Dark", 345)
book_3 = Book(library_2, datetime.date(1932, 11, 30), "Sylvia Roberts", "Roberts", 453)
book_4 = Book(library_2, datetime.date(1999, 4, 23), "Monica", "Blanco", 654)
book_5 = Book(library_2, datetime.date(2013, 5, 9), "Andrew", "Black", 234)

employee_1 = Employee("Anna", "Nowak", datetime.date(2017, 1, 1), datetime.date(1989, 12, 12), "Zabrze", "Szkolna 13", "43-210", "+481234567")
employee_2 = Employee("Aniela", "Kowal", datetime.date(2010, 3, 23), datetime.date(1979, 1, 24), "Kalety", "Wolna 4", "32-345","+48111111111")
employee_3 = Employee("Arkadiusz", "Morawiecki", datetime.date(2010, 5, 22), datetime.date(1967, 10, 25), "Bytom", "Wroclawska 43", "33-333", "+48345345345")


student_1 = Student("Karolina Tol", 45)
student_2 = Student("Adrian Wir", 82)
student_3 = Student("Sandra Wójcik", 68)

order_1 = Order(employee_1, student_1, [book_1,book_2], datetime.date(2021, 10, 26))
order_2 = Order(employee_2, student_2, [book_3,book_4], datetime.datetime.now())

print(order_1)
print(order_2)
