class Employee:
    num_of_empl = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first + "." + last + "@company.com").lower()

        Employee.num_of_empl += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "It's saturday or Sunday"
        return "It's working day"

    def __add__(self, other):
        return self.pay + other.pay

    def __str__(self):
        return "{} - {}".format(self.full_name(), self.email)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __len__(self):
        return len(self.full_name())


class Developer(Employee):

    def __init__(self, first, last, pay, prod_lang):
        super().__init__(first, last, pay)
        self.prod_lang = prod_lang

    raise_amount = 1.10


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.full_name())


dev_1 = Developer("Pierre", "Stoiko", 50000, "Python")
dev_2 = Developer("Xi", "Camargo", 60000, "Java")
mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

print(len(dev_1))
# print(repr(mgr_1))
# print(str(dev_2))
# print(dev_1+dev_2)


