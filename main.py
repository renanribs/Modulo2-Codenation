import abc

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(abc.ABC):
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary

    @abc.abstractmethod
    def calc_bonus(self):
        return self.__sales * 0.15

    @abc.abstractmethod
    def get_hours(self):
        return 8


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, department):
        self.__departament.name = department

    def calc_bonus(self):
        return self.salary * 0.15

    def get_hours(self):
        return 8


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_hours(self):
        return 8

    def get_departament(self):
        return self.__departament.name

    def set_departament(self):
        return self.__departament.name

    def get_sales(self):
        return self.__sales

    def put_sales(self, valor):
        self.__sales += valor
