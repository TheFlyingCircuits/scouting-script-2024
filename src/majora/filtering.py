def filter_out_the_crap(team_data: dict, rankings: dict):
    filter_by = "Avg. EPA"
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
