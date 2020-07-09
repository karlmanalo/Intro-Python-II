class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def print_welcome(self):
        print(f"Welcome to {self.name}! Which department would you like to visit?")

        for d in self.departments:
            print(d)

class Department:
    def __init__(self, id, name, products):
        self.id = id
        self.name = name
        self.products = products

    def __str__(self):
        return f"{self.id}: {self.name}"

store = Store("The Dugout", [
    Department(1, "Baseball", []),
    Department(2, "Basketball", []),
    Department(3, "Football", []),
    Department(4, "Golf", [])
])

while True:
    store.print_welcome()

    selection = input("Which department would you like to visit? \n")

    if selection == "quit":
        break

    chosen_department = store.departments[int(selection) - 1]
    
    print(f"You picked the {chosen_department.name} department. \n")