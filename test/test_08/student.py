class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house
        # self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    #  Getter
    @property
    def name(self):
        return self._name

    #  Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    #  Getter
    @property
    def house(self):
        return self._house

    #  Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("Invalid house")
        self._house = house

    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "🦌"
    #         case "Otter":
    #             return "🦦"
    #         case "Jack Russell terrier":
    #             return "🐶"
    #         case _:
    #             return "🪄"


def main():
    student = get_student()
    print(student)
    # print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # patronus = input("Patronus: ")
    return Student(name.capitalize(), house.capitalize())


if __name__ == '__main__':
    main()
