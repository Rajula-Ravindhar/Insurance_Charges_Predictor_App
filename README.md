# Insurance Charges Predictor 💰
A Streamlit web application that predicts medical insurance charges based on user inputs such as age, BMI, number of children, smoking status, and region.  
This project demonstrates end-to-end data analysis, visualization, and machine learning model deployment.

---

## 📘 Overview
The Insurance Charges Predictor aims to estimate the expected medical charges for individuals using demographic and lifestyle features.  
It combines **Exploratory Data Analysis (EDA)**, **feature engineering**, and **regression modeling**, and is deployed as an interactive Streamlit app.

---

## 🧠 Project Workflow

### 1. Data Understanding
- Dataset contains columns: `age`, `sex`, `bmi`, `children`, `smoker`, `region`, and `charges`.
- Each record represents an individual’s medical cost billed by an insurance company.

### 2. Data Preprocessing
- Handled missing or inconsistent values (if any).
- Encoded categorical features (`sex`, `smoker`, `region`).
- Normalized numerical columns for better model convergence.

### 3. Exploratory Data Analysis (EDA)
Performed to gain insights into how different features influence insurance charges:
- **Univariate Analysis:** Distribution of `age`, `bmi`, `charges`.
  - Used **histograms**, **boxplots**, and **density plots**.
- **Bivariate Analysis:** Relation between features.
  - `smoker vs charges` → **Violin Plot** (strong positive correlation).
  - `region vs charges` → **Bar Chart**.
  - `bmi vs charges` → **Scatter Plot** (trend observed).
- **Correlation Heatmap:** Detected strong relationships between `bmi`, `smoker`, and `charges`.

### 4. Feature Engineering
- Converted categorical variables using **Label Encoding**.
- Removed highly correlated features (to reduce multicollinearity).
- Created polynomial or interaction features if needed.

### 5. Model Training
Used **Linear Regression**, **Random Forest**, and **Gradient Boosting** models.  
The best-performing model was selected based on metrics:
- R² Score
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)

Model was serialized using **Pickle** (`model.pkl`) for deployment.

---

## 🚀 Deployment

### 🔹 Streamlit App
The app allows users to input their details and instantly receive a predicted insurance charge.

**Key Features:**
- Simple and professional UI
- Real-time prediction from trained model
- Background image for a polished look
- Runs locally or on Streamlit Cloud / Google Colab

**App Inputs:**
- Age  
- BMI  
- Number of Children  
- Smoker (Yes/No)  
- Region (Northeast, Northwest, Southeast, Southwest)  

**Output:**
- Predicted Insurance Charge (in USD)

---

## 🧩 Tech Stack
| Category | Tools / Libraries |
|-----------|------------------|
| Programming | Python 3.12 / 3.13 |
| Libraries | pandas, numpy, matplotlib, seaborn, scikit-learn, pickle |
| Web Framework | Streamlit |
| Deployment | Streamlit Cloud / Google Colab |
| Visualization | Matplotlib, Seaborn |

---

## 🧪 How to Run the Project
   streamlit run <file_name>.py


