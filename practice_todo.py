"""AI-assisted task-management demonstration with synthetic fixtures."""
class Task:
    def __init__(self, title, status="ToDo"):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("A non-empty title is required")
        if status not in {"ToDo", "Done"}:
            raise ValueError("Status must be ToDo or Done")
        self.title = title
        self.status = status
        self.completed = status == "Done"

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        return f"{self.title} - {self.status}"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"


class TaskPool:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not isinstance(task, Task):
            raise TypeError("Expected Task")
        self.tasks.append(task)

    def populate(self):
        # Synthetic teaching fixtures, not claims about actual project completion.
        titles = ["Define API contract", "Create mock response", "Check missing fields",
                  "Evaluate model quality", "Review permissions", "Record user feedback"]
        self.tasks = [Task(title, "Done" if i < 3 else "ToDo") for i, title in enumerate(titles)]

    def get_open_tasks(self):
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        return [task for task in self.tasks if task.status == "Done"]


if __name__ == "__main__":
    pool = TaskPool()
    pool.populate()
    print("ToDo Tasks:")
    for task in pool.get_open_tasks():
        print(task.title)
    print("Done Tasks:")
    for task in pool.get_done_tasks():
        print(task.title)
