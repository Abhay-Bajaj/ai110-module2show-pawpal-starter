from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str
    category: str
    preferred_time: str

    def update_priority(self, priority: str):
        pass

    def update_duration(self, duration: int):
        pass

    def get_task_info(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    needs: list = field(default_factory=list)
    tasks: list = field(default_factory=list)

    def add_need(self, need: str):
        pass

    def view_info(self):
        pass


class Owner:
    def __init__(self, name: str, available_time: int, preferences: list = None):
        self.name = name
        self.available_time = available_time
        self.preferences = preferences or []

    def set_preferences(self, preferences: list):
        pass

    def update_available_time(self, time: int):
        pass

    def view_schedule(self, schedule: list):
        pass


class Scheduler:
    def __init__(self, owner: Owner, pet: Pet, tasks: list = None):
        self.owner = owner
        self.pet = pet
        self.tasks = tasks or []

    def prioritize_tasks(self):
        pass

    def filter_tasks_by_time(self):
        pass

    def build_schedule(self):
        pass

    def explain_schedule(self):
        pass