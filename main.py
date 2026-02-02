import pandas as pd
import matplotlib.pyplot as plt

from src.market_simulation import simulate_gbm
from src.exposure import (
    compute_exposure,
    expected_exposure,
    expected_positive_exposure,
    potential_future_exposure
)
from src.cva import compute_cva
from src.stress_testing import run_stress_scenario


def main():
    # =========================
    # BASE PARAMETERS
    # =========================
    base_params = {
        "s0": 100.0,
        "mu": 0.02,
        "sigma": 0.15,
        "T": 1.0,
        "n_steps": 252,
        "n_paths": 5000,
        "strike": 100.0,
        "hazard_rate": 0.02,
        "recovery_rate": 0.40,
        "discount_rate": 0.01
    }

    # =========================
    # MARKET SIMULATION
    # =========================
    paths = simulate_gbm(
        s0=base_params["s0"],
        mu=base_params["mu"],
        sigma=base_params["sigma"],
        T=base_params["T"],
        n_steps=base_params["n_steps"],
        n_paths=base_params["n_paths"]
    )

    # =========================
    # PORTFOLIO VALUES
    # =========================
    portfolio_values = paths - base_params["strike"]

    # =========================
    # EXPOSURE METRICS
    # =========================
    exposure = compute_exposure(portfolio_values)
    ee = expected_exposure(exposure)
    epe = expected_positive_exposure(exposure)
    pfe = potential_future_exposure(exposure, quantile=0.95)

    print(f"Expected Positive Exposure (EPE): {epe:.4f}")

    # =========================
    # CVA CALCULATION
    # =========================
    cva = compute_cva(
        ee=ee,
        times=ee.index,
        hazard_rate=base_params["hazard_rate"],
        recovery_rate=base_params["recovery_rate"],
        discount_rate=base_params["discount_rate"]
    )

    print(f"Credit Valuation Adjustment (CVA): {cva:.4f}")

    # =========================
    # STRESS TESTING
    # =========================
    scenarios = {
        "Base": {},
        "High Volatility (+50%)": {"sigma": 0.225},
        "Credit Stress (HR x2)": {"hazard_rate": 0.04},
        "Severe Stress": {"sigma": 0.30, "hazard_rate": 0.05}
    }

    results = {}
    for name, stress in scenarios.items():
        results[name] = run_stress_scenario(base_params, stress)

    stress_df = pd.DataFrame(results).T

    print("\nStress Testing Results")
    print(stress_df)

    # =========================
    # VISUALIZATION
    # =========================
    plt.figure(figsize=(10, 5))
    plt.plot(ee.index, ee, label="Expected Exposure (EE)")
    plt.plot(pfe.index, pfe, linestyle="--", label="PFE (95%)")
    plt.xlabel("Time (years)")
    plt.ylabel("Exposure")
    plt.title("Exposure Profile")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
