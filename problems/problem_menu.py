def get_problem_choice(problems):
    while True:
        print("\nChoose problems (enter '0' to finish):")
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem} - {problems[problem]} NIS")

        try:
            choice = int(input("Enter problem number: "))
            if choice == 0:
                return None
            elif 1 <= choice <= len(problems):
                return list(problems.keys())[choice - 1]
            else:
                print("Invalid problem number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
