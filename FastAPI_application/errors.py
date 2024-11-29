class ValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)

class FileNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)

class UserNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)

class TaskNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)