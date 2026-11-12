import tkinter as tk
import password_verifier
from tkinter import messagebox
def main():
    def password_checker():
        user_entry=user_pwd_entry.get()
        try:
            if password_verifier.check_passkey(user_entry):
                root.destroy()
                import main_menu_ui
                main_menu_ui.main()
            else:
                user_pwd_label.config(text="Incorrect Password. Try Again.",fg="red")
                user_pwd_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error","Verification Failed",parent=root)

               
    def close_window():
        root.destroy()
        import main_menu_ui
        main_menu_ui.main()

    def Hide_passkey():
        if check_var.get():
            user_pwd_entry.config(show="*")
            
        else:
            user_pwd_entry.config(show="")
            
    root=tk.Tk()
    root.protocol("WM_DELETE_WINDOW", close_window)
    root.title("Verify User")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    window_width = 400
    window_height = 300
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2) 

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    user_pwd_label=tk.Label(root,text="Enter Password:", width=25, height=2,font=("Helvetica", 10, "bold"))
    user_pwd_label.pack(pady=20)

    user_pwd_entry=tk.Entry(root,width=35,show="*")
    user_pwd_entry.pack(pady=20)

    check_var=tk.BooleanVar(value=True)
    checkbox=tk.Checkbutton(root,text="Hide Password", width=25, height=2,font=("Helvetica", 10, "bold"),variable=check_var,command=Hide_passkey)
    checkbox.pack(pady=20)

    button=tk.Button(root,text="Submit", width=25, height=2,font=("Helvetica", 10, "bold"),command=password_checker)
    button.pack(pady=20)

    root.mainloop()
    
