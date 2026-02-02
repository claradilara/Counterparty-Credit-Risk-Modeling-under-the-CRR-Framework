import numpy as np
import pandas as pd


def discount_factors(
    times: pd.Index,
    rate: float
) -> pd.Series:
    """
    Flat discount curve.
    """
    return np.exp(-rate * times)


def default_probabilities(
    times: pd.Index,
    hazard_rate: float
) -> pd.Series:
    """
    Default probability per time step using constant hazard rate.
    """
    times_series = pd.Series(times, index=times)
    survival = np.exp(-hazard_rate * times_series)

    pd_t = survival.shift(1)
    pd_t.iloc[0] = 1.0
    pd_t = pd_t - survival

    return pd_t



def compute_cva(
    ee: pd.Series,
    times: pd.Index,
    hazard_rate: float,
    recovery_rate: float,
    discount_rate: float
) -> float:
    """
    Compute CVA using EE profile.
    """
    df = discount_factors(times, discount_rate)
    pd_t = default_probabilities(times, hazard_rate)

    cva = (1 - recovery_rate) * np.sum(ee * pd_t * df)
    return float(cva)
