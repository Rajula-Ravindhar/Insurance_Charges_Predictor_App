import streamlit as st # type: ignore
import pickle
import numpy as np # type: ignore

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="US Insurance_Charges_Predictor", layout="centered")

# ---------- BACKGROUND IMAGE ----------
def set_bg(image_url):
    page_bg = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("{image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# ---------- BACKGROUND GRADIENT ----------
def set_bg_gradient():
    page_bg = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(120deg, #0f172a 0%, #0ea5a9 40%, #7dd3fc 100%);
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

set_bg_gradient()


# ---------- LOAD MODEL ----------
with open(r"Insurance_charge_pred.pickle", "rb") as file:
    model = pickle.load(file)

# ---------- APP TITLE ----------
st.markdown("<h2 style='text-align: left; color: white;'>🏥Insurance_Charges_Predictor App</h2>", unsafe_allow_html=True)

# ---------- INPUT FORM ----------
st.markdown('###### 📃fill the below form to predict insurance charges :')
with st.form("input_form"):
    age = st.number_input("Age", min_value=1, max_value=120,value=None,format='%d')
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1,value=None)
    children = st.number_input("Number of Children", min_value=0, max_value=5,value=None)
    sex = st.selectbox("Gender", ["Select","Male", "Female"])
    smoker = st.selectbox("Smoker", ["Select","Yes", "No"])
    region = st.selectbox("Region", ["Select","northeast", "northwest", "southeast", "southwest"])
    
    st.markdown(
    """
    <style>
    div.stButton {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True,)

    submit = st.form_submit_button("Predict")

# ---------- WHEN SUBMIT PRESSED ----------
if submit:
    # Check if all inputs are filled correctly
    if (age is None or bmi is None or children is None 
        or sex == "Select" or smoker == "Select" or region == "Select"):
        st.warning("⚠️ Please fill in all details before predicting!")
    else:
    # Example preprocessing (adjust based on how you trained your model)
        smoker_val = 1 if smoker == "Yes" else 0
        gender_val = 1 if sex == "Male" else 0
    # One-hot encoding for region
        region_encoding = {
            "northeast": [0, 0, 0],
            "northwest": [1, 0, 0],
            "southeast": [0, 1, 0],
            "southwest": [0, 0, 1],
        }
        region_vals = region_encoding[region]

        # Combine all into a feature array
        features = np.array([[age, bmi, children,gender_val,smoker_val,region_vals[0],region_vals[1],region_vals[2]]])

        # Get prediction
        prediction = model.predict(features)

        # ---------- DISPLAY RESULT ----------
        st.success(f"✅ Estimated Insurance Charges: 💵 **{round(prediction[0],2)}**")
        


