import sqlite3
import pandas as pd

def add_application(company, role, status, date_applied, notes):
    conn = sqlite3.connect("job_tracker.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO job_applications (company, role, status, date_applied, notes) VALUES (?, ?, ?, ?, ?)",
        (company, role, status, date_applied, notes)
    )
    conn.commit()
    conn.close()

def view_applications():
    conn = sqlite3.connect("job_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM job_applications")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_application(app_id, new_status):
    conn = sqlite3.connect("job_tracker.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE job_applications SET status=? WHERE id=?", (new_status, app_id))
    conn.commit()
    conn.close()

def delete_application(app_id):
    conn = sqlite3.connect("job_tracker.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM job_applications WHERE id=?", (app_id,))
    conn.commit()
    conn.close()
    
def get_statistics():
    conn=sqlite3.connect("job_tracker.db")
    cursor=conn.cursor()
    cursor.execute("SELECT status,COUNT(*)FROM job_applications GROUP BY status") 
    status_count=cursor.fetchall()
    conn.close()   
    return status_count


def export_to_csv():
    conn = sqlite3.connect("job_tracker.db")
    df = pd.read_sql_query("SELECT * FROM job_applications", conn)
    conn.close()
    df.to_csv("job_applications_export.csv", index=False)