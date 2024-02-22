import csv
import json
from pathlib import Path

import requests
from statbotics import Statbotics

from majora import config
from majora.match import Match
from majora.team import Team


def load_all_team_data():
    team_data = {}

    load_field_scouting_data(team_data)
    add_pit_scouting_data(team_data)
    add_tba_data(team_data)
    add_statbotics_data(team_data)

    return team_data


def extract_max_value(values_as_text: str) -> int:
    split_values = values_as_text.split(';')

    max_value = 0
    for value in split_values:
        value = int(value)
        if value > max_value:
            max_value = value

    return max_value


def load_field_scouting_data(team_data):
    # Opens the CSV file that we download from Google Sheets
    with open(config.FIELD_DATA_CSV_PATH, "r") as f:
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


def add_pit_scouting_data(team_data):
    with open(config.PIT_DATA_CSV_PATH, "r") as f:
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


def load_auth():
    if Path(__file__).parent.parent.parent != config.ROOT_FOLDER_PATH:
        raise FileNotFoundError("This script must be executed from within the "
                                f"{config.ROOT_FOLDER_PATH.name} folder!")

    with open("auth.json", "r") as f:
        return json.loads(f.read())


def add_statbotics_data(team_data):
    sb = Statbotics()
    ...


def add_tba_data(team_data):
    # GET /event/{event_key}/matches
    auth = load_auth()

    response = requests.get(
        url=f"{config.TBA_API_URL}{config.TBA_API_ENDPOINT}",
        headers={"X-TBA-Auth-Key": auth["Blue Alliance"]}
    )

    breakpoint()
