from majora import load


class Match:
    """Represents a single team's match data
    TODO: tell the team to add in different comment boxes for different categories (all optional boxes)

    TODO: sentiment analysis on comments
    talk to students to think of names for the personalities
    """

    def __init__(self, row):
        self.match_number = int(row[3])

        if row[4].lower() == "yes":
            self.left_starting_zone = True
        else:
            self.left_starting_zone = False

        self.notes_scored_in_amp_auto = load.extract_max_value(row[5])
        self.notes_scored_in_speaker_auto = load.extract_max_value(row[6])
        self.notes_scored_in_amp_tele = load.extract_max_value(row[7])
        self.notes_scored_in_speaker_tele = load.extract_max_value(row[8])
        self.parked = (row[9] == "Yes")
        self.onstage_without_harmony = row[10]
        self.onstage_with_harmony = row[11]
        self.notes_scored_in_trap = load.extract_max_value(row[12])
        self.defense = (row[13] == "Yes")
        self.rating_auto = row[14]
        self.rating_speed = row[15]
        self.rating_pickup = row[16]
        self.rating_scoring = row[17]
        self.rating_driver = row[18]
        self.rating_balance = row[19]
        self.rating_pick = row[20]
        self.comments_broken = row[21]
        self.comments_details = row[22]

    def to_list(self) -> list:
        return list(self.__dict__.values())

    @property
    def total_pts_auto(self):
        total = 2 * self.notes_scored_in_amp_auto + \
            5 * self.notes_scored_in_speaker_auto
        return total

    @property
    def total_pts_tele(self):
        total = 1 * self.notes_scored_in_amp_tele + \
            2 * self.notes_scored_in_speaker_tele
        return total

    @property
    def total_pts_amp(self):
        total = 2 * self.notes_scored_in_amp_auto + 1 * self.notes_scored_in_amp_tele
        return total

    @property
    def total_pts_speaker(self):
        total = 5 * self.notes_scored_in_speaker_auto + \
            2 * self.notes_scored_in_speaker_tele
        return total

    @property
    def total_notes_auto(self):
        return self.notes_scored_in_amp_auto + self.notes_scored_in_speaker_auto

    @property
    def total_notes_tele(self):
        return self.notes_scored_in_amp_tele + self.notes_scored_in_speaker_tele

    @property
    def total_notes_amp(self):
        return self.notes_scored_in_amp_auto + self.notes_scored_in_amp_tele

    @property
    def total_notes_speaker(self):
        return self.notes_scored_in_speaker_auto + self.notes_scored_in_speaker_tele

    # @property
    # def total_onstage(self):
    #     return self.onstage_with_harmony + self.onstage_without_harmony

    @property
    def total_notes(self):
        return self.total_notes_auto + self.total_notes_tele

    def _quantify_rating(self, s: str) -> int:
        match s:
            case "Bad":
                return 1
            case "OK":
                return 2
            case "Good":
                return 3
            case _:
                raise ValueError(f"Cannot convert a rating of \"{s}\" to a number.")

    @property
    def rating_auto_quantified(self):
        return self._quantify_rating(self.rating_auto)

    @property
    def rating_speed_quantified(self):
        return self._quantify_rating(self.rating_speed)

    @property
    def rating_pickup_quantified(self):
        return self._quantify_rating(self.rating_pickup)

    @property
    def rating_scoring_quantified(self):
        return self._quantify_rating(self.rating_scoring)

    @property
    def rating_driver_quantified(self):
        return self._quantify_rating(self.rating_driver)

    @property
    def rating_balance_quantified(self):
        return self._quantify_rating(self.rating_balance)

    @property
    def rating_pick_quantified(self):
        return self._quantify_rating(self.rating_pick)
