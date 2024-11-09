import json

with open("user_data.json") as file:
    json_data = json.load(file)

def read_file():
    if json_data.get('departments'):
        for department in json_data['departments']:
            if department.get('employees'):
                for employee in department['employees']:
                    if employee['role'] == 'Manager' and employee['age'] > 30:
                        print(employee)



# r = read_file()

    with open("filtered_users.json", "w") as new_file:
        json.dump(employee, new_file, indent=4)

r = read_file()
