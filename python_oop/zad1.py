class Student:
    def __init__(self, name: str, marks: [int]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        val = 0
        it = 0
        for i in self.marks:
            val += i
            it += 1
        arg = val/it
        if arg > 3.0:
            return True
        else:
            return False


Krycha = Student("Krycha", [2, 3, 1, 4, 3, 5, 5])
Divix = Student("Divix", [1, 2, 3, 1])

print(Krycha.is_passed(), Divix.is_passed())
