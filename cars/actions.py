from problems.problem_menu import get_problem_choice
from problems.problems import problems




def add_car(cars, problems):
    name = input("Enter car name: ").capitalize()

    while True:
        number = input("Enter car number : ")
        if number.isdigit():
            break
        else:
            print("Invalid car number. Please enter digits only.")

    car_problems = []
    total_cost = 0

    while True:
        selected_problem = get_problem_choice(problems)
        if selected_problem is None:
            break
        car_problems.append(selected_problem)
        total_cost += problems[selected_problem]
        print(f"Added problem: {selected_problem} (Cost: {problems[selected_problem]} NIS)")

    print(f"\nTotal cost of repairs: {total_cost} NIS")
    confirm = input("Do you wish to proceed? (yes/no): ")

    if confirm.lower() == 'yes':
        cars[name] = {"number": number, "problems": car_problems, "total_cost": total_cost}
        print(f"Car {name} added successfully!")
    else:
        print("Car not added.")



def remove_car(cars):
    name = input("Enter car name to remove: ").capitalize()
    if name in cars:
        del cars[name]
        print(f"Car {name} removed.")
    else:
        for car_name in cars.keys():
            if car_name.lower() == name.lower():
                del cars[car_name]
                print(f"Car {car_name} removed.")
                return

        print(f"Car {name} not found.")



def search_car(cars):
    search_str = input("Enter car name or number to search: ")
    found_cars = []
    for name, info in cars.items():
        if (search_str.lower() in name.lower() or search_str in info['number']):
            found_cars.append((name, info['number'], info['problems']))

    if found_cars:
        print("Found the following cars:")
        for car in found_cars:
            print(f"Name: {car[0]}, Number: {car[1]}, Problems: {car[2]}")
    else:
        print("No cars found.")


def list_cars(cars, problems):
    if cars:
        print("\nList of cars:")
        for name, info in cars.items():
            problems_list = info['problems']
            total_cost = sum(problems[p] for p in problems_list)
            print(f"{name}: Number - {info['number']}, Problems - {problems_list}, Total Cost - {total_cost} NIS")
    else:
        print("No cars in the system.")
