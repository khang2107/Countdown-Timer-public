class Meeting:
    def __init__(self, name, password, duration):
        self.name = name
        self.password = password
        self.duration = duration

    def __str__(self):
        return f"{self.name} - {self.duration} seconds"
