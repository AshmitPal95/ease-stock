def add():
    import tkinter as tk
    from tkinter import messagebox
    import db.category_repo 
    

    def insert_category():
        user_input=entry.get()
        result=db.category_repo.check(user_input)
        if result>0:
            messagebox.showerror("Error","Category Already Exists",parent=root)
        else:
            try:
                db.category_repo.add(user_input)
                messagebox.showinfo("Operation","Category Added Sucessfully",parent=root)
                clear()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add: {e}", parent=root)    
            
    def close_window():    
        root.destroy()
    def clear():
        entry.delete(0,tk.END)

    root=tk.Toplevel()
    root.title("Add Category")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    window_width = 400
    window_height = 300   
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2) 
       
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    

    root.transient()
    root.grab_set()
    root.protocol("WM_DELETE_WINDOW", close_window)

    label=tk.Label(root,text="Enter Category to be Added:", width=25, height=2,font=("Helvetica", 10, "bold"))
    label.pack(pady=20)

    entry=tk.Entry(root,width=50)
    entry.pack(pady=20)

    submit_button=tk.Button(root,text="Submit",width=25, height=2,font=("Helvetica", 10, "bold"),command=insert_category)
    submit_button.pack(side="left",padx=10)
    clear_button=tk.Button(root,text="Clear",width=25, height=2,font=("Helvetica", 10, "bold"),command=clear)
    clear_button.pack(side="left",padx=10)
    root.wait_window(root)

    
