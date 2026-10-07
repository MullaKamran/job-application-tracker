import streamlit as st
import requests
import pandas as pd

st.title("Job Application Tracker")
st.write("Welcome! This is your job application dashboard.")

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