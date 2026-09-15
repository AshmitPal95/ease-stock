import tkinter as tk
from tkinter import ttk, messagebox


def view():
    import db.category_repo
    def fetch_data():
        return db.category_repo.fetch()

    def show_data(filter_text=""):
        rows = fetch_data()

        # Clear existing rows
        for item in tree.get_children():
            tree.delete(item)

        # Insert filtered rows
        for row in rows:
            category_id,category_name = row
            if filter_text:  # if search text entered
                if category_name.lower().startswith(filter_text.lower()):
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
                category_id_var.set(values[0])
                category_name_var.set(values[1])
    def modify_category():
        category_id = category_id_var.get()
        new_name = category_name_var.get().strip()
        if not new_name:
            messagebox.showerror("Error", "Category name cannot be empty", parent=root)
            return
        proceed=messagebox.askyesno("Confirm modification","Are you sure you want to modify",parent=root)
        if proceed:
            try:
                db.category_repo.update(new_name,category_id)
                messagebox.showinfo("Success", "Category updated successfully", parent=root)
                show_data()
                # Clear the Entry fields
                category_id_var.set("")
                category_name_var.set("")
                # Optionally clear Treeview selection too
                tree.selection_remove(tree.selection())
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update: {e}", parent=root)
        else:
            return

    def delete_category():
        category_id = category_id_var.get()
        if not category_id:
            messagebox.showerror("Error", "No category selected", parent=root)
            return
        proceed=messagebox.askyesno("Confirm deletion","Are you sure you want to delete",parent=root)
        if proceed:
            try:
                        
                db.category_repo.delete(category_id)
                messagebox.showinfo("Success", "Category deleted successfully", parent=root)
            
                # Refresh the Treeview
                show_data()
            
                # Clear the entry fields
                category_id_var.set("")
                category_name_var.set("")
            
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
    root.title("View Category")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    window_width = 450
    window_height = 400   
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

    tk.Label(search_frame, text="Search by Category Name :", font=("Helvetica", 10, "bold")).pack(side="left", padx=(0,5))
    search_var = tk.StringVar()
    # search_var.trace("w", on_search)
    search_var.trace_add("write", on_search)

    search_entry = tk.Entry(search_frame, textvariable=search_var, width=25)
    search_entry.pack(side="left", padx=(0,5))

    clear_button = tk.Button(search_frame, text="Clear", command=clear_search)
    clear_button.pack(side="left",padx=10)


    # --- Treeview ---
    columns = ("Category ID", "Category Name")
    tree = ttk.Treeview(frame, columns=columns, show="headings")

    # Configure each column individually
    tree.heading("Category ID", text="Category ID")
    tree.column("Category ID", width=60)

    tree.heading("Category Name", text="Category Name")
    tree.column("Category Name", width=150)

    tree.pack(fill="both", expand=True, pady=10)
    tree.bind("<<TreeviewSelect>>", on_select)

    # --- Category controls in one line ---
    category_id_var = tk.StringVar()
    category_name_var = tk.StringVar()

    cat_frame = tk.Frame(frame)
    cat_frame.pack(fill="x", pady=10)

    tk.Label(cat_frame, text="Category ID:", font=("Helvetica", 10, "bold")).pack(side="left", padx=(0,5))
    tk.Label(cat_frame, textvariable=category_id_var, width=8).pack(side="left", padx=(0,10))

    tk.Label(cat_frame, text="Category Name:", font=("Helvetica", 10, "bold")).pack(side="left", padx=(0,5))
    tk.Entry(cat_frame, textvariable=category_name_var, width=20).pack(side="left", padx=(0,5))

    # --- Buttons below controls ---
    btn_frame = tk.Frame(frame)
    btn_frame.pack(pady=10)

    modify_button = tk.Button(btn_frame, text="Modify", command=modify_category)
    modify_button.pack(side="left", padx=10)

    delete_button = tk.Button(btn_frame, text="Delete", command=delete_category)
    delete_button.pack(side="left", padx=10)

    close_button = tk.Button(btn_frame, text="Close", command=close_window)
    close_button.pack(side="left", padx=10)

    # Load initial data
    show_data()

    # Wait until closed
    root.wait_window(root)
