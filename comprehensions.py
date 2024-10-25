# comprehensions.py

# Sample employee list, each element is a dictionary with 'name' and 'department'
employee_list = [
    {'name': 'Lisa', 'department': 'Cold Storage', 'id': 101},
    {'name': 'Tom', 'department': 'Produce', 'id': 102},
    {'name': 'Jerry', 'department': 'Bakery', 'id': 103},
    {'name': 'Anna', 'department': 'Dairy', 'id': 104}
]

def mod(employee):
    """
    Returns a formatted string combining the employee's name and department.
    :param employee: dict, contains 'name' and 'department' keys.
    :return: str, formatted as 'Name_Department'.
    """
    return f"{employee['name']}_{employee['department']}"

def to_mod_list(employee_list):
    """
    Applies the mod() function to all elements in employee_list using map().
    :param employee_list: list of dicts, each representing an employee.
    :return: list, modified strings for each employee.
    """
    # Apply map() with mod() to the employee list
    map_emp = map(mod, employee_list)
    # Convert the map object to a list and return
    return list(map_emp)

def generate_usernames(mod_list):
    """
    Generates usernames by replacing spaces with underscores.
    :param mod_list: list, modified employee strings.
    :return: list, usernames with underscores instead of spaces.
    """
    # Use list comprehension to replace spaces with underscores
    return [employee.replace(" ", "_") for employee in mod_list]

def map_id_to_initial(employee_list):
    """
    Creates a dictionary mapping employee's first initials to their IDs.
    :param employee_list: list of dicts, each representing an employee.
    :return: dict, keys are initials and values are employee IDs.
    """
    # Use dictionary comprehension to create a mapping of initials to IDs
    return {employee['name'][0]: employee['id'] for employee in employee_list}

# Main function to test the implemented functions
if __name__ == "__main__":
    # Step 1: Get the modified list using to_mod_list()
    mod_list = to_mod_list(employee_list)
    print("Modified List:", mod_list)

    # Step 2: Generate usernames from the modified list
    usernames = generate_usernames(mod_list)
    print("Usernames:", usernames)

    # Step 3: Map employee initials to IDs
    initials_to_ids = map_id_to_initial(employee_list)
    print("Initials to IDs:", initials_to_ids)
