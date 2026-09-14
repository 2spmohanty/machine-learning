# Medical Cost Personal Dataset — Regression Practice

## Project Objective

Build a baseline regression model to predict individual medical insurance charges using the  [Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance) from Kaggle.

* **Prediction target**: charges
* **Task type**: Regression

## Learning Goal

Practice handling mixed numerical and categorical data in a linear regression workflow. This project focuses on one-hot encoding, feature scaling, feature interactions, and understanding which features influence medical insurance costs.


## Concepts

* **One-Hot Encoding**: Converted categorical text data (like 'Smoker' status and 'Region') into binary numerical values that a regression model can process.
* **Interaction Features**: Engineered new features (e.g., BMI * Smoker) to capture complex relationships where two variables combined have a massive impact on the target.
* **Advanced Feature Scaling**: Applied Z-score Normalisation to handle features with massive scale differences (Age vs. Annual Charges).
* **Learning Rate Tuning** : Experimented with different values to find the "sweet spot" that allows for fast convergence without overshooting the minimum cost.

