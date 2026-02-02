import pandas as pd
from typing import Dict
from src.market_simulation import simulate_gbm
from src.exposure import (
    compute_exposure,
    expected_exposure,
    expected_positive_exposure
)
from src.cva import compute_cva


def run_stress_scenario(
    base_params: Dict,
    stress_params: Dict
) -> Dict:
    """
    Run a stressed scenario and compute EPE and CVA.
    """

    # Simulate stressed market paths
    paths = simulate_gbm(
        s0=base_params["s0"],
        mu=base_params["mu"],
        sigma=stress_params.get("sigma", base_params["sigma"]),
        T=base_params["T"],
        n_steps=base_params["n_steps"],
        n_paths=base_params["n_paths"]
    )

    portfolio_values = paths - base_params["strike"]
    exposure = compute_exposure(portfolio_values)
    ee = expected_exposure(exposure)
    epe = expected_positive_exposure(exposure)

    cva = compute_cva(
        ee=ee,
        times=ee.index,
        hazard_rate=stress_params.get(
            "hazard_rate", base_params["hazard_rate"]
        ),
        recovery_rate=base_params["recovery_rate"],
        discount_rate=base_params["discount_rate"]
    )

    return {
        "EPE": epe,
        "CVA": cva
    }
