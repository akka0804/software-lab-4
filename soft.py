employee_data = [
    {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary": 56000},
    {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary": 67500},
    {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary": 82100},
    {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary": 44000},
]

def print_employee_data(data):
    print("{:<12} {:<10} {:<4} {:<8}".format("Employee ID", "Name", "Age", "Salary"))
    for emp in data:
        print("{:<12} {:<10} {:<4} {:<8}".format(emp["Employee ID"], emp["Name"], emp["Age"], emp["Salary"]))

def sort_employee_data(data, key):
    return sorted(data, key=lambda x: x[key])

while True:
    print("\nOptions:")
    print("1. Sort by Age")
    print("2. Sort by Name")
    print("3. Sort by Salary")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        sorted_data = sort_employee_data(employee_data, "Age")
        print_employee_data(sorted_data)
    elif choice == "2":
        sorted_data = sort_employee_data(employee_data, "Name")
        print_employee_data(sorted_data)
    elif choice == "3":
        sorted_data = sort_employee_data(employee_data, "Salary")
        print_employee_data(sorted_data)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a valid option.")
