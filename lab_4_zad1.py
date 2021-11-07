class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    @property
    def is_passed(self) -> bool:
        return self.marks > 50

    def __str__(self) -> str:
        return f"""
        Student: {self.name}, 
        Marks: {self.marks}
        """


student1 = Student('Karolina', 84)
student2 = Student('Martyna', 35)

print(student1)
print(student1.is_passed)
print(student2)
print(student2.is_passed)
