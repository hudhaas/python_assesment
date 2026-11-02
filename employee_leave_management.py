
class Employee:

    def __init__(self, emp_id, emp_name, emp_department, available_leaves):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_department = emp_department
        self.available_leaves = available_leaves

    def apply_leave(self, leave_days):

        if leave_days <= 0:
            print("Invalid Leave Request")

        elif leave_days <= self.available_leaves:
            self.available_leaves -= leave_days
            print("Leave Approved")

        else:
            print("Insufficient Leave Balance")

    def cancel_leave(self, leave_days):

        if leave_days > 0:
            self.available_leaves += leave_days
        else:
            print("Invalid Cancellation")

    def check_balance(self):
        print(f"Leave Balance: {self.available_leaves}")

    def display_employee(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Department: {self.emp_department}")
        print(f"Leave Balance: {self.available_leaves}")


emp_id = input("Employee Id: ")
emp_name = input("Name: ")
emp_department = input("Department: ")
available_leaves = int(input("Leave balance: "))

number_of_operations = int(input("Enter number of operations: "))

print()
print("=" * 30)

employee = Employee(emp_id, emp_name, emp_department, available_leaves)

print("Operations")
print()
print("Apply\nBalance\nCancel\nDisplay\n")

for i in range(number_of_operations):

    operation = input("Enter operation: ").lower()

    if operation == "apply":
        leave_days = int(input("Enter days: "))
        employee.apply_leave(leave_days)
        print("-" * 20)

    elif operation == "cancel":
        leave_days = int(input("Enter days: "))
        employee.cancel_leave(leave_days)
        print("-" * 20)

    elif operation == "balance":
        employee.check_balance()
        print("-" * 20)

    elif operation == "display":
        employee.display_employee()
        print("-" * 20)
