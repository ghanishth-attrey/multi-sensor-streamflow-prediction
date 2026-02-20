from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from src.config import TEST_SIZE, RANDOM_STATE


def split_data(X, y):
    return train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )


def train_random_forest(X_train, y_train):
    model = RandomForestRegressor(
        n_estimators=300,
        random_state=RANDOM_STATE
    )
    model.fit(X_train, y_train)
    return model


def train_linear_regression(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def train_xgboost(X_train, y_train):
    model = XGBRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=5,
        random_state=RANDOM_STATE
    )
    model.fit(X_train, y_train)
    return model
