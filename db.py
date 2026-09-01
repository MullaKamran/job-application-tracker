import sqlite3

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
    