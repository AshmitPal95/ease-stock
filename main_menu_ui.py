import tkinter as tk

def main():
    def add_or_withdraw():
        root.destroy()
        import add_or_withdraw_menu_ui
        add_or_withdraw_menu_ui.main()
        
    def view():
        root.destroy()
        import view_menu_ui
        view_menu_ui.main()

    def change_pwd():
        root.destroy()
        import change_password
        change_password.change()

    root = tk.Tk()
    root.title("Main Menu")  
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    window_width = 400
    window_height = 400 
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2) 
   
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label=tk.Label(root,text="Select your choice",font=("Helvetica", 14, "bold"))
    label.pack(pady=15)

    add_or_withdraw_button=tk.Button(root, text="Add/Withdraw", width=25, height=2,font=("Helvetica", 10, "bold"),command=add_or_withdraw)
    add_or_withdraw_button.pack(pady=10)

    view_button=tk.Button(root, text="View", width=25, height=2,font=("Helvetica", 10, "bold"),command=view)
    view_button.pack(pady=10)
    
    change_pwd_button=tk.Button(root,text="Change Password",width=25, height=2,font=("Helvetica", 10, "bold"),command=change_pwd)
    change_pwd_button.pack(pady=10)

    

    root.mainloop()

