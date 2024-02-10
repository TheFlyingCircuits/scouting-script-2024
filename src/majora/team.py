from majora import Pits


class Team:
    """Represents one team and all of its field & pit scouting data."""

    def __init__(self, team_number):
        self.team_number = team_number
        self.matches = []
        self.pits = Pits()

    def __repr__(self) -> str:
        return self.__dict__.__repr__()

    def average_points_auto(self):
        # 2 pts for amp in auto
        # 5 pts for speaker in auto

        total_points_auto = 0

        for match in self.matches:
            # Add points from a single match to the total
            total_points_auto += match.total_pts_auto()

        number_of_matches = len(self.matches)
        average = total_points_auto / number_of_matches

        return average

    def average_points_tele(self):
        # 1 pts for amp
        # 2 pts for speaker

        total_points_tele = 0

        for match in self.matches:
            total_points_tele += match.total_pts_tele()

        number_of_matches = len(self.matches)
        average = total_points_tele / number_of_matches

        return average

    def average_points_speaker(self):
        # 5 pts for auto
        # 2 pts for tele

        total_points_speaker = 0

        for match in self.matches:

            total_points_speaker += match.total_pts_speaker()

        number_of_matches = len(self.matches)
        average = total_points_speaker / number_of_matches

        return average

    def average_points_amp(self):
        # auto 2
        # tele 1
        total_points_amp = 0

        for match in self.matches:
            total_points_amp += match.total_pts_amp()

        number_of_matches = len(self.matches)
        average = total_points_amp / number_of_matches

        return average
