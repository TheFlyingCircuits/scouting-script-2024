from majora.pits import Pits
from majora.stats import TeamStats


class Team:
    """Represents one team and all of its field & pit scouting data."""

    def __init__(self, team_number):
        self.team_number = team_number
        self.matches = []
        self.pits = Pits()
        self.stats = TeamStats()

    @property
    def num_matches(self):
        return len(self.matches)

    @property
    def avg_pts_auto(self):
        # 2 pts for amp in auto
        # 5 pts for speaker in auto

        total_points_auto = 0

        for match in self.matches:
            # Add points from a single match to the total
            total_points_auto += match.total_pts_auto()

        average = total_points_auto / self.num_matches if self.num_matches else 0

        return average

    @property
    def avg_pts_tele(self):
        # 1 pts for amp
        # 2 pts for speaker

        total_points_tele = 0

        for match in self.matches:
            total_points_tele += match.total_pts_tele()

        average = total_points_tele / self.num_matches if self.num_matches else 0

        return average

    @property
    def avg_pts_speaker(self):
        # 5 pts for auto
        # 2 pts for tele

        total_points_speaker = 0

        for match in self.matches:

            total_points_speaker += match.total_pts_speaker()

        average = total_points_speaker / self.num_matches if self.num_matches else 0

        return average

    @property
    def avg_pts_amp(self):
        # auto 2
        # tele 1
        total_points_amp = 0

        for match in self.matches:
            total_points_amp += match.total_pts_amp()

        average = total_points_amp / self.num_matches if self.num_matches else 0

        return average

    @property
    def avg_notes_auto(self):
        total_amp = sum([match.notes_scored_in_amp_auto for match in self.matches])
        total_speaker = sum([match.notes_scored_in_speaker_auto for match in self.matches])

        return (total_amp + total_speaker) / self.num_matches if self.num_matches else 0

    @property
    def avg_notes_tele(self):
        total_amp = sum([match.notes_scored_in_amp_tele for match in self.matches])
        total_speaker = sum([match.notes_scored_in_speaker_tele for match in self.matches])

        return (total_amp + total_speaker) / self.num_matches if self.num_matches else 0

    @property
    def avg_notes_amp(self):
        total_auto = sum([match.notes_scored_in_amp_auto for match in self.matches])
        total_tele = sum([match.notes_scored_in_amp_tele for match in self.matches])

        return (total_auto + total_tele) / self.num_matches if self.num_matches else 0

    @property
    def avg_notes_speaker(self):
        total_auto = sum([match.notes_scored_in_speaker_auto for match in self.matches])
        total_tele = sum([match.notes_scored_in_speaker_tele for match in self.matches])

        return (total_auto + total_tele) / self.num_matches if self.num_matches else 0

    @property
    def avg_rating_auto(self):
        return sum([match.rating_auto_quantified for match in self.matches]) / self.num_matches if self.num_matches else 0

    @property
    def avg_rating_speed(self):
        return sum([match.rating_speed_quantified for match in self.matches]) / self.num_matches if self.num_matches else 0

    @property
    def avg_rating_pickup(self):
        return sum([match.rating_pickup_quantified for match in self.matches]) / self.num_matches if self.num_matches else 0

    @property
    def avg_rating_scoring(self):
        return sum([match.rating_scoring_quantified for match in self.matches]) / self.num_matches if self.num_matches else 0

    @property
    def avg_rating_driver(self):
        return sum([match.rating_driver_quantified for match in self.matches]) / self.num_matches if self.num_matches else 0

    @property
    def avg_rating_balance(self):
        return sum([match.rating_balance_quantified for match in self.matches]) / self.num_matches if self.num_matches else 0

    @property
    def avg_rating_pick(self):
        return sum([match.rating_pick_quantified for match in self.matches]) / self.num_matches if self.num_matches else 0

    @property
    def total_notes_amp(self):
        return sum([match.total_notes_amp for match in self.matches])

    @property
    def total_notes_speaker(self):
        return sum([match.total_notes_speaker for match in self.matches])
