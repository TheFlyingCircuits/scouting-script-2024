import csv
import json
from pathlib import Path

import requests
from statbotics import Statbotics

from majora import config
from majora.match import Match
from majora.team import Team


def load_all_team_data(field_data_path: Path, pit_data_path: Path):
    team_data = {}

    load_field_scouting_data(team_data, field_data_path)
    add_pit_scouting_data(team_data, pit_data_path)

    return team_data


def extract_max_value(values_as_text: str) -> int:
    split_values = values_as_text.split(',')

    max_value = 0
    for value in split_values:
        value = int(value)

        if value > max_value:
            max_value = value

    return max_value


def load_field_scouting_data(team_data, field_data_path):
    # Opens the CSV file that we download from Google Sheets
    with open(field_data_path, "r") as f:
        # Helps us read the CSV file easier
        reader = csv.reader(f)

        # Loop through each row of the CSV file
        for index, row in enumerate(reader):

            # Skip the first row because its just titles
            if index == 0:
                continue

            # Extract the team number
            team_number = row[3]

            # if team has not been seen before add a new entry to the dictionary
            if team_number not in team_data.keys():
                # Set up a new team with empty data
                team_data[team_number] = Team(team_number)

            # Creating a new match based on the row data
            match_data = Match(row)
            team_data[team_number].matches.append(match_data)


def add_pit_scouting_data(team_data, pit_data_path):
    with open(pit_data_path, "r") as f:
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
    try:
        with open("auth.json", "r") as f:
            return json.loads(f.read())
    except FileNotFoundError:
        raise FileNotFoundError("Failed to find auth.json file.")


def add_statbotics_data(team_data):
    sb = Statbotics()
    # TODO:
    ...


def add_tba_data(team_data):
    # GET /event/{event_key}/matches
    auth = load_auth()

    response = requests.get(
        url=f"{config.TBA_API_URL}{config.TBA_API_ENDPOINT}",
        headers={"X-TBA-Auth-Key": auth["Blue Alliance"]}
    )

    # TODO:
