# Base class
class Person:
    def __init__(self, name: str, phone_number: int, email_address: str):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address

# Student class
class Student(Person):
    def __init__(self, name: str, phone_number: int, email_address: str, student_number: int, average_mark: float):
        super().__init__(name, phone_number, email_address)
        self.student_number = student_number
        self.average_mark = average_mark

    def print_info(self):
        print(f"\nStudent Info:")
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email Address: {self.email_address}")
        print(f"Student Number: {self.student_number}")
        print(f"Average Mark: {self.average_mark}")

# Professor class
class Professor(Person):
    def __init__(self, name: str, phone_number: int, email_address: str, salary: float):
        super().__init__(name, phone_number, email_address)
        self.salary = salary

    def print_info(self):
        print(f"\nProfessor Info:")
        print(f"Name: {self.name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email Address: {self.email_address}")
        print(f"Salary: {self.salary} €")

# Main program
if __name__ == "__main__":
    print("Enter Student Info:")
    s_name = input("Name: ")
    s_phone = int(input("Phone Number: "))
    s_email = input("Email Address: ")
    s_number = int(input("Student Number: "))
    s_mark = float(input("Average Mark: "))
    student = Student(s_name, s_phone, s_email, s_number, s_mark)

    print("\nEnter Professor Info:")
    p_name = input("Name: ")
    p_phone = int(input("Phone Number: "))
    p_email = input("Email Address: ")
    p_salary = float(input("Salary: "))
    professor = Professor(p_name, p_phone, p_email, p_salary)

    # Output
    student.print_info()
    professor.print_info()
