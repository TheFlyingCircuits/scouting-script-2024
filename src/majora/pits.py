class Pits:
    """Represents a single team's pit scouting data"""

    def __init__(self):
        self.weight = 0
        self.speed = 0
        self.drive_train = None
        self.robot_abilities = None
        self.can_leave_starting_zone = None
        self.preferred_starting_position = None
        self.where_robot_can_score = None
        self.how_robot_scores = None
        self.climb = None

    def __repr__(self) -> str:
        return self.__dict__.__repr__()

    def update(self, row: list):
        self.weight = row[3]
        self.speed = row[4]
        self.drive_train = row[5]
        self.robot_abilities = row[6].split(";")
        self.can_leave_starting_zone = (row[7] == "Yes")
        # Skip notes they say they can score, which is columns 8 and 9
        self.preferred_starting_position = row[10]
        self.where_robot_can_score = row[11].split(";")
        self.how_robot_scores = row[12]
        self.climb = (row[13] == "Can balance on chain")
