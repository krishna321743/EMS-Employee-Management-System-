# EMS-Employee-Management-System-
#🚀 Python Project – Employee Management System . In this we use Python dictionaries and nested dictionaries,  #Functions and conditional statements , Menu-driven program development  and Basic problem-solving
#Create a dictionary to store the employee data
employee = {
    101: {
        'name': 'x',
        'age': 18,
        'department': 'hr',
        'salary': float('50000')
    },
    102: {
        'name': 'y',
        'age': 19,
        'department': 'ai development',
        'salary': float('50000')
    }
}

#add employee 
def add_emp():
    emp_id = int(input('ENTER EMPLOYEE ID: '))
#check the employee id already exist or not
    if emp_id in employee:
        print('Use a different employee ID!')
        return

    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    department = input('Enter your department: ')
    salary = float(input('Enter your salary: '))

    employee[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print('Successfully added!')

#view employee
def view_employee():
    for emp_id, details in employee.items():
        print('\nEmployee ID:', emp_id)
        print('Name:', details['name'])
        print('Age:', details['age'])
        print('Department:', details['department'])
        print('Salary:', details['salary'])

#search employee
def search_employee():
    emp_id = int(input('Enter employee ID to search: '))

    if emp_id in employee:
        print(employee[emp_id])
    else:
        print('Employee not found!')


while True:
    print('\n' + '=' * 10 + ' Menu Section ' + '=' * 10)
    print('1 for add employee data')
    print('2 for view all employee data')
    print('3 for search employee')
    print('4 for exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        add_emp()

    elif choice == '2':
        view_employee()

    elif choice == '3':
        search_employee()

    elif choice == '4':
        print('Program exited!')
        break

    else:
        print('Invalid choice!')
