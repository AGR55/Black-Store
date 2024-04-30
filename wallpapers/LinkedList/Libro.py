class Libro:
    def __init__(self, name, author, isbn):
        self.name = name
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f'Libro = [Name: {self.name}, Author: {self.author}, ISBN: {self.isbn}]'
