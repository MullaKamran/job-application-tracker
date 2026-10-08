from unittest import result

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from crud import add_application,view_applications,update_application,delete_application
from db import create_table

app=FastAPI()
create_table()

class JobApplication(BaseModel):

    company:str
    role:str
    status:str
    date_applied:str
    notes:str
class StatusUpdate(BaseModel):
    status: str    
    
@app.post("/applications")
def create_application(application: JobApplication):
    add_application(
        application.company,
        application.role,
        application.status,
        application.date_applied,
        application.notes
    )
    return {"message": "Application added successfully"}

@app.put("/applications/{app_id}")
def update_application_endpoint(app_id: int, status_update: StatusUpdate):
    result = update_application(app_id, status_update.status)
    if not result:
        raise HTTPException(status_code=404, detail="Application not found")
    return {"message": "Application updated successfully"}

@app.delete("/applications/{app_id}")
def delete_application_endpoint(app_id: int):
    result = delete_application(app_id)
    if not result:
        raise HTTPException(status_code=404, detail="Application not found")
    return {"message": "Application deleted successfully"}
@app.get("/applications")
def get_applications():
    return view_applications()
    