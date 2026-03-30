import streamlit as st
from datetime import datetime
from pawpal_system import Owner, Pet, Task, Scheduler

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan", available_time=120)

if "pet" not in st.session_state:
    st.session_state.pet = Pet(name="Mochi", species="dog", age=1)
    st.session_state.owner.add_pet(st.session_state.pet)

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
available_time = st.number_input(
    "Available time today (minutes)",
    min_value=1,
    max_value=600,
    value=st.session_state.owner.available_time
)

st.session_state.owner.name = owner_name
st.session_state.owner.update_available_time(int(available_time))
st.session_state.pet.name = pet_name
st.session_state.pet.species = species

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

col4, col5, col6 = st.columns(3)
with col4:
    category = st.text_input("Category", value="general")
with col5:
    preferred_time = st.selectbox(
        "Preferred time",
        ["morning", "afternoon", "evening"],
        index=0
    )
with col6:
    frequency = st.selectbox(
        "Frequency",
        ["none", "daily", "weekly"],
        index=0
    )

if st.button("Add task"):
    new_task = Task(
        title=task_title,
        duration_minutes=int(duration),
        priority=priority,
        category=category,
        preferred_time=preferred_time,
        frequency=None if frequency == "none" else frequency,
        due_date=datetime.now()
    )
    st.session_state.pet.add_task(new_task)
    st.session_state.tasks.append(
        {
            "title": task_title,
            "duration_minutes": int(duration),
            "priority": priority,
            "category": category,
            "preferred_time": preferred_time,
            "frequency": frequency,
            "completed": False
        }
    )
    st.success(f"Added task: {task_title}")

if st.session_state.pet.tasks:
    st.write("Current tasks:")

    status_filter = st.selectbox(
        "Filter current tasks by status",
        ["all", "completed", "incomplete"],
        index=0
    )

    scheduler = Scheduler(st.session_state.owner)
    pet_tasks = st.session_state.pet.tasks

    if status_filter == "completed":
        filtered_tasks = scheduler.filter_tasks_by_status(pet_tasks, True)
    elif status_filter == "incomplete":
        filtered_tasks = scheduler.filter_tasks_by_status(pet_tasks, False)
    else:
        filtered_tasks = pet_tasks

    current_task_data = []
    for task in filtered_tasks:
        current_task_data.append(
            {
                "title": task.title,
                "duration_minutes": task.duration_minutes,
                "priority": task.priority,
                "category": task.category,
                "preferred_time": task.preferred_time,
                "frequency": task.frequency if task.frequency else "none",
                "completed": task.completed
            }
        )

    st.table(current_task_data)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    scheduler = Scheduler(st.session_state.owner)
    schedule = scheduler.build_schedule()
    sorted_schedule = scheduler.sort_by_time(schedule)
    explanations = scheduler.explain_schedule(sorted_schedule)
    conflicts = scheduler.detect_conflicts(sorted_schedule)

    if sorted_schedule:
        st.success("Schedule generated successfully.")

        schedule_data = []
        for task in sorted_schedule:
            schedule_data.append(
                {
                    "title": task.title,
                    "duration_minutes": task.duration_minutes,
                    "priority": task.priority,
                    "category": task.category,
                    "preferred_time": task.preferred_time,
                    "frequency": task.frequency if task.frequency else "none",
                    "completed": task.completed
                }
            )

        st.write("Generated Schedule:")
        st.table(schedule_data)

        if conflicts:
            st.write("### Conflict Warnings")
            for conflict in conflicts:
                st.warning(conflict)
        else:
            st.info("No task conflicts detected.")

        st.write("Why these tasks were chosen:")
        for explanation in explanations:
            st.write(f"- {explanation}")
    else:
        st.warning("No tasks fit within the available time.")

    st.markdown(
        """
Suggested approach:
1. Design your UML (draft).
2. Create class stubs (no logic).
3. Implement scheduling behavior.
4. Connect your scheduler here and display results.
"""
    )