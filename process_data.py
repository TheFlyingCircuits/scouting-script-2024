from majora import config, generate, load


def main():
    team_data = load.load_all_team_data()
    generate.generate_spreadsheet(team_data, "output.xlsx")
    print("> Finished running.")

    breakpoint()


if __name__ == "__main__":
    main()
