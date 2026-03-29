# PawPal+ Project Reflection

## 1. System Design
1. Add and manage pet care tasks: The user should be able to create tasks such as feeding, walking, giving medication, grooming, or playtime. Each task should include details like duration, priority, and possibly a preferred time.
2. Generate a daily care schedule: The user should be able to ask the app to create a plan for the day based on the pet’s needs, the task priorities, the owner’s available time, and any preferences or constraints.
3. View and understand the final plan: The user should be able to see the ordered schedule clearly and understand why each task was included, such as because it was high priority, time-sensitive, or matched the owner’s available time.

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial UML design focused on four main classes: Owner, Pet, Task, and Scheduler. I kept the design simple so each class has a clear role and the system is easy to build and understand. The Owner class is responsible for storing information about the user, such as their name, available time, and preferences. It represents the person using the app and helps define the constraints for the schedule. The Pet class stores basic information about the pet, such as name, species, age, and needs. Its responsibility is to represent the pet and provide context for what kind of care is required. The Task class represents individual care activities like feeding, walking, or giving medication. Each task includes details like duration, priority, category, and preferred time. This class is important because it models everything that needs to be scheduled. The Scheduler class handles the main logic of the system. It takes the owner, pet, and list of tasks, then decides which tasks should be included and in what order. It is also responsible for explaining the final schedule. Overall, each class has a specific responsibility, which keeps the system organized and makes it easier to develop and test.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes, my design changed slightly during implementation. I updated the Scheduler class to include both the owner and the pet, since the schedule depends on both. I also cleaned up some method names to keep them consistent across classes. I also thought about adding a separate Schedule class, but kept the design with four classes to keep it simple.
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My scheduler considers constraints like available time, task priority, and preferred time of day. I prioritized task importance and available time the most, since high priority tasks should be completed first and everything must fit within the owner’s time.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff my scheduler makes is that it only checks for exact time matches like morning or evening instead of tracking detailed overlapping time ranges. This is reasonable because it keeps the scheduling logic simple and still gives the user a helpful warning when tasks may conflict.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
