from .actions import add_car, remove_car, search_car, list_cars
from problems.problems import problems


def main_menu(cars, problems):
    while True:
        total_cars = len(cars)
        total_profit = calculate_total_profit(cars, problems)
        print(f"\nCurrently there are {total_cars} cars. The current profit is: {total_profit} NIS")

        print("\nChoose an action:")
        print("1. Add car")
        print("2. Remove car")
        print("3. Search car")
        print("4. List all cars")
        print("5. Exit")

        try:
            user_input = int(input("Enter your choice: "))

            if user_input == 1:
                add_car(cars, problems)
            elif user_input == 2:
                remove_car(cars)
            elif user_input == 3:
                search_car(cars)
            elif user_input == 4:
                list_cars(cars, problems)
            elif user_input == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_total_profit(cars, problems):
    total_profit = 0
    for _, car_info in cars.items():
        total_profit += car_info.get("total_cost", 0)
    return total_profit