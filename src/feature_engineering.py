def create_lag_features(df, column, lags=[1]):
    for lag in lags:
        df[f"{column}_lag{lag}"] = df[column].shift(lag)
    return df


def create_rolling_features(df, column, window=3):
    df[f"{column}_{window}day_avg"] = df[column].rolling(window).mean()
    return df


def engineer_features(df):
    df = create_lag_features(df, "sat_rain", [1])
    df = create_lag_features(df, "ground_rain", [1])

    df = create_rolling_features(df, "sat_rain", 3)
    df = create_rolling_features(df, "ground_rain", 3)

    df = df.dropna()
    return df
