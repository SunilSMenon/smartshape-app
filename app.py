import streamlit as st

st.title("Smart Shape - Powered by AI")
st.subheader("Sustainable weight loss for busy professionals")

st.write("""
Welcome to Smart Shape! Get personalized meal plans, effortless food logging, and actionable tips—all powered by AI.
""")

menu = ["Home", "Log Meal", "Meal Plans", "Progress"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.header("Welcome!")
    st.write("Track your journey and join our community.")

elif choice == "Log Meal":
    st.header("Log Your Meal")
    uploaded_file = st.file_uploader("Upload a photo of your meal", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Your meal", use_column_width=True)
        st.success("Meal logged! (AI analysis coming soon)")

elif choice == "Meal Plans":
    st.header("Your Personalized Meal Plan")
    st.write("Feature coming soon!")

elif choice == "Progress":
    st.header("Your Progress")
    st.write("Feature coming soon!")
