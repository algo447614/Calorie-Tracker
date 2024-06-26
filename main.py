class CalorieTracker:
    def __init__(self):
        self.meals = {}

    def add_meal(self, meal_name, calories):
        if meal_name in self.meals:
            self.meals[meal_name] += calories
        else:
            self.meals[meal_name] = calories

    def remove_meal(self, meal_name):
        if meal_name in self.meals:
            del self.meals[meal_name]
            print(f"{meal_name} removed from the tracker.")
        else:
            print(f"{meal_name} not found in the tracker.")

    def get_total_calories(self):
        return sum(self.meals.values())

    def display_meals(self):
        print("Meals:")
        for meal, calories in self.meals.items():
            print(f"{meal}: {calories} calories")
        print(f"Total calories: {self.get_total_calories()}")

def main():
    tracker = CalorieTracker()

    while True:
        print("\nMenu:")
        print("1. Add a meal")
        print("2. Remove a meal")
        print("3. Display meals")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            meal_name = input("Enter meal name: ")
            calories = int(input("Enter calorie count: "))
            tracker.add_meal(meal_name, calories)
            print("Meal added successfully.")
        elif choice == "2":
            meal_name = input("Enter meal name to remove: ")
            tracker.remove_meal(meal_name)
        elif choice == "3":
            tracker.display_meals()
        elif choice == "4":
            print("Exiting the calorie tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
