import streamlit as st
import requests
import pandas as pd
from pydantic import BaseModel, Field

st.title("Job Application Tracker")
st.write("Welcome! This is your job application dashboard.")

API_URL = "http://127.0.0.1:8000"

# ---------- Add form ----------
with st.form("application_form"):
    company = st.text_input("Company Name")
    role = st.text_input("Role")
    status = st.selectbox("Status", ["Applied", "Interviewing", "Offered", "Rejected"])
    date_applied = st.date_input("Date Applied")
    notes = st.text_area("Notes")
    submitted = st.form_submit_button("Add Application")
    

if submitted:
    if not company.strip() or not role.strip():
        st.error("Company and Role are required")
    else:
        payload = {
            "company": company,
            "role": role,
            "status": status,
            "date_applied": str(date_applied),
            "notes": notes,
        }
        try:
            response = requests.post(f"{API_URL}/applications", json=payload)
            if response.status_code == 200:
                st.success("Application submitted successfully!")
            else:
                st.error(f"Failed to submit application: {response.status_code} - {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("Failed to connect to the API. Please ensure the backend server is running.")

# ---------- Fetch applications ----------
try:
    response = requests.get(f"{API_URL}/applications")
    data = response.json()
except requests.exceptions.ConnectionError:
    st.error("API not running")
    data = []

labels = [f"{item[0]} - {item[1]} - {item[2]}" for item in data]
st.write(labels)
options = {f"{item[0]} - {item[1]} - {item[2]}": item[0] for item in data}

if options:
    choice = st.selectbox("Select an application", list(options.keys()))
    app_id = options[choice]
    st.write(app_id)
else:
    st.info("No applications yet")

# ---------- Table ----------
df = pd.DataFrame(data, columns=["id", "company", "role", "status", "date_applied", "notes"])
st.dataframe(df)
if st.button("Delete"):
    response = requests.delete(f"{API_URL}/applications/{app_id}")
    if response.status_code == 200:
        st.success("Deleted")
        st.rerun()
    else:
        st.error(f"Failed: {response.status_code}")
with st.form("update_form"):
    new_status = st.selectbox("New status", ["Applied", "Interviewing", "Offered", "Rejected"])
    new_role = st.text_input("New role (leave empty to keep the current one)")
    update_clicked = st.form_submit_button("Update")

if update_clicked:
    body = {"status": new_status}
    if new_role.strip():
        body["role"] = new_role.strip()
    try:
        response = requests.put(f"{API_URL}/applications/{app_id}", json=body)
        if response.status_code == 200:
            st.success("Updated")
            st.rerun()
        else:
            st.error(f"Failed: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("API not running")