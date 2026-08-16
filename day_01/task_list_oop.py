class Task:
    def __init__(self,name):
        self.name = name
        self.completed = False
class TaskList:
    def __init__(self):
        self.tasks = []
    def add_task(self,name):
        task = Task(name)
        self.tasks.append(task)
    def complete_task(self,name):
        for task in self.tasks:
            if task.name == name:
                task.completed = True
    def list_tasks(self):
        for task in self.tasks:
            if task.completed:
                print('[x] '+ task.name)
            else:
                print('[ ]'+task.name)
tasks = TaskList()
tasks.add_task('Buy Milk')
tasks.add_task("Study Python")
tasks.complete_task('Buy Milk')
tasks.list_tasks()