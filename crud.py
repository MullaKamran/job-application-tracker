import sqlite3

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