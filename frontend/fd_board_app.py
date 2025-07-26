import streamlit as st
from streamlit_login import authenticate_user


import pandas as pd
import requests
from fd_board_config import API_URL

# Configure the page
st.set_page_config(page_title="FD Dashboard", layout="wide")

st.write("🔍 Session User Check:", st.session_state.get("user"))


# 🔒 Enforce login
if "user" not in st.session_state:
    user = authenticate_user()
    st.session_state["user"] = user["email"]
    st.experimental_rerun()


# ✅ Authenticated user can see the dashboard
st.title("📊 FD Summary Dashboard")

res = requests.get(API_URL)
if res.status_code != 200:
    st.error("Failed to fetch data")
else:
    data = res.json()
    deposits = data["summary"]["deposits"]
    df = pd.DataFrame(deposits)

    st.subheader("🧾 Fixed Deposits")
    st.dataframe(df)

    st.subheader("📈 Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Principal", f"₹{df['principal_amount'].sum():,.0f}")
    col2.metric("Avg Interest Rate", f"{df['interest_rate'].mean():.2f}%")
    col3.metric("Next Maturity", df["maturity_date"].min())

    st.download_button("📥 Download as Excel", df.to_csv(index=False), file_name="fd_summary.csv")
