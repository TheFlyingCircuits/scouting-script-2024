from majora import config
from majora.stats import DayFilter


def filter_out_the_crap(team_data: dict, rankings: dict):
    filter_by = "Avg. EPA (All Days)"
    bottom_20_teams = [
        team_number
        for (team_number, _, _) in rankings[filter_by][-20:]
    ]

    for team_number in bottom_20_teams:
        team_data.pop(team_number)

        for category, ranks in rankings.items():

            new_ranks = []

            for rank_data in ranks:
                team_number, _, _ = rank_data

                if team_number not in bottom_20_teams:
                    new_ranks.append(rank_data)

            rankings[category] = new_ranks


def get_matches_from_day(matches: list, day: DayFilter):
    matches_to_keep = []

    if day == DayFilter.LAST_3:
        return matches[-3:]
    elif day == DayFilter.COMBINED:
        return matches
    else:
        for match in matches:
            if day == DayFilter.FRIDAY and match.match_number < config.FIRST_MATCH_ON_SATURDAY:
                matches_to_keep.append(match)

            elif day == DayFilter.SATURDAY and match.match_number >= config.FIRST_MATCH_ON_SATURDAY:
                matches_to_keep.append(match)

    return matches_to_keep
