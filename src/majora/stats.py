import time

import gevent
from statbotics import Statbotics

from majora import config


class TeamStats:
    rankings: dict


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
        "Auto Notes": "avg_notes_auto",
        "Tele Notes": "avg_notes_tele",
        "Amp Notes": "avg_notes_amp",
        "Speaker Notes": "avg_notes_speaker",
        "Avg. EPA": "avg_epa",
        "Final EPA": "end_epa"
    }

    rankings = {}

    # Calculate rankings per category
    for display_name, attr in categories.items():

        attr_data_by_team = [
            (team_number, team, getattr(team, attr))
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
        for index, (team_number, _, value) in enumerate(ranks, 1):
            # breakpoint()
            # TODO:
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
