from pawpal_system import Owner, Pet, Task, Scheduler


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
    task1 = Task("Morning walk", 20, "high", "exercise", "morning")
    task2 = Task("Feed Mochi", 10, "high", "feeding", "morning")
    task3 = Task("Play with Luna", 15, "medium", "play", "afternoon")
    task4 = Task("Groom Mochi", 30, "low", "grooming", "evening")

    # Assign tasks to pets
    pet1.add_task(task1)
    pet1.add_task(task2)
    pet1.add_task(task4)

    pet2.add_task(task3)

    # Create scheduler
    scheduler = Scheduler(owner)

    # Build schedule
    schedule = scheduler.build_schedule()

    # Print schedule
    print("\nToday's Schedule:\n")

    for i, task in enumerate(schedule, 1):
        print(f"{i}. {task.title}")
        print(f"   Duration: {task.duration_minutes} mins")
        print(f"   Priority: {task.priority}")
        print(f"   Time: {task.preferred_time}\n")

    # Print explanations
    print("Why these tasks were chosen:\n")
    explanations = scheduler.explain_schedule(schedule)
    for exp in explanations:
        print(f"- {exp}")


if __name__ == "__main__":
    main()