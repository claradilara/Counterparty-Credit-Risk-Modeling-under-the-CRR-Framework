import numpy as np
import pandas as pd


def simulate_gbm(
    s0: float,
    mu: float,
    sigma: float,
    T: float,
    n_steps: int,
    n_paths: int,
    seed: int = 42
) -> pd.DataFrame:
    """
    Simulate Geometric Brownian Motion (GBM) paths.

    Parameters
    ----------
    s0 : float
        Initial value of the asset / risk factor
    mu : float
        Drift term
    sigma : float
        Volatility
    T : float
        Time horizon in years
    n_steps : int
        Number of time steps
    n_paths : int
        Number of Monte Carlo paths
    seed : int
        Random seed for reproducibility

    Returns
    -------
    pd.DataFrame
        Simulated paths with time as index and paths as columns
    """

    np.random.seed(seed)
    dt = T / n_steps

    # Initialize matrix
    paths = np.zeros((n_steps + 1, n_paths))
    paths[0, :] = s0

    # Simulate paths
    for t in range(1, n_steps + 1):
        z = np.random.standard_normal(n_paths)
        paths[t, :] = paths[t - 1, :] * np.exp(
            (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z
        )

    time_grid = np.linspace(0, T, n_steps + 1)
    return pd.DataFrame(paths, index=time_grid)
