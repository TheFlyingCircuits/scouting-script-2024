from majora import config, filtering
from majora.pits import Pits
from majora.stats import TeamStats


class Team:
    """Represents one team and all of its field & pit scouting data."""

    def __init__(self, team_number):
        self.team_number = team_number
        self.matches = []
        self.pits = Pits()
        self.stats = TeamStats()
        self.statbotics = {}

    def num_matches(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)
        return len(matches)

    def avg_pts_auto(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)

        # 2 pts for amp in auto
        # 5 pts for speaker in auto

        total_points_auto = 0

        for match in matches:
            # Add points from a single match to the total
            total_points_auto += match.total_pts_auto()

        average = total_points_auto / self.num_matches(day) if self.num_matches(day) else 0

        return average

    def avg_pts_tele(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)

        # 1 pts for amp
        # 2 pts for speaker

        total_points_tele = 0

        for match in matches:
            total_points_tele += match.total_pts_tele()

        average = total_points_tele / self.num_matches(day) if self.num_matches(day) else 0

        return average

    def avg_pts_speaker(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)

        # 5 pts for auto
        # 2 pts for tele

        total_points_speaker = 0

        for match in matches:

            total_points_speaker += match.total_pts_speaker()

        average = total_points_speaker / self.num_matches(day) if self.num_matches(day) else 0

        return average

    def avg_pts_amp(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)

        # auto 2
        # tele 1
        total_points_amp = 0

        for match in matches:
            total_points_amp += match.total_pts_amp()

        average = total_points_amp / self.num_matches(day) if self.num_matches(day) else 0

        return average

    def avg_notes_auto(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)

        total_amp = sum([match.notes_scored_in_amp_auto for match in matches])
        total_speaker = sum([match.notes_scored_in_speaker_auto for match in matches])

        return (total_amp + total_speaker) / self.num_matches(day) if self.num_matches(day) else 0

    def avg_notes_tele(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)

        total_amp = sum([match.notes_scored_in_amp_tele for match in matches])
        total_speaker = sum([match.notes_scored_in_speaker_tele for match in matches])

        return (total_amp + total_speaker) / self.num_matches(day) if self.num_matches(day) else 0

    def avg_notes_amp(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)

        total_auto = sum([match.notes_scored_in_amp_auto for match in matches])
        total_tele = sum([match.notes_scored_in_amp_tele for match in matches])

        return (total_auto + total_tele) / self.num_matches(day) if self.num_matches(day) else 0

    def avg_notes_speaker(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)

        total_auto = sum([match.notes_scored_in_speaker_auto for match in matches])
        total_tele = sum([match.notes_scored_in_speaker_tele for match in matches])

        return (total_auto + total_tele) / self.num_matches(day) if self.num_matches(day) else 0

    def avg_rating_auto(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)
        return sum([match.rating_auto_quantified for match in matches]) / self.num_matches(day) if self.num_matches(day) else 0

    def avg_rating_speed(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)
        return sum([match.rating_speed_quantified for match in matches]) / self.num_matches(day) if self.num_matches(day) else 0

    def avg_rating_pickup(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)
        return sum([match.rating_pickup_quantified for match in matches]) / self.num_matches(day) if self.num_matches(day) else 0

    def avg_rating_scoring(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)
        return sum([match.rating_scoring_quantified for match in matches]) / self.num_matches(day) if self.num_matches(day) else 0

    def avg_rating_driver(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)
        return sum([match.rating_driver_quantified for match in matches]) / self.num_matches(day) if self.num_matches(day) else 0

    def avg_rating_balance(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)
        return sum([match.rating_balance_quantified for match in matches]) / self.num_matches(day) if self.num_matches(day) else 0

    def avg_rating_pick(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)
        return sum([match.rating_pick_quantified for match in matches]) / self.num_matches(day) if self.num_matches(day) else 0

    def total_notes_amp(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)
        return sum([match.total_notes_amp for match in matches])

    def total_notes_speaker(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)
        return sum([match.total_notes_speaker for match in matches])

    def start_epa(self, _):
        return self.statbotics["epa_start"]

    def avg_epa(self, _):
        return self.statbotics["epa_mean"]

    def end_epa(self, _):
        return self.statbotics["epa_end"]

    def avg_rating_overall(self, day):
        return (self.avg_rating_auto(day) + self.avg_rating_balance(day) +
                self.avg_rating_driver(day) + self.avg_rating_pick(day) +
                self.avg_rating_pickup(day) + self.avg_rating_speed(day) +
                self.avg_rating_scoring(day)) / 7

    def avg_speaker_tele_notes(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)

        total_notes = sum([match.notes_scored_in_speaker_tele for match in matches])

        return (total_notes) / self.num_matches(day) if self.num_matches(day) else 0

    def rice_score(self, day):
        normalized_speaker_tele_avg = (self.avg_speaker_tele_notes(
            day) / config.HIGHEST_TELE_SPEAKER_NOTES) * 2 + 1

        return (normalized_speaker_tele_avg + self.avg_rating_driver(day) + self.avg_rating_speed(day)) / 3

    def defense_pct(self, day):
        matches = filtering.get_matches_from_day(self.matches, day)

        defense_total = 0

        for match in matches:
            if match.defense:
                defense_total += 1

        return defense_total / self.num_matches(day) if self.num_matches(day) else 0
