def add():
    import tkinter as tk
    from tkinter import messagebox
    import db.vendor_repo   

    def add_vendor():
        name_input = name_entry.get().strip()   # strip removes leading/trailing spaces
        address_input = address_entry.get("1.0", tk.END).strip()

        # Check if vendor name is empty
        if not name_input:
            messagebox.showerror("Error", "Vendor name cannot be empty", parent=root)
            return

        result = db.vendor_repo.check(name_input)
        if result > 0:
            messagebox.showerror("Error", "Vendor Already Exists", parent=root)
        else:
            try:
                db.vendor_repo.add(name_input, address_input)
                messagebox.showinfo("Operation", "Vendor Added Successfully", parent=root)
                clear()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add: {e}", parent=root)


    def close_window():    
        root.destroy()
    def clear():
        name_entry.delete(0,tk.END)
        address_entry.delete("1.0",tk.END)

    root=tk.Toplevel()
    root.title("Add Vendor")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    window_width = 500
    window_height = 350   
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2) 
       
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    

    root.transient()
    root.grab_set()
    root.protocol("WM_DELETE_WINDOW", close_window)

    name_label=tk.Label(root,text="Enter Vendor Name to be Added:", width=35, height=2,font=("Helvetica", 10, "bold"))
    name_label.pack(pady=10)

    name_entry=tk.Entry(root,width=50)
    name_entry.pack(pady=10)

    address_label=tk.Label(root,text="Enter Vendor Address to be Added:", width=35, height=2,font=("Helvetica", 10, "bold"))
    address_label.pack(pady=10)

    address_entry=tk.Text(root,width=50,height=5,wrap="word")
    address_entry.pack(pady=10)

    submit_button=tk.Button(root,text="Add Vendor",width=25, height=2,font=("Helvetica", 10, "bold"),command=add_vendor)
    submit_button.pack(side="left",padx=10)
    clear_button=tk.Button(root,text="Clear",width=25, height=2,font=("Helvetica", 10, "bold"),command=clear)
    clear_button.pack(side="left",padx=10)
    root.wait_window(root)

    
