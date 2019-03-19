class TaskStatus:
    TO_DO = 1
    DOING = 2
    DONE = 3

    def list(self=None):
        return [
            TaskStatus.TO_DO,
            TaskStatus.DOING,
            TaskStatus.DONE,
        ]
