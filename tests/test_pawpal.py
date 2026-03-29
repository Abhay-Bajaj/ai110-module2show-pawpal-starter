from pawpal_system import Task, Pet


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