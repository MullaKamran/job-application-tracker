import streamlit as st
import requests
import pandas as pd

st.title("Job Application Tracker")
st.write("Welcome! This is your job application dashboard.")

API_URL = "http://127.0.0.1:8000"
with st.form("application_form"):
    company=st.text_input("Company Name")
    role=st.text_input("Role")
    status=st.selectbox("Status", ["Applied", "Interviewing", "Offered", "Rejected"])
    date_applied=st.date_input("Date Applied")
    notes=st.text_area("Notes")
    submitted=st.form_submit_button("Add Application")
if submitted:
     data={
        "company": company,
        "role": role,
        "status": status,
        "date_applied": str(date_applied),
        "notes": notes
     }   
    
     try:
       response= requests.post(f"{API_URL}/applications", json=data)
       if response.status_code==200:
        st.success("Application submitted successfully!")
       else:
        st.error(f"Failed to submit application: {response.status_code} - {response.text}")
            
     except requests.exceptions.ConnectionError:
        st.error("Failed to connect to the API. Please ensure the backend server is running.")        
response = requests.get("http://127.0.0.1:8000/applications")
if response.status_code==200:
    st.write(response.status_code)
    st.write(response.text)
    data = response.json()
    print(data)
else:
    st.error(f"Failed: {response.status_code} - {response.text}")
df = pd.DataFrame(data, columns=["id", "company", "role", "status", "date_applied", "notes"])
st.dataframe(df)