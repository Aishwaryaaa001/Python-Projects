def task_management_app():
    tasks = []
    print("---WELCOME TO THE TASK MANAGEMENT APP---")
    
    # Initial task input
    try:
        total_task = int(input("Enter how many tasks you want to add: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print(f"Today's tasks are: {tasks}")

    while True:
        print("\nEnter an option:")
        print("1 - Add Task")
        print("2 - Update Task")
        print("3 - Delete Task")
        print("4 - View Tasks")
        print("5 - Exit")

        try:
            operation = int(input("Select an option (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if operation == 1:
            add_task = input("Enter the task you want to add: ")
            tasks.append(add_task)
            print(f"Task '{add_task}' has been successfully added.")
        elif operation == 2:
            view_tasks(tasks)  # Show current tasks for reference
            task_to_update = input("Enter the task name you want to update: ")
            if task_to_update in tasks:
                new_task = input("Enter the new task: ")
                index = tasks.index(task_to_update)
                tasks[index] = new_task
                print(f"Updated task to '{new_task}'.")
            else:
                print("Task not found.")
        elif operation == 3:
            view_tasks(tasks)  # Show current tasks for reference
            task_to_delete = input("Enter the task name you want to delete: ")
            if task_to_delete in tasks:
                tasks.remove(task_to_delete)
                print(f"Task '{task_to_delete}' has been deleted.")
            else:
                print("Task not found.")
        elif operation == 4:
            view_tasks(tasks)
        elif operation == 5:
            print("Exiting the task management app.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")

def view_tasks(tasks):
    if tasks:
        print("Current tasks are:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks available.")

# Run the task management app
task_management_app()
