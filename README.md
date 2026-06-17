# Advanced EDA & Feature Engineering (Project 1)

## 📌 Project Overview
[cite_start]Welcome to **Project 1: Advanced EDA & Feature Engineering**, an enterprise-grade data engineering project developed under the **DecodeLabs Industrial Training Kit (Batch 2026)**[cite: 134, 135, 158]. 

[cite_start]Machine learning estimators are numerical optimization algorithms that operate strictly on real-numbered coordinate spaces[cite: 206]. [cite_start]If low-fidelity, unrefined data enters the pipeline, the system will flawlessly optimize for incorrect patterns[cite: 207]. [cite_start]This project implements rigorous, rules-based statistical logic over arbitrary guesswork to build production-ready data pipelines [cite: 159, 240][cite_start], ensuring the highest structural engineering of mathematical truth before feeding downstream models[cite: 208].

---

## 🏗️ System Architecture: The IPO Blueprint
[cite_start]The data wrangling process transitions away from basic, local Jupyter scripts into a rigid **Input-Process-Output (IPO)** architectural framework[cite: 233, 234]:

1. [cite_start]**MODULE 1: INPUT (Securing Fidelity)** * Focuses on identifying data anomalies, neutralizing missing values, and establishing outlier boundaries to protect distribution variance[cite: 215, 216, 238].
2. **MODULE 2: PROCESS (The Engine)**
   * [cite_start]Implements block-allocated arrays to execute vectorized math, clean categorical data encodings, and eradicate multi-collinearity[cite: 223, 234].
3. **MODULE 3: OUTPUT (Contracts & Serving)**
   * [cite_start]Validates the finalized dataset using **Pandera schemas** and delivers high-fidelity feature stores via **Feast** for production downstream estimators[cite: 158, 230, 234].

---

## 🛠️ Key Requirements & Core Functionalities

### 1. Missing Data Decision Matrix (Module 1)
[cite_start]Instead of applying blanket strategies, the pipeline calculates the exact missingness proportion per feature and applies specific thresholds to mitigate MCAR and MAR scenarios[cite: 243, 253]:
* [cite_start]**`< 5% Missingness`**: Rows are dropped via optimized `dropna` scripts, ensuring low CPU overhead and zero synthetic data insertion[cite: 246, 255].
* [cite_start]**`5% to 20% Missingness`**: Implements targeted statistical imputation[cite: 244, 247]. [cite_start]Skewed numerical attributes utilize the **Global Median** to remain robust against extreme values[cite: 249, 255]. [cite_start]Categorical or correlated features use **Group-Wise Sub-Group Conditional Imputation** to preserve sub-population variance patterns[cite: 250, 255].
* [cite_start]**`> 20% Missingness`**: Employs multi-dimensional estimation using **K-Nearest Neighbors (KNN) Imputation** to cleanly capture complex variable relationships[cite: 245, 251, 252, 255].

### 2. Outlier Neutralization (Module 1)
[cite_start]To ensure extreme hardware glitches or transcription human errors do not warp regression optimization slopes or inflate variance boundaries [cite: 262][cite_start], the pipeline isolates statistical anomalies using robust, non-parametric boundaries[cite: 262]:
* **Interquartile Range (IQR) Method**: Formulates mathematical bounds where:
  [cite_start]$$Lower~Bound = Q1 - 1.5 \times IQR$$ [cite: 260]
  [cite_start]$$Upper~Bound = Q3 + 1.5 \times IQR$$ [cite: 261]
* [cite_start]**Z-Score Method**: Standardizes normal distributions to discard values deviating heavily from the population mean[cite: 141, 152].

### 3. Feature Engineering & Extraction (Module 2)
* [cite_start]Structural extraction of **at least 3 new predictive features** engineered from raw existing data columns to significantly boost downstream predictive power[cite: 155, 179].

---

## 💻 Technical Stack & Skills Demonstrated
* [cite_start]**Languages & Scripting:** Python [cite: 150]
* [cite_start]**Core Libraries:** Pandas, NumPy [cite: 156]
* [cite_start]**Methodologies:** Statistical Data Analysis, Vectorized Pipeline Architecture, Data Preprocessing, Feature Extraction[cite: 156, 158].
* [cite_start]**Production Validation:** Pandera (Schema Enforcement), Feast (Feature Store Serving)[cite: 158, 230].

---
[cite_start]*Developed as part of the DecodeLabs Data Scientist Track (Batch 2026).* [cite: 135, 137]
