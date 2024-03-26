from pathlib import Path

FIRST_MATCH_ON_SATURDAY = 58
HIGHEST_TELE_SPEAKER_NOTES = 6.833

TBA_EVENT_KEY: str = "2024ohcl"
TBA_API_URL: str = "https://www.thebluealliance.com/api/v3"
TBA_API_ENDPOINT: str = f"/event/{TBA_EVENT_KEY}/matches"

# If the script cant open one of these files, try changing the file name here
REPO_ROOT = Path(__file__).parent.parent.parent
FIELD_DATA_CSV_PATH: Path = Path(REPO_ROOT, "data", "[BUCKEYE] Field Scouting.csv")
PIT_DATA_CSV_PATH: Path = Path(REPO_ROOT, "data", "[BUCKEYE] Pit Scouting.csv")
