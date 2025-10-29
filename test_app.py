import streamlit as st
import pandas as pd
import joblib
import os
import plotly.express as px

# --- Helper Function to Load Model/Data ---
@st.cache_resource # Use cache_resource for models
def load_pickle(file_path, name):
    if not os.path.exists(file_path):
        st.error(f"{name} File not found: {file_path}")
        return None
    try:
        obj = joblib.load(file_path)
        st.success(f"Loaded {name} from {file_path}")
        return obj
    except Exception as e:
        st.error(f"Error loading {name}: {e}")
        return None

@st.cache_data # Use cache_data for dataframes
def load_data(path):
    if not os.path.exists(path):
        st.error(f"File not found: {path}")
        return None
    return pd.read_csv(path)

# --- Load Your Assets ---
model = load_pickle("final_pizza_price_model.pkl", "Price Prediction Model")

# --- THIS LINE IS NOW CORRECTED ---
df = load_data("data/pizza_sales.csv") 

if model is None or df is None:
    st.warning("Model or data file not found. App cannot continue.")
    st.stop() # Stops the app if files are missing

# --- Page Title ---
st.title("🍕 Pizza Price Prediction and Analysis")
st.markdown("An AI-Powered Approach to Understanding Pizza Pricing")

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Data and EDA", 
    "Predictions and Explainability"
])

# --- Page 1: Data and EDA ---
if page == "Data and EDA":
    st.header("Data Collection and EDA")
    st.write("The dataset contains various attributes for each pizza...")
    st.subheader("Sample of the Dataset")
    st.dataframe(df.head())

    st.subheader("Exploratory Data Analysis (EDA) Insights")

    # --- THIS BLOCK IS NOW CORRECTED ---
    # Plot 1: Distribution of Prices
    st.write("Distribution of Product Prices")
    fig1 = px.histogram(df, x="unit_price", title="Pizza Price Distribution")
    st.plotly_chart(fig1, use_container_width=True)

    # Plot 2: Prices by Category
    st.write("Prices by Category")
    fig2 = px.box(df, x="pizza_category", y="unit_price", title="Pizza Prices by Category")
    st.plotly_chart(fig2, use_container_width=True)

# --- Page 2: Predictions ---
elif page == "Predictions and Explainability":
    st.header("Predict a Product's Price")
    st.write("Fill in the pizza details below to predict its price.")

    # --- THIS BLOCK IS NOW CORRECTED ---
    # Interactive Widgets
    col1, col2 = st.columns(2)
    with col1:
        # Changed 'company' to 'pizza_name'
        pizza_name = st.selectbox("Pizza Name", df['pizza_name'].unique()) 
        
        # Changed 'type' to 'pizza_category'
        category = st.selectbox("Category", df['pizza_category'].unique()) 
    with col2:
        # Changed slider to a selectbox for 'pizza_size'
        pizza_size = st.selectbox("Size", df['pizza_size'].unique()) 
        # Add other widgets for your model's features...

    # --- Prediction Button ---
    if st.button("Predict Price"):
        
        # --- Placeholder for prediction logic ---
        # This part will need to be updated to match how your
        # 'final_pizza_price_model.pkl' was trained.
        # It likely needs inputs like pizza_name, category, and size
        # to be one-hot encoded or label encoded.
        predicted_price = 19.99 # This is still a placeholder

        st.success(f"Predicted Price: ${predicted_price:.2f}")

        # --- Explainability ---
        st.subheader("Model Explainability (SHAP/LIME)")
        st.write("This section shows why the model made its prediction.")
        # Add your SHAP or LIME plots here