from datetime import datetime, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler


def test_task_completion():
    task = Task("Feed", 10, "high", "feeding", "morning")
    task.mark_completed()
    assert task.completed is True


def test_task_addition():
    pet = Pet("Mochi", "dog", 3)
    task = Task("Walk", 20, "high", "exercise", "morning")

    initial_count = len(pet.tasks)
    pet.add_task(task)

    assert len(pet.tasks) == initial_count + 1


def test_sorting_correctness():
    owner = Owner("Jordan", 60)
    scheduler = Scheduler(owner)

    task1 = Task("Evening Groom", 20, "low", "grooming", "evening")
    task2 = Task("Morning Feed", 10, "high", "feeding", "morning")
    task3 = Task("Afternoon Play", 15, "medium", "play", "afternoon")

    tasks = [task1, task2, task3]
    sorted_tasks = scheduler.sort_by_time(tasks)

    assert sorted_tasks[0].title == "Morning Feed"
    assert sorted_tasks[1].title == "Afternoon Play"
    assert sorted_tasks[2].title == "Evening Groom"


def test_recurrence_logic_daily_task():
    pet = Pet("Mochi", "dog", 3)
    original_date = datetime.now()

    task = Task(
        "Feed Mochi",
        10,
        "high",
        "feeding",
        "morning",
        frequency="daily",
        due_date=original_date
    )

    pet.add_task(task)
    pet.complete_task(task)

    assert len(pet.tasks) == 2
    new_task = pet.tasks[1]
    assert new_task.title == "Feed Mochi"
    assert new_task.completed is False
    assert new_task.due_date.date() == (original_date + timedelta(days=1)).date()


def test_conflict_detection():
    owner = Owner("Jordan", 60)
    pet1 = Pet("Mochi", "dog", 3)
    pet2 = Pet("Luna", "cat", 2)

    owner.add_pet(pet1)
    owner.add_pet(pet2)

    task1 = Task("Feed Mochi", 10, "high", "feeding", "morning")
    task2 = Task("Play with Luna", 15, "medium", "play", "morning")

    pet1.add_task(task1)
    pet2.add_task(task2)

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts(owner.get_all_tasks())

    assert len(conflicts) > 0
    assert "morning" in conflicts[0].lower()