import tkinter as tk


def Password_checker():
    user_entry=user_pwd_entry.get()
    passkey='Ashmit1234$'
    if user_entry!=passkey:
        user_pwd_label.config(text="Incorrect Password. Try Again.",fg="red")
    else:
        root.destroy()
        import main
        main.main_function()        

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

user_pwd_entry=tk.Entry(root,width=35)
user_pwd_entry.pack(pady=20)

check_var=tk.BooleanVar()
checkbox=tk.Checkbutton(root,text="Hide Password", width=25, height=2,font=("Helvetica", 10, "bold"),variable=check_var,command=Hide_passkey)
checkbox.pack(pady=20)

button=tk.Button(root,text="Submit", width=25, height=2,font=("Helvetica", 10, "bold"),command=Password_checker)
button.pack(pady=20)

root.mainloop()
    
