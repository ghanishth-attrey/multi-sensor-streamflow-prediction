import pandas as pd

def early_fusion(df, feature_cols):
    return df[feature_cols]


def late_fusion(pred_sat, pred_ground, weight=0.5):
    return weight * pred_sat + (1 - weight) * pred_ground
