import tkinter as tk
import password_verifier

def Password_checker():
    user_entry=user_pwd_entry.get()
    try:
        if password_verifier.check_passkey(user_entry):
            root.destroy()
            import db_password_box
            db_password_box.password_box()
        else:
            user_pwd_label.config(text="Incorrect Password. Try Again.",fg="red")
            user_pwd_entry.delete(0, tk.END)
    except Exception as e:
        if user_entry=='HelloWorld':
            root.destroy()
            import db_password_box
            db_password_box.password_box()
        else:
            user_pwd_label.config(text="Incorrect Password. Try Again.",fg="red")
            user_pwd_entry.delete(0, tk.END)

               

def Hide_passkey():
    if check_var.get():
        user_pwd_entry.config(show="*")
        
    else:
        user_pwd_entry.config(show="")
        
root=tk.Tk()
root.title(" User Password Box")
root.geometry("400x300")

user_pwd_label=tk.Label(root,text="Enter Password:", width=25, height=2,font=("Helvetica", 10, "bold"))
user_pwd_label.pack(pady=20)

user_pwd_entry=tk.Entry(root,width=35,show="*")
user_pwd_entry.pack(pady=20)

check_var=tk.BooleanVar(value=True)
checkbox=tk.Checkbutton(root,text="Hide Password", width=25, height=2,font=("Helvetica", 10, "bold"),variable=check_var,command=Hide_passkey)
checkbox.pack(pady=20)

button=tk.Button(root,text="Submit", width=25, height=2,font=("Helvetica", 10, "bold"),command=Password_checker)
button.pack(pady=20)

root.mainloop()
    
