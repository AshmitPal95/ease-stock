import tkinter as tk
from tkinter import ttk, messagebox

def view():
    import db.vendor_repo
    def fetch_data():
        return db.vendor_repo.fetch()

    def show_data(filter_text=""):
        rows = fetch_data()

        # Clear existing rows
        for item in tree.get_children():
            tree.delete(item)

        # Insert filtered rows
        for row in rows:
            vendor_id,vendor_name,vendor_address,total_worth = row
            if filter_text:  # if search text entered
                if filter_text.lower() in vendor_name.lower():
                    tree.insert("", "end", values=row)
            else:  # show all if no filter
                tree.insert("", "end", values=row)

    def on_search(*args):
        filter_text = search_var.get().strip()
        show_data(filter_text)

    def clear_search():
        search_var.set("")
        show_data()
    def on_select(event):
        selected = tree.focus()
        if selected:
            values = tree.item(selected, "values")
            if values:
                vendor_id_var.set(values[0])
                vendor_name_var.set(values[1])
                vendor_address_text.delete("1.0", tk.END)
                vendor_address_text.insert("1.0", values[2])
                total_worth_var.set(values[3])
    def modify_vendor():
        vendor_id = vendor_id_var.get()
        new_name = vendor_name_var.get().strip()
        new_address=vendor_address_text.get("1.0", "end-1c").strip()
        if not new_name:
            messagebox.showerror("Error", "Vendor name cannot be empty", parent=root)
            return
        proceed=messagebox.askyesno("Confirm modification","Are you sure you want to modify",parent=root)
        if proceed:
            try:
                db.vendor_repo.update(new_name,new_address,vendor_id)
                messagebox.showinfo("Success", "Vendor updated successfully", parent=root)
                show_data()
                # Clear the Entry fields
                vendor_id_var.set("")
                vendor_name_var.set("")
                vendor_address_text.delete("1.0", tk.END)
                total_worth_var.set(0.0)
                # Optionally clear Treeview selection too
                tree.selection_remove(tree.selection())
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update: {e}", parent=root)
        else:
            return

    def delete_vendor():
        vendor_id = vendor_id_var.get()
        if not vendor_id:
            messagebox.showerror("Error", "No Vendor selected", parent=root)
            return
        proceed=messagebox.askyesno("Confirm deletion","Are you sure you want to delete",parent=root)
        if proceed:
            try:
                        
                db.vendor_repo.delete(vendor_id)
                messagebox.showinfo("Success", "Vendor deleted successfully", parent=root)
            
                # Refresh the Treeview
                show_data()
            
                # Clear the entry fields
                vendor_id_var.set("")
                vendor_name_var.set("")
                vendor_address_text.delete("1.0", tk.END)
                total_worth_var.set(0.0)
            
                # Clear Treeview selection
                tree.selection_remove(tree.selection())
            
            except Exception as e:
                        messagebox.showerror("Error", f"Failed to delete: {e}", parent=root)
        else:
            return
            
        
    def close_window():
        root.destroy()

    # Create modal Toplevel
    root = tk.Toplevel()
    root.title("View Vendor")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    window_width = 800
    window_height = 500   
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2) 
       
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # --- Modal behavior ---
    
    root.transient()   # keep on top of parent
    root.grab_set()              # block interaction with other windows
    root.protocol("WM_DELETE_WINDOW", close_window)

    # Frame for margins
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(fill="both", expand=True)

    # --- Search controls ---
    search_frame = tk.Frame(frame)
    search_frame.pack(fill="x", pady=(0, 10))

    tk.Label(search_frame, text="Search:", font=("Helvetica", 10, "bold")).pack(side="left", padx=(0,5))
    search_var = tk.StringVar()
    # search_var.trace("w", on_search)
    search_var.trace_add("write", on_search)

    search_entry = tk.Entry(search_frame, textvariable=search_var, width=25)
    search_entry.pack(side="left", padx=(0,5))

    clear_button = tk.Button(search_frame, text="Clear", command=clear_search)
    clear_button.pack(side="left",padx=10)


    # --- Treeview ---
    columns = ("Vendor ID", "Vendor Name","Vendor Address","Total Worth")
    tree = ttk.Treeview(frame, columns=columns, show="headings")

    # Configure each column individually
    tree.heading("Vendor ID", text="Vendor ID")
    tree.column("Vendor ID", width=60)

    tree.heading("Vendor Name", text="Vendor Name")
    tree.column("Vendor Name", width=50)

    tree.heading("Vendor Address", text="Vendor Address")
    tree.column("Vendor Address", width=150)

    tree.heading("Total Worth", text="Total Worth")
    tree.column("Total Worth",width=100)
    

    tree.pack(fill="both", expand=True, pady=10)
    tree.bind("<<TreeviewSelect>>", on_select)

    # --- Category controls in one line ---
    vendor_id_var = tk.StringVar()
    vendor_name_var = tk.StringVar()
    total_worth_var=tk.DoubleVar()
  

    cat_frame_1 = tk.Frame(frame)
    cat_frame_1.pack(fill="x", pady=10)

    tk.Label(cat_frame_1, text="Vendor ID:", font=("Helvetica", 10, "bold")).pack(side="left", padx=(0,5))
    tk.Label(cat_frame_1, textvariable=vendor_id_var, width=8).pack(side="left", padx=(0,10))

    tk.Label(cat_frame_1, text="Vendor Name:", font=("Helvetica", 10, "bold")).pack(side="left", padx=(0,5))
    tk.Entry(cat_frame_1, textvariable=vendor_name_var, width=20).pack(side="left", padx=(0,5))

    cat_frame_2 = tk.Frame(frame)
    cat_frame_2.pack(fill="x", pady=10)

    tk.Label(cat_frame_2, text="Vendor Address:", font=("Helvetica", 10, "bold")).pack(side="left", padx=(0,5))
    vendor_address_text=tk.Text(cat_frame_2,width=50,height=4,wrap="word")
    vendor_address_text.pack(side="left", padx=(0,5))

    tk.Label(cat_frame_2, text="Total Worth:", font=("Helvetica", 10, "bold")).pack(side="left", padx=(0,5))
    tk.Label(cat_frame_2, textvariable=total_worth_var, width=8).pack(side="left", padx=(0,10))

    # --- Buttons below controls ---
    btn_frame = tk.Frame(frame)
    btn_frame.pack(pady=10)

    modify_button = tk.Button(btn_frame, text="Modify", command=modify_vendor)
    modify_button.pack(side="left", padx=10)

    delete_button = tk.Button(btn_frame, text="Delete", command=delete_vendor)
    delete_button.pack(side="left", padx=10)

    close_button = tk.Button(btn_frame, text="Close", command=close_window)
    close_button.pack(side="left", padx=10)

    # Load initial data
    show_data()

    # Wait until closed
    root.wait_window(root)
