from pathlib import Path

from majora import config, filtering, generate, load, stats


def main():
    print(f"Running for event: {config.TBA_EVENT_KEY}")

    team_data = load.load_all_team_data(config.FIELD_DATA_CSV_PATH, config.PIT_DATA_CSV_PATH)
    rankings = stats.add_statistics(team_data)
    filtering.filter_out_the_crap(team_data, rankings)
    generate.generate_spreadsheet("output.xlsx", team_data, rankings)

    print("> Finished running.")

    breakpoint()


if __name__ == "__main__":
    main()
