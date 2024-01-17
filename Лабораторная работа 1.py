import random

class Student:
    """
    Создание класса Студент

    name: имя студента (Строка)
    age: возраст студента (целое число)
    marks: словарь предметов и оценок студента
    Словарь вида {"предмет" : оценка, ...}
    """
    def __init__(self, name: str, age: int, marks: dict):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if not isinstance(marks, dict):
            raise TypeError("Оценки должны быть заданны в виде словаря")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        items = list(marks.items())
        for i in items:
            if not isinstance(i[0], str):
                raise TypeError("Словарь должен быть вида {\"предмет\" : оценка, ...}")
            if not isinstance(i[1], int):
                raise TypeError("Словарь должен быть вида {\"предмет\" : оценка, ...}")
        self.name = name
        self.age = age
        self.marks = marks

    def say_hi(self) -> None:
        #Выводит имя и возраст студента в виде приветствия
        print(f"Привет, я %(self.name)s. Мне %(age)d лет.")

    def add_mark(self, exam: str, mark: int, ret = False) -> dict:
        """
        Метод добавляющий студенту оценку
        Принимает аргументы
        exam: название экзамена
        mark: оценка
        ret: отвечает за вывод словаря как результата выполнения функции
        """
        if not isinstance(exam, str):
            raise TypeError("Название экзамена должно быть строкой")
        if not isinstance(mark, int):
            raise TypeError("Оценка должна быть числом")
        if not isinstance(ret, bool):
            raise TypeError("Аргумент ret должен быть типа bool")
        self.marks[exam] = mark
        if ret:
            return self.marks

    def aver_mark(self) -> float:
        #Метод возвращающий средний балл студента
        values = self.marks.values()
        return sum(values)/len(values)

Josh = Student("Josh", 21, {"Math":5, "Physics":2})
print(type(Josh))

class Charger:
    """
    Создание класса зарядного устройства для батарей

    name: название
    voltage: выходное напряжение
    amperage: выходное напряжение
    """
    
    def __init__(self, name: str, voltage: float, amperage: float):
        if not isinstance(voltage, (int, float)):
            raise TypeError("Напяжение должно быть числом")
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        if not isinstance(amperage, (int, float)):
            raise TypeError("Ток должен быть числом")
        self.name = name
        self.amperage = amperage
        self.voltage = voltage

    def check_battery(self, battery) -> bool:
        #Проверяет совместимость батареи и зарядного устройства
        if self.voltage == battery.voltage:
            return True
        else:
            return False
    def charge(self, battery) -> None:
        battery.apply_charger(self)
    
class Battery:
    """
    Создание класса аккумулятора
    
    name: название
    capacity: ёмкость
    charge: процент заряда
    voltage: напряжение в заряженном состоянии
    """
    def __init__(self, name: str, capacity: int, charge: float, voltage: float):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        if not isinstance(capacity, int):
            raise TypeError("Ёмкость должена быть типа int")
        if not isinstance(charge, (int, float)):
            raise TypeError("Процент зарядки должен быть числом")
        if not isinstance(voltage, (int, float)):
            raise TypeError("Напяжение должно быть числом")
        if capacity < 0:
            raise ValueError("Ёмкость не может быть отрицательна")
        if voltage < 0:
            raise ValueError("Напряжение не может быть отрицательно")
        if charge < 0 or charge > 100:
            raise ValueError("Процент заряда должен входить в промежуток от 0 до 100%")

        self.name = name
        self.capacity = capacity
        self.charge = charge
        self.voltage = voltage

    def apply_charger(self, charger) -> None:
        #Функция заряжающая батарею на рандомное количество процентов, может зарядить и полностью
        if self.voltage != charger.voltage:
            print("Напряжение не подходит")
        else:
            self.charge += (100 - self.charge)*random.random()

    def add_capacity(self, added_capacity: int) -> None:
        #Метод увеличивающий объём батареии на введёное число
        if not isinstance(added_capacity, int):
            raise TypeError("Добавляемая ёмкость должна быть типа int")
        if added_capacity < 0:
            raise ValueError("Добавляемая ёмкость должна быть больше нуля")
        self.capacity += added_capacity

    def show_data(self) -> None:
        #Вывод всех данных
        print(self.name)
        print(str(self.capacity) + " мАч")
        print(str(self.charge) + "%")
        print(str(self.voltage) + " В")
        


 
    
        
