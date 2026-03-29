class EmployePayrole:
    employees = {}
    def __init__(self):
        self.ranks = {'1stofficer':12,'2ndofficer':10,'3rdofficer':8,'manager':5}
        
    def add(self,name,rank):
        if rank in self.ranks.keys():
            EmployePayrole.employees[name] = rank
            print('SUCCESS')
            return EmployePayrole.employees
        else:
            print('Invalid Positon')
    def weigh(self,rank):
        if rank in self.ranks.keys():
            print(f"{rank} weighs {self.ranks[rank]}$/6 week")
        else:
            print('Invalid position')
    def show(self):
        for k,v in EmployePayrole.employees.items():
            print(f"\n{k} as {v}")
##
##
class EmployeePayroll:

    employees = {}

    def __init__(self):
        self.ranks = {
            "1stofficer": 12,
            "2ndofficer": 10,
            "3rdofficer": 8,
            "manager": 5
        }

    def add_employee(self, name, rank):
        if rank in self.ranks:
            EmployeePayroll.employees[name] = rank
            print("Employee added successfully")
        else:
            print("Invalid position")

    def show_salary(self, rank):
        if rank in self.ranks:
            print(f"{rank} earns {self.ranks[rank]}$/6 week")
        else:
            print("Invalid position")

    def show_employees(self):
        print("\nEmployees List:")
        for name, rank in EmployeePayroll.employees.items():
            print(f"{name} -> {rank}")
#chatgpt
class EmployeePayroll:

    def __init__(self):
        # salary rate per rank
        self.ranks = {
            "1st_officer": 12,
            "2nd_officer": 10,
            "3rd_officer": 8,
            "manager": 5
        }

        # employee storage
        self.employees = {}

    def add_employee(self, name, rank, weeks):
        if rank not in self.ranks:
            print("Invalid position")
            return
        
        pay = self.ranks[rank] * weeks
        self.employees[name] = {
            "rank": rank,
            "weeks": weeks,
            "salary": pay
        }

        print(f"{name} added successfully.")

    def show_employee(self, name):
        if name in self.employees:
            e = self.employees[name]
            print(f"{name} | Rank: {e['rank']} | Weeks: {e['weeks']} | Salary: {e['salary']}$")
        else:
            print("Employee not found.")

    def show_all(self):
        print("\nEmployee Payroll List")
        for name, info in self.employees.items():
            print(f"{name} | {info['rank']} | Weeks: {info['weeks']} | Salary: {info['salary']}$")
payroll = EmployeePayroll()

payroll.add_employee("Ghost", "1st_officer", 6)
payroll.add_employee("Wizard", "2nd_officer", 6)
payroll.add_employee("Witch", "3rd_officer", 6)
payroll.add_employee("Valk", "manager", 6)

payroll.show_employee("Ghost")

payroll.show_all()
