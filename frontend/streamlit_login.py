# frontend/streamlit_login.py

import streamlit as st
import streamlit.components.v1 as components
import requests

RENDER_BACKEND_URL = "https://fd-board-backend.onrender.com"

def load_login_widget():
    st.markdown("### 🔐 Please login with your Google account to continue")

    login_component = """
    <script src="https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js"></script>

    <script>
      const firebaseConfig = {
        apiKey: "AIzaSyAcAz9ue_SxuHapI9ZpabDk8G8tlsvuXms",
        authDomain: "find-my-net-worth.firebaseapp.com",
        projectId: "find-my-net-worth",
        appId: "1:646679222393:web:99f9e71514993167a41ca8"
      };

      firebase.initializeApp(firebaseConfig);

      window.addEventListener("message", (event) => {
        const token = event.data.idToken;
        if (token) {
          const query = new URLSearchParams({ token: token });
          window.location.href = window.location.pathname + "?" + query.toString();
        }
      });

      firebase.auth().onAuthStateChanged(async function(user) {
        if (user) {
          const idToken = await user.getIdToken();
          window.parent.postMessage({ idToken: idToken }, "*");
        }
      });
    </script>
    """

    components.html(login_component, height=400)

    # Read token from URL param
    token = st.experimental_get_query_params().get("token", [None])[0]

    if not token:
        st.stop()

    # Call backend to verify token
    headers = {"Authorization": token}
    try:
        res = requests.get(f"{RENDER_BACKEND_URL}/verify-token", headers=headers, timeout=5)
        if res.status_code == 200:
            email = res.json().get("email", "")
            st.session_state["user"] = {"email": email, "token": token}  # ✅ SET user in session
            st.success(f"✅ Logged in as {email}")
            st.experimental_rerun()  # 🔁 Force rerun to show the dashboard
        else:
            st.error("❌ Invalid token. Please try logging in again.")
            st.stop()
    except Exception as e:
        st.error(f"❌ Failed to reach backend. Error: {e}")
        st.stop()
