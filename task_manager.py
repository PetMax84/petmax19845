class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False  # False = не выполнено, True = выполнено

    def mark_completed(self):
        self.status = True

    def __str__(self):
        status_str = "Выполнено" if self.status else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status_str}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Неверный индекс задачи")

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.status]

    def print_current_tasks(self):
        current_tasks = self.get_current_tasks()
        if not current_tasks:
            print("Нет текущих задач")
        else:
            for i, task in enumerate(current_tasks):
                print(f"{i + 1}. {task}")