
class Library:
    def __init__(self, city: str, street: str, zip_code: str,
                 open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (
            f"Biblioteka:\n"
            f"  Miasto: {self.city}\n"
            f"  Ulica: {self.street}\n"
            f"  Kod pocztowy: {self.zip_code}\n"
            f"  Godziny otwarcia: {self.open_hours}\n"
            f"  Telefon: {self.phone}"
        )


class Employee:
    def __init__(self, first_name, last_name, hire_date,
                 birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (
            f"Pracownik: {self.first_name} {self.last_name}\n"
            f"  Data zatrudnienia: {self.hire_date}\n"
            f"  Data urodzenia: {self.birth_date}\n"
            f"  Adres: {self.street}, {self.zip_code} {self.city}\n"
            f"  Telefon: {self.phone}"
        )


class Student:
    def __init__(self, first_name, last_name, student_id,
                 city, street, zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.city = city
        self.street = street
        self.zip_code = zip_code

    def __str__(self):
        return (
            f"Student: {self.first_name} {self.last_name}\n"
            f"  Numer indeksu: {self.student_id}\n"
            f"  Adres: {self.street}, {self.zip_code} {self.city}"
        )


class Book:
    def __init__(self, library, publication_date,
                 author_name, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Książka:\n"
            f"  Autor: {self.author_name}\n"
            f"  Data publikacji: {self.publication_date}\n"
            f"  Liczba stron: {self.number_of_pages}\n"
            f"  {self.library}"
        )


class Order:
    def __init__(self, employee, student, books: list[Book],
                 order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_description = "\n\n".join(
            str(book) for book in self.books
        )

        return (
            f"ZAMÓWIENIE\n"
            f"Data zamówienia: {self.order_date}\n\n"
            f"Pracownik obsługujący:\n{self.employee}\n\n"
            f"Student składający zamówienie:\n{self.student}\n\n"
            f"Zamówione książki:\n{books_description}"
        )


# 1. Tworzenie dwóch bibliotek
library1 = Library(
    "Warszawa", "Marszałkowska 10",
    "00-001", "8:00-18:00", "111-222-333"
)

library2 = Library(
    "Kraków", "Długa 20",
    "30-001", "9:00-17:00", "444-555-666"
)


# 2. Tworzenie pięciu książek
book1 = Book(library1, 2020, "Adam Mickiewicz", 300)
book2 = Book(library1, 2018, "Henryk Sienkiewicz", 450)
book3 = Book(library1, 2022, "Olga Tokarczuk", 280)
book4 = Book(library2, 2019, "Bolesław Prus", 350)
book5 = Book(library2, 2023, "Stanisław Lem", 220)


# 3. Tworzenie trzech pracowników
employee1 = Employee(
    "Anna", "Kowalska", "2020-03-01",
    "1990-05-12", "Warszawa",
    "Polna 5", "00-100", "123-456-789"
)

employee2 = Employee(
    "Piotr", "Nowak", "2019-06-15",
    "1985-08-20", "Kraków",
    "Kwiatowa 8", "30-200", "234-567-890"
)

employee3 = Employee(
    "Maria", "Wiśniewska", "2022-01-10",
    "1995-11-03", "Warszawa",
    "Leśna 12", "00-200", "345-678-901"
)


# 4. Tworzenie trzech studentów
student1 = Student(
    "Jan", "Kowalski", "S001",
    "Warszawa", "Szkolna 1", "00-300"
)

student2 = Student(
    "Ewa", "Zielińska", "S002",
    "Kraków", "Akademicka 2", "30-400"
)

student3 = Student(
    "Tomasz", "Lewandowski", "S003",
    "Gdańsk", "Morska 3", "80-500"
)


# 5. Tworzenie dwóch zamówień
order1 = Order(
    employee1,
    student1,
    [book1, book2, book4],
    "2026-10-20"
)

order2 = Order(
    employee2,
    student2,
    [book3, book5],
    "2026-10-22"
)


# 6. Wyświetlenie obu zamówień
print(order1)
print("\n" + "=" * 50 + "\n")
print(order2)
