import streamlit as st
import pandas as pd

st.title("Attendance App for VGU staff")
st.text("Welcome to our dashboard")


if "attendance_data" not in st.session_state:
    st.session_state.attendance_data = pd.DataFrame(columns=["Name", "duty", "Status"])


name = st.text_input("Enter your name:")
duty = st.text_input("enter type of duty:")
attendance = st.selectbox("Enter your attendance:", ["Present", "Absent"])

if st.button("Submit Attendance"):
    if name and duty:
        new_row = {"Name": name, "duty": duty, "Status": attendance}
        st.session_state.attendance_data = st.session_state.attendance_data._append(new_row, ignore_index=True)
        st.success(f"Attendance Submitted for {name}!")
    else:
        st.error("Please fill all details!")

st.write(" All Attendance Records")
st.dataframe(st.session_state.attendance_data)


st.write(" staff-wise Attendance Chart")

if name.strip() != "":
 
    staff_data = st.session_state.attendance_data[st.session_state.attendance_data["Name"] == name]

    if not staff_data.empty:
        chart_data = staff_data["Status"].value_counts()
        st.bar_chart(chart_data)
    else:
        st.info(f"No attendance data found for **{name}**")
else:
    st.info("Enter a name to view attendance chart.")
