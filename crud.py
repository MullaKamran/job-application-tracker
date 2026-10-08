import pandas as pd
from db import get_connection


def add_application(company, role, status, date_applied, notes):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO job_applications (company, role, status, date_applied, notes) "
        "VALUES (?, ?, ?, ?, ?)",
        (company, role, status, date_applied, notes),
    )
    conn.commit()
    conn.close()


def view_applications():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM job_applications")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_application(app_id, new_status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE job_applications SET status = ? WHERE id = ?",
        (new_status, app_id),
    )
    conn.commit()
    changed = cursor.rowcount > 0
    conn.close()
    return changed


def delete_application(app_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM job_applications WHERE id = ?", (app_id,))
    conn.commit()
    changed = cursor.rowcount > 0
    conn.close()
    return changed


def get_statistics():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT status, COUNT(*) FROM job_applications GROUP BY status"
    )
    status_count = cursor.fetchall()
    conn.close()
    return status_count


def export_to_csv():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM job_applications", conn)
    conn.close()
    df.to_csv("job_applications_export.csv", index=False)