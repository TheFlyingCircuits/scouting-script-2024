import csv

from majora import Match, Team


def load_field_scouting_data(team_data):
    # Opens the CSV file that we download from Google Sheets
    with open("Field Scouting Form Crescendo.csv", "r") as f:
        # Helps us read the CSV file easier
        reader = csv.reader(f)

        # Loop through each row of the CSV file
        for index, row in enumerate(reader):

            # Skip the first row because its just titles
            if index == 0:
                continue

            # Extract the team number
            team_number = row[2]

            # if team has not been seen before add a new entry to the dictionary
            if team_number not in team_data.keys():
                # Set up a new team with empty data
                team_data[team_number] = Team(team_number)

            # Creating a new match based on the row data
            match_data = Match(row)
            team_data[team_number].matches.append(match_data)


def load_pit_scouting_data(team_data):
    with open("Pit Scouting Form - Crescendo.csv", "r") as f:
        # Helps us read the CSV file easier
        reader = csv.reader(f)

        # Loop through each row of the CSV file
        for index, row in enumerate(reader):
            # Skip the first row because its just titles
            if index == 0:
                continue

            # Extract the team number
            team_number = row[2]

            # if team has not been seen before add a new entry to the dictionary
            if team_number not in team_data.keys():
                # Set up a new team with empty data
                team_data[team_number] = Team(team_number)

            team_data[team_number].pits.update(row)


def generate_spreadsheet(team_data, filename):
    """
    Notes:
    - Take some of the qualitative data (Good/OK/Bad) and make it quantitative
      - I.e. good = 3, OK = 2
    - Amp vs speaker points pie chart
    - Chart of match vs points, to see how they progress over the competition
      - Slope for match vs points to see how the team got better
      - Also have separate lines for teleop vs auto, and lines for amp vs speaker
    - Add the scouter's comments, also list the scouter's name
    - Generally have more high-level statistics at the top of the sheet
      - Have the complete data hidden, have to scroll down
      - Rank all the robots
    - Use statbotics API and TBA API
      - Have a cache for the statbotics data?
    - How well did their teammates do in their matches?
    - How well did their opponents do in their matches?
    - One number to rule them all?

    """
    ...


def main():
    team_data = {}

    load_field_scouting_data(team_data)
    load_pit_scouting_data(team_data)
    generate_spreadsheet(team_data, "output.xlsx")

    print("> Finished running.")

    breakpoint()


main()
