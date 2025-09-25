class Professor:

    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print(f"Professor Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")