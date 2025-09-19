class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def display_info(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}, Department: {self.department}"
    
class Manager(Employee):
    def __init__(self, name, emp_id, department, team_size):
        super().__init__(name, emp_id, department)
        self.team_size = team_size

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Team Size: {self.team_size}"
    
class Developer(Employee):
    def __init__(self, name, emp_id, department, programming_language):
        super().__init__(name, emp_id, department)
        self.programming_language = programming_language

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Programming Language: {self.programming_language}"
    
if __name__ == "__main__":
    
    manager = Manager("Bob", 102, "IT", 10)
    developer = Developer("Charlie", 103, "IT", "Python")

    print(manager.display_info())
    print(developer.display_info())
    