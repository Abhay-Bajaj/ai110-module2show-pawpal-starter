from datetime import datetime
from pawpal_system import Owner, Pet, Task, Scheduler


def print_tasks(title, tasks):
    print(f"\n{title}\n")
    if not tasks:
        print("No tasks found.\n")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.title}")
        print(f"   Duration: {task.duration_minutes} mins")
        print(f"   Priority: {task.priority}")
        print(f"   Time: {task.preferred_time}")
        print(f"   Completed: {task.completed}")
        print(f"   Frequency: {task.frequency}")
        print(f"   Due Date: {task.due_date.strftime('%Y-%m-%d')}\n")


def main():
    # Create owner
    owner = Owner(name="Jordan", available_time=60)

    # Create pets
    pet1 = Pet(name="Mochi", species="dog", age=3)
    pet2 = Pet(name="Luna", species="cat", age=2)

    # Add pets to owner
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    # Create tasks
    task1 = Task(
        "Groom Mochi",
        30,
        "low",
        "grooming",
        "evening",
        due_date=datetime.now()
    )
    task2 = Task(
        "Feed Mochi",
        10,
        "high",
        "feeding",
        "morning",
        frequency="daily",
        due_date=datetime.now()
    )
    task3 = Task(
        "Play with Luna",
        15,
        "medium",
        "play",
        "morning",
        due_date=datetime.now()
    )
    task4 = Task(
        "Morning walk",
        20,
        "high",
        "exercise",
        "morning",
        frequency="weekly",
        due_date=datetime.now()
    )

    # Assign tasks to pets
    pet1.add_task(task1)
    pet1.add_task(task2)
    pet1.add_task(task4)
    pet2.add_task(task3)

    # Complete recurring tasks to generate next occurrences
    pet1.complete_task(task2)
    pet1.complete_task(task4)

    # Create scheduler
    scheduler = Scheduler(owner)

    # Print all tasks
    all_tasks = owner.get_all_tasks()
    print_tasks("All Tasks", all_tasks)

    # Detect conflicts
    conflicts = scheduler.detect_conflicts(all_tasks)
    print("\nConflict Warnings:\n")
    if conflicts:
        for warning in conflicts:
            print(warning)
    else:
        print("No task conflicts found.")

    # Print tasks sorted by time
    sorted_tasks = scheduler.sort_by_time(all_tasks)
    print_tasks("Tasks Sorted by Time", sorted_tasks)

    # Print completed tasks
    completed_tasks = scheduler.filter_tasks_by_status(all_tasks, True)
    print_tasks("Completed Tasks", completed_tasks)

    # Print incomplete tasks
    incomplete_tasks = scheduler.filter_tasks_by_status(all_tasks, False)
    print_tasks("Incomplete Tasks", incomplete_tasks)

    # Print tasks for Mochi
    mochi_tasks = scheduler.filter_tasks_by_pet_name("Mochi")
    print_tasks("Tasks for Mochi", mochi_tasks)

    # Build schedule
    schedule = scheduler.build_schedule()
    print_tasks("Today's Schedule", schedule)

    # Print explanations
    print("Why these tasks were chosen:\n")
    explanations = scheduler.explain_schedule(schedule)
    for exp in explanations:
        print(f"- {exp}")


if __name__ == "__main__":
    main()