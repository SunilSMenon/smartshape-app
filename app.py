import streamlit as st

st.title("Smart Shape - Powered by AI")
st.subheader("Sustainable weight loss for busy professionals")

st.write("""
Welcome to Smart Shape! Get personalized meal plans, effortless food logging, and actionable tips—all powered by AI.
""")

menu = ["Home", "Log Meal", "Meal Plans", "Progress"]
choice = st.sidebar.selectbox("Menu", menu)

# Initialize session state for meal logs
if "meal_logs" not in st.session_state:
    st.session_state.meal_logs = []

if choice == "Home":
    st.header("Welcome!")
    st.write("Track your journey and join our community.")

elif choice == "Log Meal":
    st.header("Log Your Meal")
    uploaded_file = st.file_uploader("Upload a photo of your meal", type=["jpg", "jpeg", "png"])
    meal_note = st.text_input("Add a note about your meal (optional)")
    if st.button("Save Meal"):
        if uploaded_file is not None:
            st.session_state.meal_logs.append({
                "image": uploaded_file,
                "note": meal_note
            })
            st.success("Meal logged!")
        else:
            st.warning("Please upload a photo before saving.")

    st.subheader("Your Logged Meals")
    for i, meal in enumerate(st.session_state.meal_logs):
        st.image(meal["image"], caption=f"Meal {i+1}", use_column_width=True)
        st.write(meal["note"])

elif choice == "Meal Plans":
    st.header("Your Personalized Meal Plan")
    st.write("Feature coming soon!")

elif choice == "Progress":
    st.header("Your Progress")

    # Initialize session state for progress tracking
    if "weights" not in st.session_state:
        st.session_state.weights = []
        st.session_state.dates = []

    # Input for today's weight
    import datetime
    today = datetime.date.today()
    weight = st.number_input("Enter your weight for today (kg):", min_value=0.0, max_value=300.0, step=0.1)
    if st.button("Save Weight"):
        st.session_state.weights.append(weight)
        st.session_state.dates.append(today)
        st.success("Weight saved!")

    # Show progress chart if there is data
    if st.session_state.weights:
        st.subheader("Progress Chart")
        import pandas as pd
        df = pd.DataFrame({
            "Date": st.session_state.dates,
            "Weight": st.session_state.weights
        })
        st.line_chart(df.set_index("Date"))
        st.write(df)
    else:
        st.info("No progress data yet. Enter your weight to get started!")

