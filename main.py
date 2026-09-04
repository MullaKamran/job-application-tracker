from crud import add_application, get_statistics,view_applications,update_application,delete_application,export_to_csv
from db import create_table

create_table()
def main():
    while True:
        print("\n JOB APPLICATION TRACKER")
        print("1.Add a new job application")
        print("2.View all job applications")
        print("3.Update a job application")
        print("4.Delete a job application")
        print("5.View statistics")
        print("6.Export job applications to CSV")
        print("7.Exit")
        
        choice=input("Enter your choice: ")
        if choice=="1":
            company=input("Enter company name: ")
            role=input("Enter role: ")
            status=input("Enter status: ")
            date_applied=input("Enter date applied (YYYY-MM-DD): ")
            notes=input("Enter notes: ")
            add_application(company,role,status,date_applied,notes)
        
        elif choice=="2":
            applications=view_applications()
            for app in applications:
                print(app)    
        elif choice=="3":
               app_id=int(input("Enter application ID to  update:"))
               new_status=input("Enter new status: ")
               update_application(app_id,new_status)
               
        elif choice=="4":
                app_id=int(input("Enter applicarion ID to delete:"))
                delete_application(app_id)
        
        elif choice=="5":
               stats=get_statistics()
               for status,count in stats:
                print(f"Status: {status}, Count: {count}")        
                
        elif choice=="6":
            export_to_csv()
            print("Job applications exported to CSV.")
        elif choice=="7":
            print("goodbye!")
        
            break
        else:
            print("You selected option", choice)
main()            