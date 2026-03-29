from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    category: str
    preferred_time: str
    completed: bool = False

    def update_priority(self, priority: str):
        """Update the task's priority."""
        self.priority = priority

    def update_duration(self, duration: int):
        """Update the task duration in minutes."""
        self.duration_minutes = duration

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def get_task_info(self):
        """Return task details as a dictionary."""
        return {
            "title": self.title,
            "duration_minutes": self.duration_minutes,
            "priority": self.priority,
            "category": self.category,
            "preferred_time": self.preferred_time,
            "completed": self.completed
        }


@dataclass
class Pet:
    name: str
    species: str
    age: int
    needs: list = field(default_factory=list)
    tasks: list = field(default_factory=list)

    def add_need(self, need: str):
        """Add a need to the pet."""
        self.needs.append(need)

    def add_task(self, task: Task):
        """Add a task to the pet."""
        self.tasks.append(task)

    def view_info(self):
        """Return pet information."""
        return {
            "name": self.name,
            "species": self.species,
            "age": self.age,
            "needs": self.needs,
            "tasks": [task.get_task_info() for task in self.tasks]
        }


class Owner:
    def __init__(self, name: str, available_time: int, preferences: list = None):
        self.name = name
        self.available_time = available_time
        self.preferences = preferences or []
        self.pets = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner."""
        self.pets.append(pet)

    def set_preferences(self, preferences: list):
        """Set owner preferences."""
        self.preferences = preferences

    def update_available_time(self, time: int):
        """Update available time for tasks."""
        self.available_time = time

    def get_all_tasks(self):
        """Return all tasks from all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks

    def view_schedule(self, schedule: list):
        """Return the schedule in a readable format."""
        return [task.get_task_info() for task in schedule]


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def prioritize_tasks(self, tasks: list):
        """Sort tasks by priority."""
        priority_order = {"high": 3, "medium": 2, "low": 1}
        return sorted(
            tasks,
            key=lambda task: priority_order.get(task.priority.lower(), 0),
            reverse=True
        )

    def filter_tasks_by_time(self, tasks: list):
        """Filter tasks based on available time."""
        selected_tasks = []
        total_time = 0

        for task in tasks:
            if total_time + task.duration_minutes <= self.owner.available_time:
                selected_tasks.append(task)
                total_time += task.duration_minutes

        return selected_tasks

    def build_schedule(self):
        """Create a schedule based on priority and time."""
        all_tasks = self.owner.get_all_tasks()
        prioritized_tasks = self.prioritize_tasks(all_tasks)
        final_schedule = self.filter_tasks_by_time(prioritized_tasks)
        return final_schedule

    def explain_schedule(self, schedule: list):
        """Explain why each task was selected."""
        explanations = []
        for task in schedule:
            explanations.append(
                f"{task.title} was included because it is a {task.priority} priority task "
                f"and fits within the available time."
            )
        return explanations