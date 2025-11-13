class Employee:
    def __init__(self, ism, lavozim, ish_haqi_maxfiy):
        self.ism = ism
        self.lavozim = lavozim
        self._ish_haqi = ish_haqi_maxfiy  

    def set_salary(self, yangi_haq):
        self._ish_haqi = yangi_haq

    def get_salary(self):
        if isinstance(self, Manager):
            return "maxfiy"
        else:
            return self._ish_haqi


class Manager(Employee):
    pass 


class HR(Employee):
    pass  


hr = HR("Ali", "HR Specialist", 5000)
manager = Manager("Vali", "Project Manager", 8000)
employee = Employee("Soli", "Developer", 6000)


print(f"{hr.ism} ish haqi: {hr.get_salary()}")        # 5000
print(f"{manager.ism} ish haqi: {manager.get_salary()}")  # maxfiy
print(f"{employee.ism} ish haqi: {employee.get_salary()}") # 6000


hr.set_salary(5500)
print(f"{hr.ism} yangi ish haqi: {hr.get_salary()}")  # 5500
