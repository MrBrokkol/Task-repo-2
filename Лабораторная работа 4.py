from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, age: int):
        """
        Конструктор класса Animal.
        name: имя животного
        age: возраст животного
        """
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        #Возвращает имя животного.
        return self._name

    @property
    def age(self) -> int:
        #Возвращает возраст животного.
        return self._age

    @abstractmethod
    def make_sound(self) -> str:
        #Абстрактный метод, который должен быть переопределен в дочерних классах для издания звука животным.
        pass

    def __str__(self) -> str:
        #Магический метод для строкового представления объекта.
        return f"{self.__class__.__name__}: {self.name}, {self.age} years old."

    def __repr__(self) -> str:
        #Магический метод для представления объекта.
        return f"{self.__class__.__name__}('{self.name}', {self.age})"
        

class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        """
        Конструктор класса Dog.

        name: Имя
        age: Возраст
        breed: Порода
        """
        super().__init__(name, age)
        self._breed = breed

    @property
    def breed(self) -> str:
        #Возвращает породу собаки.
        return self._breed

    def make_sound(self) -> str:
        #Переопределенный метод из базового класса для собаки.
        return "Woof! Woof!"

    def __str__(self) -> str:
        #Магический метод для строкового представления объекта Dog.
        return f"Dog: {self.name}, {self.age} years old, {self.breed}."

    def __repr__(self) -> str:
        #Магический метод для представления объекта Dog.
        return f"Dog('{self.name}', {self.age}, '{self.breed}')"
