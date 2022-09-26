class Meet(object):
    def __init__(self, title='', duration='0h 0m', participants=-9999, prev_value=-9999, is_first=False):
        self.title = title
        self.duration = duration
        self.participants = participants
        self.prev_value = prev_value
        self.is_first = is_first

    def __eq__(self, other) -> bool:
        return self.title == other.title and self.duration == self.duration and self.participants == other.participants

    def __str__(self) -> str:
        return f'Title: {self.title}\nDuration: {self.duration}\nParticipants: {self.participants}\nPrev: {self.prev_value}\nIs_first: {self.is_first}'