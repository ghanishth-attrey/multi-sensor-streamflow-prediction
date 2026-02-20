DATA_PATH = "data/raw/"

TARGET_COLUMN = "streamflow"

FEATURE_COLUMNS = [
    "sat_rain",
    "ground_rain",
    "sat_rain_lag1",
    "ground_rain_lag1",
    "sat_rain_3day_avg",
    "ground_rain_3day_avg"
]

TEST_SIZE = 0.2
RANDOM_STATE = 42
