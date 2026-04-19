project_title = input("Project title: ")

while project_title == "":
    print("Project title cannot be empty.")
    project_title = input("Project title: ")

group_name = input("Group name: ")

while group_name == "":
    print("Group name cannot be empty.")
    group_name = input("Group name: ")

task_names = [
    "Program Logic / Coding",
    "UI / Output Formatting",
    "Testing & Debugging",
    "Documentation / README",
    "Presentation Slides"
]

task_hours = [6, 3, 2, 2, 2]

print("\n==========================================")
print("        COM 103 PROJECT -- TASK TYPES     ")
print("==========================================")

i = 0
while i < 5:
    print(" " + str(i + 1) + ". " + task_names[i] + " [" + str(task_hours[i]) + "h]")
    i = i + 1

print("==========================================")

assigned_names = []
assigned_status = []
assigned_task = []
assigned_hours = []
assigned_points = []

count = 1
total_points = 0
max_points = 0

while count <= 4:
    print("\n--- TASK " + str(count) + " ---------------------------")

    task_num = input("Task number (0 to skip): ")

    while task_num == "":
        print("Task number cannot be empty.")
        task_num = input("Task number (0 to skip): ")

    task_num = int(task_num)

    if task_num == 0:
        count = count + 1

    elif task_num >= 1 and task_num <= 5:

        name = input("Member name: ")
        while name == "":
            print("Member name cannot be empty.")
            name = input("Member name: ")

        status = input("Status (done/pending): ")
        while status == "":
            print("Status cannot be empty.")
            status = input("Status (done/pending): ")

        if status == "done":
            points = 2
        else:
            points = 1

        assigned_names.append(name)
        assigned_status.append(status)
        assigned_task.append(task_names[task_num - 1])
        assigned_hours.append(task_hours[task_num - 1])
        assigned_points.append(points)

        total_points = total_points + points
        max_points = max_points + 2

        count = count + 1

    else:
        print("Invalid task number. Please enter 0–5.")

if max_points > 0:
    progress = int((total_points / max_points) * 100)
else:
    progress = 0

if progress >= 75:
    project_status = "PROJECT READY!"
elif progress >= 50:
    project_status = "ON TRACK."
else:
    project_status = "NEEDS MORE WORK!"

print("\n================================================")
print("        " + project_title + " -- TASK BOARD")
print("================================================")

print("\nProject : " + project_title)
print("Group   : " + group_name)
print("------------------------------------------------")

j = 0
display = 1

while j < len(assigned_names):
    print("[" + str(display) + "] " + assigned_task[j] + " [" + str(assigned_hours[j]) + "h]")
    print("    Assigned to : " + assigned_names[j])
    print("    Status      : " + assigned_status[j])
    print("    Points      : " + str(assigned_points[j]) + " / 2")
    print("")

    j = j + 1
    display = display + 1

print("------------------------------------------------")
print("Points Earned   : " + str(total_points) + " / " + str(max_points))
print("Progress        : " + str(progress) + "%")
print("Project Status  : " + project_status)
print("================================================") 