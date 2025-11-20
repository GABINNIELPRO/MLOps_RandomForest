# mlops-immobilier

# Project: Real Estate Property Value Prediction

**Date:** December 2024  
**Presented to:** Mr. Yamak  
**Presented by:** Gabin Niel  

---

## 📄 Project Overview

This project focuses on **predicting real estate property values** using **Machine Learning** and **Deep Learning** techniques. The goal is to estimate the property’s market value based on multiple parameters such as surface area, number of rooms, location, and property type using a government-provided dataset.

---

## 🔹 Dataset

- **Rows:** 305,000  
- **Columns:** 41  
- The dataset contains information on transactions, including property details, surface areas, location, type of property, and the transaction value (`valeur_foncière`).  
- After preprocessing, the dataset was reduced to **74,000 rows** with **no missing values** and only the relevant columns kept.

---

## 🔹 Preprocessing Steps

1. **Initial Data Cleaning**
   - Removed irrelevant columns.
   - Filled missing values using:
     - `lot_surface_carrez` for `surface_reelle_bati`.
     - Group-based means for latitude, longitude, and terrain area.
   - Created **missing indicator columns** for certain features.

2. **Transaction Consolidation**
   - Grouped rows by `id_mutation` to merge multiple lots in a single transaction.
   - Added a `dep` column to indicate the presence of dependencies (1 if present, 0 if absent).

3. **Data Conversion**
   - Converted object/string columns to numeric using `LabelEncoder`.
   - Ensured all features are compatible with ML/DL models.

4. **Feature Selection**
   - Retained 18 relevant columns including:
     ```
     surface_reelle_bati, nombre_pieces_principales, surface_terrain, 
     code_type_local, id_mutation, nature_mutation, valeur_fonciere, 
     adresse_nom_voie, code_commune, lot1_surface_carrez, lot2_surface_carrez, 
     lot3_surface_carrez, lot4_surface_carrez, lot5_surface_carrez, 
     nombre_lots, longitude, latitude, nature_culture
     ```

5. **Train/Test Split**
   - 90% for training, 10% for testing.
   - StandardScaler used for feature normalization.

---

## 🔹 Models Used

### 1. **Linear Regression**
- **R² Score:** 76%  
- **MAE:** 89,477  
- **RMSE:** 324,310  
- **Observations:** Performed best among all tested models given dataset size.

### 2. **Deep Learning (Neural Network)**
- **Architecture:** 5 hidden layers, ReLU activation, BatchNormalization, EarlyStopping
- **Optimizer:** Adam  
- **Loss Function:** MSE  
- **Epochs:** 50  
- **R² Score:** 78%  
- **MAE:** 74,000  
- **Observations:** Slightly better R², but deep learning is less effective with limited data.

> **Conclusion:** For this dataset (~74k rows), **linear regression** provides reliable predictions with slightly higher MAE, while deep learning is more data-hungry.

---

## 🔹 Functions in the Repository

1. **`clean_file()`**
   - Applies the same preprocessing used for model training on new files.

2. **`predict_file()`**
   - Imports CSV files, defines features, predicts property values.
   - Outputs a new CSV with column `valeur_fonciere_predite`.

---

## 🔹 Key Takeaways

- Proper **data cleaning and preprocessing** is critical for accurate predictions.
- Transaction consolidation is essential to avoid bias caused by repeated values.
- Machine learning models, particularly **linear regression**, can outperform deep learning when dataset size is limited.
- The project provides a framework to apply trained models on new data files automatically.

---

## 📌 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/<username>/<repo-name>.git
