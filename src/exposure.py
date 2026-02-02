import numpy as np
import pandas as pd

def compute_exposure(values: pd.DataFrame) -> pd.DataFrame:
    """
    Compute exposure as max(value, 0) for each path and time.
    """
    return values.clip(lower=0.0)


def expected_exposure(exposure: pd.DataFrame) -> pd.Series:
    """
    Expected Exposure (EE) at each time step.
    """
    return exposure.mean(axis=1)


def expected_positive_exposure(exposure: pd.DataFrame) -> float:
    """
    Expected Positive Exposure (EPE).
    Time-weighted average of EE.
    """
    ee = expected_exposure(exposure)
    return ee.mean()


def potential_future_exposure(
    exposure: pd.DataFrame,
    quantile: float = 0.95
) -> pd.Series:
    """
    Potential Future Exposure (PFE) at given confidence level.
    """
    return exposure.quantile(quantile, axis=1)
