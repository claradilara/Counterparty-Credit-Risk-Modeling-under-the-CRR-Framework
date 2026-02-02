import numpy as np
import pandas as pd


def validate_dataframe(df: pd.DataFrame, name: str = "DataFrame"):
    """
    Validate that input is a non-empty DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(f"{name} must be a pandas DataFrame.")

    if df.empty:
        raise ValueError(f"{name} is empty.")


def validate_series(series: pd.Series, name: str = "Series"):
    """
    Validate that input is a non-empty Series.
    """
    if not isinstance(series, pd.Series):
        raise TypeError(f"{name} must be a pandas Series.")

    if series.empty:
        raise ValueError(f"{name} is empty.")


def check_positive(value: float, name: str):
    """
    Ensure numeric values are positive.
    """
    if value <= 0:
        raise ValueError(f"{name} must be positive.")


def check_probability(value: float, name: str):
    """
    Ensure value is between 0 and 1.
    """
    if not 0 <= value <= 1:
        raise ValueError(f"{name} must be between 0 and 1.")


def annualize_series(series: pd.Series) -> float:
    """
    Annualize a time series by taking its mean.
    """
    validate_series(series)
    return float(series.mean())
