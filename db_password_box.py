import main
import tkinter as tk
import mysql.connector
import config

def password_box():
    def Hide_passkey():
        if check_var.get():
            db_pwd_entry.config(show="*")
        else:
            db_pwd_entry.config(show="")

    def Password_checker():
        db_pwd=db_pwd_entry.get()
        try:
            conn = mysql.connector.connect(
                    host="localhost",  
                    user='root',
                    password=f"{db_pwd}"
                )
            conn.close()
            config.get_db_password(db_pwd)
            root.destroy()
            main.main_function()
        except mysql.connector.Error as err:
            db_pwd_label.config(text="Incorrect Database Password. Try Again.",fg="red")



    root=tk.Tk()
    root.title("Database Password Box")
    root.geometry("400x300")

    db_pwd_label=tk.Label(root,text="Enter Database Password:", width=50, height=2,font=("Helvetica", 10, "bold"))
    db_pwd_label.pack(pady=20)

    db_pwd_entry=tk.Entry(root,width=35)
    db_pwd_entry.pack(pady=20)

    check_var=tk.BooleanVar()
    checkbox=tk.Checkbutton(root,text="Hide Password", width=25, height=2,font=("Helvetica", 10, "bold"),variable=check_var,command=Hide_passkey)
    checkbox.pack(pady=20)

    button=tk.Button(root,text="Submit", width=25, height=2,font=("Helvetica", 10, "bold"),command=Password_checker)
    button.pack(pady=20)

    root.mainloop()
