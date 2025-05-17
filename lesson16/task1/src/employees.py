class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)

class Manager(Employee):
    def __init__(self, department, **kwargs):
        self.department = department
        super().__init__(**kwargs)

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        self.programming_language = programming_language
        super().__init__(**kwargs)

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        self.team_size = team_size
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )
