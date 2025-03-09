import pandas as pd

from collections import Counter
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import NearMiss

def under_sampling(df: pd.DataFrame, target: str) -> pd.DataFrame:
    X = df.drop(columns=[target])
    y = df[target]

    print("Original class distribution:", Counter(y))

    under_sampler = NearMiss(version=1)
    X_resampled, y_resampled = under_sampler.fit_resample(X, y)

    df_resampled = pd.DataFrame(X_resampled, columns=X.columns)
    df_resampled[target] = y_resampled

    print("Resampled class distribution:", Counter(y_resampled))
    return df_resampled


def over_sampling(df: pd.DataFrame, target: str) -> pd.DataFrame:
    X = df.drop(columns=[target])
    y = df[target]

    print("Original class distribution:", Counter(y))

    over_sampler = SMOTE(sampling_strategy="auto", random_state=42)
    X_resampled, y_resampled = over_sampler.fit_resample(X, y)

    df_resampled = pd.DataFrame(X_resampled, columns=X.columns)
    df_resampled[target] = y_resampled

    print("Resampled class distribution:", Counter(y_resampled))
    return df_resampled