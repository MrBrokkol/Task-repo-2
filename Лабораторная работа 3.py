class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Колчиество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительно")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга: {self.name}, {self.author}, {self.pages} страниц."

    def __repr__(self):
        return f"PaperBook('{self.name}', '{self.author}', {self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float): 
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise ValueError("Длительность должна быть вещественным числом")
        if value <= 0:
            raise ValueError("Длительность должна быть положительна")
        self._duration = value

    def __str__(self):
        return f"Аудиокнига: {self.name}, {self.author}, {self.duration} минут."

    def __repr__(self):
        return f"AudioBook('{self.name}', '{self.author}', {self.duration})"
