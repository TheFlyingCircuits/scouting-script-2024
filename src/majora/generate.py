from openpyxl import Workbook
from openpyxl.styles import Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.worksheet import Worksheet

from majora.team import Team


def generate_spreadsheet(team_data, filename):
    """
    Notes:
    - Take some of the qualitative data (Good/OK/Bad) and make it quantitative
        - I.e. good = 3, OK = 2
        - Averages
    - Amp vs speaker points pie chart
    - Chart of match vs points, to see how they progress over the competition
        - Slope for match vs points to see how the team got better
        - Also have separate lines for teleop vs auto, and lines for amp vs speaker
    - Add the scouter's comments, also list the scouter's name
    - Generally have more high-level statistics at the top of the sheet
        - Have the complete data hidden, have to scroll down
        - Rank all the robots
        -
    - Use statbotics API and TBA API
        - Have a cache for the statbotics data?
    - How well did their teammates do in their matches?
    - How well did their opponents do in their matches?
    - One number to rule them all?


    - 3 AI generated personalities that give a review of each robot


    """
    wb = Workbook()

    main_sheet = MainSheet(team_data)
    main_sheet.add_to_workbook(wb)

    for team_number, team in team_data.items():
        team_sheet = TeamSheet(team_number, team)
        team_sheet.add_to_workbook(wb)

    wb.save(filename)


class MainSheet:

    def __init__(self, team_data: dict) -> None:
        self.team_data = team_data

    def add_to_workbook(self, workbook: Workbook):
        ws = workbook.active
        ws.title = "Main"  # type: ignore
        ...


class TeamSheet:

    def __init__(self, team_number: int, team: Team) -> None:
        self.team_number = team_number
        self.team = team

    def add_to_workbook(self, workbook: Workbook):
        ws = workbook.create_sheet(str(self.team_number))
        self.add_match_data(ws, (1, 25))

    def add_match_data(self, ws: Worksheet, top_left_cell: tuple[int, int]):
        top_left_col, top_left_row = top_left_cell

        column_titles = [
            "Match Number",
            "Left Starting Zone",
            "Amp (Notes)",
            "Speaker (Notes)",
            "Amp (Notes)",
            "Speaker (Notes)",
            "Parked",
            "Onstage without Harmony",
            "Onstage with Harmony",
            "Notes in Trap",
            "Defense",
            "Auto",
            "Speed",
            "Pickup",
            "Scoring",
            "Driver",
            "Balance",
            "Pick",
            "Broken",
            "Details",
        ]

        centered_alignment = Alignment(vertical="center", horizontal="center", wrap_text=True)

        auto_cols = [2, 3]
        teleop_cols = [4, 5]
        ratings_cols = [col for col in range(10, 18)]
        comments_cols = [18, 19]

        col_groups_with_headers = {
            "Auto": auto_cols,
            "Teleop": teleop_cols,
            "Ratings": ratings_cols,
            "Comments": comments_cols
        }

        # Write column headers
        for col_index, col_title in enumerate(column_titles, top_left_col):
            col_offset = col_index - top_left_col

            if any([col_offset in col_group for col_group in col_groups_with_headers.values()]):
                cell_str = f"{get_column_letter(col_index)}{top_left_row + 1}"
                ws[cell_str] = col_title
                ws[cell_str].alignment = centered_alignment
            else:
                ws.merge_cells(start_row=top_left_row, start_column=col_index,
                               end_row=top_left_row+1, end_column=col_index)
                cell_str = f"{get_column_letter(col_index)}{top_left_row}"
                ws[cell_str] = col_title
                ws[cell_str].alignment = centered_alignment

        for group_name, col_group in col_groups_with_headers.items():
            ws.merge_cells(start_row=top_left_row, start_column=top_left_col + col_group[0],
                           end_row=top_left_row, end_column=top_left_col + col_group[-1])
            cell_str = f"{get_column_letter(top_left_col + col_group[0])}{top_left_row}"
            ws[cell_str] = group_name
            ws[cell_str].alignment = centered_alignment

        # Write actual data
        rows = []
        for match in self.team.matches:
            rows.append(match.to_list())

        for row_index, row in enumerate(rows, top_left_row + 2):
            for col_index, cell_data in enumerate(row, top_left_col):
                cell_str = f"{get_column_letter(col_index)}{row_index}"
                ws[cell_str] = cell_data
