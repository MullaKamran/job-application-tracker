import sqlite3

DB_NAME = "job_tracker.db"

def get_connection():
    return sqlite3.connect(DB_NAME)
def create_table():
    conn=sqlite3.connect("job_tracker.db")
    cursor=conn.cursor()
    
    cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS job_applications(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company TEXT,
                    role TEXT,
                    status TEXT,
                    date_applied TEXT,
                    notes TEXT
                )"""   )
    conn.commit()
    conn.close()
    
create_table()
    