# Data Models and Types

## User Model
class User:
    def __init__(self, user_id: int, username: str, email: str):
        self.user_id = user_id  # Unique identifier for the user
        self.username = username  # Username of the user
        self.email = email  # Email address of the user

## Task Model
class Task:
    def __init__(self, task_id: int, user_id: int, title: str, completed: bool = False):
        self.task_id = task_id  # Unique identifier for the task
        self.user_id = user_id  # ID of the user associated with the task
        self.title = title  # Title of the task
        self.completed = completed  # Completion status

## Project Model
class Project:
    def __init__(self, project_id: int, name: str, user_id: int):
        self.project_id = project_id  # Unique identifier for the project
        self.name = name  # Name of the project
        self.user_id = user_id  # ID of the user who created the project
