class TeamStats:
    rankings: dict


def add_statistics(team_data: dict):
    rankings = add_rankings(team_data)


def add_rankings(team_data: dict):
    categories = {
        "Auto Notes": "avg_notes_auto",
        "Tele Notes": "avg_notes_tele",
        "Amp Notes": "avg_notes_amp",
        "Speaker Notes": "avg_notes_speaker"
    }

    rankings = {}

    # Calculate rankings per category
    for display_name, attr in categories.items():
        def get_key(input):
            _, team = input
            value = getattr(team, attr)

            return value

        rankings[display_name] = sorted(list(team_data.items()), key=get_key, reverse=True)

    # Group rankings by team
    team_rank_info = {
        team_number: {}
        for team_number in team_data.keys()}

    for category, ranks in rankings.items():
        for index, (team_number, _) in enumerate(ranks, 1):
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
