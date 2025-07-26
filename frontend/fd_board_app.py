import streamlit as st
import pandas as pd
import requests
from fd_board_config import API_URL
from frontend.streamlit_login import authenticate_user  # New secure login method

st.set_page_config(page_title="FD Dashboard", layout="wide")

# 🔐 Authenticate user first
user = authenticate_user()

if not user:
    st.stop()

# ✅ Show if logged in
st.success(f"✅ Logged in as {user['email']}")
st.title("📊 FD Summary Dashboard")

# 🔄 Fetch FD data from backend
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

    # 📥 Download Excel
    st.download_button("📥 Download as Excel", df.to_csv(index=False), file_name="fd_summary.csv")
