import time
from copy import deepcopy
from enum import Enum

import gevent
from statbotics import Statbotics

from majora import config, filtering


class TeamStats:
    rankings: dict


class DayFilter(Enum):
    FRIDAY = 0
    SATURDAY = 1
    COMBINED = 2
    LAST_3 = 3


def add_statistics(team_data: dict):
    add_statbotics(team_data)
    rankings = add_rankings(team_data)

    return rankings


def add_statbotics(team_data: dict):
    start_time = time.time()

    threads = [
        gevent.spawn(get_statbotics_for_team, team_number)
        for team_number, _ in team_data.items()
    ]

    results = [
        thread.get()
        for thread in threads
    ]

    for team_number, sb_data in results:
        team_data[team_number].statbotics = sb_data

    end_time = time.time() - start_time

    print(f"Finished getting statbotics data in {end_time:.2f}s.")


def get_statbotics_for_team(team_number: str) -> tuple[str, dict]:
    sb = Statbotics()
    return (team_number, sb.get_team_event(int(team_number), config.TBA_EVENT_KEY))


def add_rankings(team_data: dict):
    categories = {
        "Auto Notes Friday": ("avg_notes_auto", DayFilter.FRIDAY),
        "Tele Notes Friday": ("avg_notes_tele", DayFilter.FRIDAY),
        "Amp Notes Friday": ("avg_notes_amp", DayFilter.FRIDAY),
        "Speaker Notes Friday": ("avg_notes_speaker", DayFilter.FRIDAY),
        "Defense % Friday": ("defense_pct", DayFilter.FRIDAY),
        "FAST! Friday": ("avg_rating_speed", DayFilter.FRIDAY),
        "DECISIVE! Friday": ("avg_rating_driver", DayFilter.FRIDAY),
        "SPEAKER TELE! Friday": ("avg_speaker_tele_notes", DayFilter.FRIDAY),
        "RICE SCORE! Friday": ("rice_score", DayFilter.FRIDAY),

        "Avg. EPA (All Days)": ("avg_epa", DayFilter.COMBINED),

        "Auto Notes Saturday": ("avg_notes_auto", DayFilter.SATURDAY),
        "Tele Notes Saturday": ("avg_notes_tele", DayFilter.SATURDAY),
        "Amp Notes Saturday": ("avg_notes_amp", DayFilter.SATURDAY),
        "Speaker Notes Saturday": ("avg_notes_speaker", DayFilter.SATURDAY),
        "Defense % Saturday": ("defense_pct", DayFilter.SATURDAY),
        "FAST! Saturday": ("avg_rating_speed", DayFilter.SATURDAY),
        "DECISIVE! Saturday": ("avg_rating_driver", DayFilter.SATURDAY),
        "SPEAKER TELE! Saturday": ("avg_speaker_tele_notes", DayFilter.SATURDAY),
        "RICE SCORE! Saturday": ("rice_score", DayFilter.SATURDAY),

        "Auto Notes Last 3": ("avg_notes_auto", DayFilter.LAST_3),
        "Tele Notes Last 3": ("avg_notes_tele", DayFilter.LAST_3),
        "Amp Notes Last 3": ("avg_notes_amp", DayFilter.LAST_3),
        "Speaker Notes Last 3": ("avg_notes_speaker", DayFilter.LAST_3),
        "Defense % Last 3": ("defense_pct", DayFilter.LAST_3),
        "FAST! Last 3": ("avg_rating_speed", DayFilter.LAST_3),
        "DECISIVE! Last 3": ("avg_rating_driver", DayFilter.LAST_3),
        "SPEAKER TELE! Last 3": ("avg_speaker_tele_notes", DayFilter.LAST_3),
        "RICE SCORE! Last 3": ("rice_score", DayFilter.LAST_3),

        "Auto Notes Combined": ("avg_notes_auto", DayFilter.COMBINED),
        "Tele Notes Combined": ("avg_notes_tele", DayFilter.COMBINED),
        "Amp Notes Combined": ("avg_notes_amp", DayFilter.COMBINED),
        "Speaker Notes Combined": ("avg_notes_speaker", DayFilter.COMBINED),
        "Defense % Combined": ("defense_pct", DayFilter.COMBINED),
        "FAST! Combined": ("avg_rating_speed", DayFilter.COMBINED),
        "DECISIVE! Combined": ("avg_rating_driver", DayFilter.COMBINED),
        "SPEAKER TELE! Combined": ("avg_speaker_tele_notes", DayFilter.COMBINED),
        "RICE SCORE! Combined": ("rice_score", DayFilter.COMBINED),
    }

    rankings = {}

    # Calculate rankings per category
    for display_name, (attr, competition_day) in categories.items():

        attr_data_by_team = [
            (team_number, team, getattr(team, attr)(competition_day))
            for team_number, team in team_data.items()
        ]

        def get_key(input):
            _, _, value = input
            return value

        rankings[display_name] = sorted(attr_data_by_team, key=get_key, reverse=True)

    # Group rankings by team
    team_rank_info = {
        team_number: {}
        for team_number in team_data.keys()}

    for category, ranks in rankings.items():
        for index, (team_number, _, _) in enumerate(ranks, 1):
            team_rank_info[team_number][category] = index

    # Write each team's ranking to its team object
    for team_number, team in team_data.items():
        team.stats.rankings = team_rank_info[team_number]

    return rankings


"""
Rankings:
X Auto
X Tele
X Speaker
X Amp
- Auto-Speaker
- Auto-Amp
- Tele-Speaker
- Tele-Amp
- Parking
- Onstage %
- Harmony %
- Notes in Trap
- Ratings in each category
- Match score
- EPA
- W/L
- Teammate Quality
    - Avg EPA?
- Opponent Quality
    - Avg EPA?
"""
