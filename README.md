# Industrial Training Kit

The **Industrial Training Kit** is an automated, high-efficiency data preprocessing and feature engineering pipeline. Designed to transform raw, "dirty" datasets into clean, model-ready inputs, this kit streamlines the data wrangling process to ensure robust machine learning workflows.

---

## 🚀 Features

* **Intelligent Imputation:** Uses **Random Forest feature importance** and **K-Nearest Neighbors (KNN)** to fill missing values, providing significantly better accuracy than simple mean/median filling.
* **Outlier Management:** Automatically detects and caps extreme values using the **Interquartile Range (IQR)** method.
* **Automated Encoding:** Identifies low-cardinality categorical variables and performs **One-Hot Encoding** automatically.
* **Multicollinearity Handling:** Identifies and removes highly correlated features (>$0.8$ correlation) to prevent model overfitting.
* **Schema Security:** Leverages **Pandera** to infer and export data schemas, ensuring data integrity and consistent structure for future workflows.

---

## 🛠 Technologies Used

| Technology | Purpose |
| --- | --- |
| **Python** | Core programming language |
| **Pandas** | Data manipulation and structural cleaning |
| **NumPy** | Numerical operations and matrix calculations |
| **Scikit-Learn** | ML-based imputation and preprocessing |
| **Pandera** | Schema inference and data validation |

---

## 💡 Why Use This Kit?

Data preparation often consumes 80% of a data scientist's time. The **Industrial Training Kit** solves this by:

1. **Reducing Manual Labor:** Automates complex decisions like group-based imputation and feature reduction.
2. **Improving Model Performance:** Cleans data using advanced algorithms, ensuring the model trains on high-quality, normalized information.
3. **Standardizing Pipelines:** Produces a consistent, repeatable `refined.csv` output and a documented schema file for every project.

---

## 📋 Requirements

To run this project, you will need to install the following dependencies:

```bash
pip install pandas numpy scikit-learn pandera

```

---

## 🚀 How to Use

1. Place your dataset file in the project directory.
2. Update the `df = pd.read_csv(...)` line in the script with your filename.
3. Run the script:
```bash

```



python your_script_name.py

```
4.  The script will generate `refined.csv` (the cleaned data) and `schema.py` (the validated data scheme).

