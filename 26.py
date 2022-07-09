

employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee_file.readline()[1])
    employee_file.close()




