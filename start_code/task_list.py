
tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# print a list of tasks, completed if argument 2 = True, uncompleted if False
def list_tasks(list, boolean):
    ones_we_want = []
    for task in list:
        if task["completed"] == boolean:
            ones_we_want.append(task["description"])
        
    print(ones_we_want)

# list_tasks(tasks, False)

# 3. Print a list of all task descriptions

def list_all(list):
    all_tasks = []
    for task in list:
        all_tasks.append(task["description"])
    print(all_tasks)

# list_all(tasks)

# 4. Print a list of tasks where time_taken is at least a given time

def long_tasks(list, time):
    longer_tasks = []
    for task in list:
        if task["time_taken"] > time:
            longer_tasks.append(task["description"])
    print(longer_tasks)

# long_tasks(tasks, 20)

# 5. Print any task with a given description

def particular_task(list, description):
    particular_task = None
    for task in list:
        if task["description"] == description:
            particular_task = task
    return particular_task


# particular_task(tasks, "Clean  dem Windows")

###############

# 6. Given a description update that task to mark it as complete.

def task_updater(list, description):
    if particular_task(list, description) != None:
        for task in list:
            if task["description"] == description:
                task["completed"] = True



# task_updater(tasks, "Wash Dishes")


# 7. Add a task to the list

new_task = { "description": "Water Plants", "completed": False, "time_taken": 15 }
tasks.append(new_task)
# print(tasks)


# ### Further Extensions

# 8. Use a while loop to display the following menu and allow the user to enter an option.




while (True):
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")
    line = input("Enter your option: ")
    if (line == "q"):
        break
    elif line == 1:
        list_all(tasks)
    elif line == 2:
        list_tasks(tasks, False)
    elif line == 3:
        list_tasks(tasks, True)
    elif line == 4:
        which_task = input("which task is complete? ")
        task_updater(tasks, which_task)
    # print(f"You typed: {line}")

