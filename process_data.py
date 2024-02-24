from majora import generate, load, stats


def main():
    team_data = load.load_all_team_data()
    stats.add_statistics(team_data)
    generate.generate_spreadsheet(team_data, "output.xlsx")
    print("> Finished running.")

    # breakpoint()


if __name__ == "__main__":
    main()
