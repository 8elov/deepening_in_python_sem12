class NameValidator:
    """Descriptor class for validating names."""
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("'Имя' должно быть строкой")

        if not value.isalpha():
            raise ValueError("'Имя' должно содержать только буквы")

        if not value.istitle():
            raise ValueError("'Имя' должно начинаться с заглавной буквы")

        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Student:
    """Represents a student with validated first name,
    last name, and middle name."""
    first_name = NameValidator()
    last_name = NameValidator()
    middle_name = NameValidator()

    def __init__(self, first_name, last_name, middle_name):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name


try:
    student = Student("Никита", "Белов", "Русланович")
    print("Student information:")
    print(f"First Name: {student.first_name}")
    print(f"Last Name: {student.last_name}")
    print(f"Middle Name: {student.middle_name}")
except ValueError as e:
    print(f"Error: {e}")
