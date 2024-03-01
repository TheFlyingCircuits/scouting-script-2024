from pathlib import Path

from majora import config, generate, load, stats

# If the script cant open one of these files, try changing the file name here
REPO_ROOT = Path(__file__).parent
FIELD_DATA_CSV_PATH: Path = Path(REPO_ROOT, "data", "[PITTSBURGH] Field Scouting.csv")
PIT_DATA_CSV_PATH: Path = Path(REPO_ROOT, "data", "[PITTSBURGH] Pit Scouting.csv")


def main():
    print(f"Running for event: {config.TBA_EVENT_KEY}")

    team_data = load.load_all_team_data(FIELD_DATA_CSV_PATH, PIT_DATA_CSV_PATH)
    rankings = stats.add_statistics(team_data)
    generate.generate_spreadsheet(team_data, rankings, "output.xlsx")

    print("> Finished running.")

    # breakpoint()


if __name__ == "__main__":
    main()
