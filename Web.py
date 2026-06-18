import streamlit as st

st.set_page_config(layout="wide")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Home"

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:
    st.header("Hello admin sriram")
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Replace with your actual authentication logic
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid username or password")

# ---------------- DASHBOARD ----------------
else:

    # Header
    st.markdown("""
    <h1 style='font-family:New Times Roman; color:blue;'>
        My Dashboard
    </h1>
    """, unsafe_allow_html=True)
    

    # Sidebar
    with st.sidebar:
        st.header("Menu")

        if st.button("Home", width = 500):
            st.session_state.page = "Home"

        if st.button("Profile", width = 500):
            st.session_state.page = "Profile"

        if st.button("Settings", width = 500):
            st.session_state.page = "Settings"

        st.markdown("---")

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.page = "Home"
            st.rerun()

    # Main Content
    st.header(st.session_state.page)

    if st.session_state.page == "Home":
        st.write("🏠 Home page content")
        st.image("photo.jpeg")

    elif st.session_state.page == "Profile":
        st.write("👤 Profile page content")

    elif st.session_state.page == "Settings":
        st.write("⚙️ Settings page content")

    # Footer
    st.markdown("---")
    st.caption("© 2026 My Website")
