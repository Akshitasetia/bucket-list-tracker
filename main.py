import json

# Load and Save Functions

def load_goals():
    try:
        with open("goals.json", "r") as file:
            return json.load(file)
    except:
        return []


goals = load_goals()


def save_goals():
    with open("goals.json", "w") as file:
        json.dump(goals, file, indent=4)

# Goal Functions


def view_goals():
    if not goals:
        print("\nNo goals added yet 🌱")
        return

    print("\n📋 Your Goals")

    for goal in goals:
        status = "✓" if goal["completed"] else " "
        print(f"[{status}] {goal['goal']} - {goal['category']}")


def add_goal():
    goal_name = input("Enter a goal: ")
    category = input("Enter category: ")

    new_goal = {
        "goal": goal_name,
        "completed": False,
        "category": category
    }

    goals.append(new_goal)
    save_goals()

    print("Goal added successfully! 🎉")


def show_goals_with_numbers():
    if not goals:
        print("No goals available.")
        return

    for i, goal in enumerate(goals, start=1):
        status = "✓" if goal["completed"] else " "
        print(f"{i}. [{status}] {goal['goal']} - {goal['category']}")


def complete_goal():
    if not goals:
        print("No goals available.")
        return

    show_goals_with_numbers()

    try:
        choice = int(input("Enter goal number to complete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    index = choice - 1

    if index < 0 or index >= len(goals):
        print("Invalid choice 😅")
        return

    goals[index]["completed"] = True
    save_goals()

    print("Goal marked as completed! 🎉")


def delete_goal():
    if not goals:
        print("No goals available.")
        return

    show_goals_with_numbers()

    try:
        choice = int(input("Enter goal number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    index = choice - 1

    if index < 0 or index >= len(goals):
        print("Invalid choice 😅")
        return

    confirm = input("Are you sure? (y/n): ").lower()

    if confirm != "y":
        print("Deletion cancelled.")
        return

    removed = goals.pop(index)
    save_goals()

    print(f"Deleted: {removed['goal']}")


def edit_goal():
    if not goals:
        print("No goals available.")
        return

    show_goals_with_numbers()

    try:
        choice = int(input("Enter goal number to edit: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    index = choice - 1

    if index < 0 or index >= len(goals):
        print("Invalid choice 😅")
        return

    print("\nLeave blank to keep current value.")

    new_goal = input(
        f"New goal ({goals[index]['goal']}): "
    )

    new_category = input(
        f"New category ({goals[index]['category']}): "
    )

    if new_goal:
        goals[index]["goal"] = new_goal

    if new_category:
        goals[index]["category"] = new_category

    save_goals()

    print("Goal updated successfully ✨")


def search_goals():
    keyword = input("Enter keyword to search: ").lower()

    found = False

    for i, goal in enumerate(goals, start=1):
        if keyword in goal["goal"].lower():
            status = "✓" if goal["completed"] else " "
            print(f"{i}. [{status}] {goal['goal']} - {goal['category']}")
            found = True

    if not found:
        print("No matching goals found 😅")


# -------------------------
# Dashboard & Statistics
# -------------------------

def dashboard():
    total = len(goals)
    completed = sum(1 for goal in goals if goal["completed"])

    print("\n🌟 DASHBOARD")
    print("-" * 25)
    print("Total Goals :", total)
    print("Completed   :", completed)
    print("Remaining   :", total - completed)


def show_progress():
    total = len(goals)

    if total == 0:
        print("No goals yet 🌱")
        return

    completed = sum(1 for goal in goals if goal["completed"])

    percent = (completed / total) * 100

    bars = int(percent // 10)
    progress_bar = "#" * bars + "-" * (10 - bars)

    print("\n📊 Progress Report")
    print(f"Completed: {completed}/{total}")
    print(f"[{progress_bar}] {percent:.1f}%")


def category_stats():
    if not goals:
        print("No goals available.")
        return

    categories = {}

    for goal in goals:
        category = goal["category"]

        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

    print("\n📂 Category Statistics")
    print("-" * 25)

    for category, count in categories.items():
        print(f"{category}: {count}")

def filter_by_category():
    if not goals:
        print("No goals available.")
        return

    category = input("Enter category: ").lower()

    found = False

    print("\n📂 Goals in Category:", category)

    for goal in goals:
        if goal["category"].lower() == category:
            status = "✓" if goal["completed"] else " "
            print(f"[{status}] {goal['goal']}")

            found = True

    if not found:
        print("No goals found in that category.")


# -------------------------
# Main Program
# -------------------------

while True:
    dashboard()

    print("\n===== Bucket List Tracker =====")
    print("1. View Goals")
    print("2. Add Goal")
    print("3. Complete Goal")
    print("4. Delete Goal")
    print("5. Show Progress")
    print("6. Search Goals")
    print("7. Edit Goal")
    print("8. Category Statistics")
    print("9. Filter by Category")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        view_goals()

    elif choice == "2":
        add_goal()

    elif choice == "3":
        complete_goal()

    elif choice == "4":
        delete_goal()

    elif choice == "5":
        show_progress()

    elif choice == "6":
        search_goals()

    elif choice == "7":
        edit_goal()

    elif choice == "8":
        category_stats()

    elif choice == "9":
       filter_by_category()

    elif choice == "10":
      print("Goodbye 👋")
      break

    else:
        print("Invalid choice 😅")