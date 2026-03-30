# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## Smarter Scheduling

PawPal+ now includes smarter scheduling features to make the daily plan more useful. Tasks can be sorted by preferred time of day, filtered by completion status or pet name, and checked for simple scheduling conflicts. The system also supports recurring daily and weekly tasks by automatically creating the next task occurrence when one is completed.

## Testing PawPal+

The test suite verifies the core functionality of the PawPal+ system. It includes tests for task creation and completion, adding tasks to pets, sorting tasks by time, recurring task behavior, and conflict detection when multiple tasks are scheduled at the same time.

My confidence level for the system's reliability would be 5 stars. Based on the passing test results, the system appears reliable for the core features implemented. The tests cover both normal behavior and important edge cases, giving confidence that the scheduling logic works as expected.

To run the automated tests, use:

```bash
python -m pytest


