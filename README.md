Perfect — below is a **professional, bank-grade `README.md`** you can copy–paste directly.
It is written exactly in the style **Nordea / EU banks / risk teams expect**.

---

# Counterparty Credit Risk Modeling under the CRR Framework

## 📌 Project Overview

This project implements a **Python-based counterparty credit risk modeling framework** aligned with **EU Capital Requirements Regulation (CRR)** principles.
It demonstrates the end-to-end development of exposure metrics, Credit Valuation Adjustment (CVA), and stress testing using Monte Carlo simulation and modular, production-style code.

The objective is to showcase **quantitative risk modeling**, **regulatory awareness**, and **clean software engineering practices** commonly used in banking risk model development teams.

---

## 🎯 Key Objectives

* Simulate market risk factors using Monte Carlo methods
* Compute counterparty exposure metrics (**EE, EPE, PFE**)
* Calculate **Credit Valuation Adjustment (CVA)**
* Perform **stress and impact testing** on market and credit parameters
* Structure code in a modular, reusable, and governance-ready way

---

## 🧠 Regulatory Context

Counterparty credit risk models are a core component of regulatory capital calculation under **Basel III / CRR**.
This project follows standard regulatory concepts, including:

* Expected Exposure (EE)
* Expected Positive Exposure (EPE)
* Potential Future Exposure (PFE)
* CVA based on exposure profiles, default probabilities, recovery rates, and discounting
* Scenario-based stress testing to assess risk sensitivity

While simplified for demonstration purposes, the framework reflects **industry-standard modeling logic and assumptions**.

---

## 🏗️ Project Structure

```
Counterparty-Credit-Risk-Modeling-under-the-CRR-Framework/
│
├── src/
│   ├── __init__.py
│   ├── market_simulation.py    # Monte Carlo GBM simulation
│   ├── exposure.py             # EE, EPE, PFE calculations
│   ├── cva.py                  # CVA computation
│   ├── stress_testing.py       # Stress & impact analysis
│   └── utils.py                # Validation & helper functions
│
├── main.py                     # Project entry point
├── requirements.txt
└── README.md
```

This structure mirrors **professional Python risk model libraries** used in banking environments.

---

## 🔬 Methodology

### 1️⃣ Market Risk Simulation

* Simulates market risk factors using **Geometric Brownian Motion (GBM)**
* Monte Carlo framework with configurable paths, time steps, and volatility
* Designed to represent simplified interest rate / FX dynamics

### 2️⃣ Exposure Modeling

For each simulated path:

* Portfolio values are calculated
* Exposure is defined as `max(V(t), 0)`

Computed metrics:

* **Expected Exposure (EE)**
* **Expected Positive Exposure (EPE)**
* **Potential Future Exposure (PFE, 95%)**

### 3️⃣ CVA Calculation

CVA is calculated using a discrete-time approximation:

[
\text{CVA} = (1 - R) \sum_t EE(t) \cdot PD(t) \cdot DF(t)
]

Where:

* `R` = recovery rate
* `PD(t)` = default probability derived from constant hazard rate
* `DF(t)` = discount factor

### 4️⃣ Stress & Impact Testing

Stress scenarios include:

* Increased market volatility
* Credit deterioration (higher hazard rate)
* Combined severe stress scenarios

Impact is measured on:

* EPE
* CVA

This aligns with regulatory expectations for **risk sensitivity and scenario analysis**.

---

## 🧪 Example Output

* Exposure profile plots (EE & PFE)
* CVA values under base and stressed conditions
* Tabular stress testing results showing relative impact

---

## 🛠️ Technologies Used

* **Python**
* NumPy, Pandas, SciPy
* Matplotlib
* Modular Python architecture

---

## 🚀 How to Run

1. Create and activate virtual environment
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the project:

   ```bash
   python main.py
   ```

---

## ⚠️ Assumptions & Limitations

* Simplified market dynamics (GBM)
* Flat discount and hazard rates
* Simplified derivative payoff structure
* Intended for **educational and demonstration purposes**, not production use

---

## 🔮 Future Enhancements

* Multiple correlated risk factors
* Netting & collateral (CSA) modeling
* Wrong-way risk
* Exposure aggregation across portfolios
* Integration with real market data
* Model validation & backtesting framework

---

## 👤 Author

**Dilara Özdil**
MSc Data Science & Business Analytics
Focus: Quantitative Risk Modeling, Counterparty Credit Risk, Regulatory Analytics

---

