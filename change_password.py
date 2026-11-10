import tkinter as tk
from tkinter import ttk, messagebox
import password_cryptography
import password_verifier
import config
import re

def  change():

    def Hide_passkey(): #for hiding user entry with hashes
        if check_var.get():
            set_pwd_entry.config(show="*")
            confirm_pwd_entry.config(show="*")
        else:
            set_pwd_entry.config(show="")
            confirm_pwd_entry.config(show="")

    def clear(): #for clearing user entry
        set_pwd_entry.delete(0, tk.END)
        confirm_pwd_entry.delete(0, tk.END)

    def set_pwd():
        if set_pwd_entry.get()!=confirm_pwd_entry.get():
            messagebox.showerror("User Input Error","Confirm Password must be same as the Password you want to set",parent=root)
        elif  not re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$',set_pwd_entry.get()):
            messagebox.showerror("Weak Password","Password must have digits,letters and special symbols and must be at least 8 characters long",parent=root)
        else:
            try:
                passkey=set_pwd_entry.get()
                crypt_pwd=password_cryptography.hash_password(passkey)
                import mysql.connector
                conn=config.db_connector()
                cursor=conn.cursor()
                cursor.execute("UPDATE yjbbfxamb SET yjbbfxamb=%s WHERE SR_NO=1",(crypt_pwd,))
                conn.commit()
                cursor.close()
                conn.close()
                root.destroy()
                messagebox.showinfo("Success","Password has been changed successfully")
            except Exception as e:
                        messagebox.showerror("Error", f"Password Change failed: {e}", parent=root)

                


    root = tk.Toplevel()
    root.title("Change Password")
    root.transient()
    root.grab_set()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    window_width = 600
    window_height = 300
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    
    root.geometry(f"{window_width}x{window_height}+{x}+{y}") 
    
    set_pwd_label=tk.Label(root,text="Enter New Password",font=("Helvetica", 14, "bold"))
    set_pwd_label.pack(pady=15)

    set_pwd_entry=tk.Entry(root,width=50,show="*")
    set_pwd_entry.pack(pady=15)

    confirm_pwd_label=tk.Label(root,text="Confirm New Password",font=("Helvetica", 14, "bold"))
    confirm_pwd_label.pack(pady=15)

    confirm_pwd_entry=tk.Entry(root,width=50,show="*")
    confirm_pwd_entry.pack(pady=10)

    check_var=tk.BooleanVar(value=True)
    checkbox=tk.Checkbutton(root,text="Hide Password", width=25, height=2,font=("Helvetica", 10, "bold"),variable=check_var,command=Hide_passkey)
    checkbox.pack(pady=20)

    button_frame=tk.Frame(root)
    button_frame.pack(pady=15)

    set_button=tk.Button(button_frame,text="Set Password",width=25,font=("Helvetica", 14, "bold"),command=set_pwd)
    set_button.pack(side="left",padx=10)

    clear_button=tk.Button(button_frame,text="Clear",width=25,font=("Helvetica", 14, "bold"),command=clear)
    clear_button.pack(side="left",padx=10)

    root.wait_window(root)

