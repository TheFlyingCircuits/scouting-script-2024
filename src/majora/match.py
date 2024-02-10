from majora import util


class Match:
    """Represents a single team's match data"""

    def __init__(self, row):
        self.match_number = int(row[3])

        if row[4].lower() == "yes":
            self.left_starting_zone = True
        else:
            self.left_starting_zone = False

        self.notes_scored_in_amp_auto = util.extract_max_value(row[5])
        self.notes_scored_in_speaker_auto = util.extract_max_value(row[6])
        self.notes_scored_in_amp_tele = util.extract_max_value(row[7])
        self.notes_scored_in_speaker_tele = util.extract_max_value(row[8])
        self.parked = (row[9] == "Yes")
        self.onstage_without_harmony = row[10]
        self.onstage_with_harmony = row[11]
        self.notes_scored_in_trap = util.extract_max_value(row[12])
        self.defense = (row[13] == "Yes")
        self.rating_auto = row[14]
        self.rating_speed = row[15]
        self.rating_game_piece_pickup = row[16]
        self.rating_game_piece_scoring = row[17]
        self.rating_driver = row[18]
        self.rating_balance = row[19]
        self.rating_pick = row[20]
        self.comments_broken = row[21]
        self.comments_details = row[22]

    def __repr__(self) -> str:
        return self.__dict__.__repr__()

    def total_pts_auto(self):
        total = 2 * self.notes_scored_in_amp_auto + \
            5 * self.notes_scored_in_speaker_auto
        return total

    def total_pts_tele(self):
        total = 1 * self.notes_scored_in_amp_tele + \
            2 * self.notes_scored_in_speaker_tele
        return total

    def total_pts_amp(self):
        total = 2 * self.notes_scored_in_amp_auto + 1 * self.notes_scored_in_amp_tele
        return total

    def total_pts_speaker(self):
        total = 5 * self.notes_scored_in_speaker_auto + \
            2 * self.notes_scored_in_speaker_tele
        return total
