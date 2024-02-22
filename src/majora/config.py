from pathlib import Path

ROOT_FOLDER_PATH: Path = Path(__file__).parent.parent.parent
DATA_FOLDER_PATH: Path = Path(ROOT_FOLDER_PATH, "data")
FIELD_DATA_CSV_PATH: Path = Path(DATA_FOLDER_PATH, "Field Scouting Form Crescendo.csv")
PIT_DATA_CSV_PATH: Path = Path(DATA_FOLDER_PATH, "Pit Scouting Form - Crescendo.csv")

TBA_EVENT_KEY: str = "2023paca"
TBA_API_URL: str = "https://www.thebluealliance.com/api/v3"
TBA_API_ENDPOINT: str = f"/event/{TBA_EVENT_KEY}/matches"
