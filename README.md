# Job Application Tracker

Job Application Tracker is a command-line Python application for managing job applications throughout your job search. It supports full CRUD operations (add, view, update, delete), tracks application status, generates quick statistics, and exports your data to CSV.

## Features

- Add a new job application
- View all applications
- Update application status
- Delete an application
- View statistics by status
- Export applications to CSV

## Architecture

```
┌─────────────┐
│   main.py   │  ← User interacts here (menu, input/output)
└──────┬──────┘
       │ calls functions
       ▼
┌─────────────┐
│   crud.py   │  ← Business logic (add, view, update, delete, stats, export)
└──────┬──────┘
       │ reads/writes
       ▼
┌─────────────┐
│ job_tracker │  ← SQLite database file
│    .db      │
└─────────────┘
```

## Project Structure

- `main.py` — CLI menu, handles user interaction
- `crud.py` — business logic for database operations
- `db.py` — database table setup
- `job_tracker.db` — SQLite database file (created automatically on first run)
- `job_applications_export.csv` — generated CSV export

## Tech Stack

- Python 3
- SQLite (`sqlite3`)
- Pandas (for CSV export)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/MullaKamran/job-application-tracker.git
   cd job-application-tracker
   ```

2. Install dependencies:
   ```
   pip install pandas
   ```

3. Run the application:
   ```
   python main.py
   ```

The database table is created automatically the first time you run the app — no manual setup required.

## Example Usage

```
JOB APPLICATION TRACKER
1. Add a new job application
2. View all job applications
3. Update a job application
4. Delete a job application
5. View statistics
6. Export job applications to CSV
7. Exit
Enter your choice: 1
Enter company name: Google
Enter role: SWE Intern
Enter status: Applied
Enter date applied (YYYY-MM-DD): 2026-09-01
Enter notes: Referred by a friend
```

## What I Learned

Building this project helped me practice:
- Structuring a Python application with separation of concerns (UI, business logic, data layer)
- Writing safe, parameterized SQL queries to prevent SQL injection
- Designing a database schema and handling CRUD operations with SQLite
- Using Pandas for reading from and exporting to CSV
- Building a persistent, menu-driven CLI application with a clean control loop
