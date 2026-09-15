import tkinter as tk
from tkinter import ttk, messagebox

def withdraw():
    import db.inventory_repo
    def fetch_data():
        return db.inventory_repo.fetch()
    def show_data(filter_text=""):
            for item in tree.get_children():
                tree.delete(item)
            rows = fetch_data()
            for row in rows:
                entry_id, invoice_number, category_id, grade, garden_name, vendor_id, num_of_units, unit_wt, rate, worth = row
                # Filter by invoice_number starting characters
                if filter_text:
                    if not str(invoice_number).startswith(filter_text):
                        continue
                tree.insert("", "end", values=row)

    def make_withdrawal():
            
            limit=units_limit.get()
            withdrawn=units_withdrawn.get()

            if limit < withdrawn: 
                messagebox.showerror("Insufficient Balance","The number of units to be withdrawn is more than the balance available ",parent=root)
                
            else:
                try:
                    choice=messagebox.askyesno("Confirm Withdrawal","Confirm Withdrawal")
                    if choice:
                         db.inventory_repo.withdraw(withdrawn,entry_id.get())
                         show_data()
                    else:
                         return
                except Exception as e:
                     messagebox.showerror("Error",f"Withdrawal failed:{e}",parent=root)
                      
    def on_search(*args):
            filter_text = search_var.get().strip()
            show_data(filter_text)

    def on_select(event):
            selected = tree.focus()
            if selected:
                values = tree.item(selected, "values")
                if values:
                     entry_id.set(values[0])
                     units_limit.set(values[6])
                                   
    def clear_search():
            search_var.set("")
            show_data()
    def close_window():
            root.destroy()

        
    # Create withdrawal window
    root = tk.Toplevel()
    root.title("Make Withdrawal")

    # Center the window on screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    window_width = 1000
    window_height = 400   
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Keep window on top of parent and block other interactions
    root.transient()
    root.grab_set()
    root.protocol("WM_DELETE_WINDOW", close_window)

    # Main frame
    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(fill="both", expand=True)

    # ---------------- Search Section ----------------
    search_frame = tk.Frame(frame)
    search_frame.pack(fill="x", pady=(0, 10))

    tk.Label(search_frame, text="Search Invoice:", font=("Helvetica", 10, "bold")).pack(side="left", padx=(0,5))
    search_var = tk.StringVar()
    search_var.trace_add("write", on_search)  # trigger search on text change

    search_entry = tk.Entry(search_frame, textvariable=search_var, width=25)
    search_entry.pack(side="left", padx=(0,5))

    clear_button = tk.Button(search_frame, text="Clear", font=("Helvetica", 10, "bold"), command=clear_search)
    clear_button.pack(side="left", padx=10)

    # ---------------- Treeview Section ----------------
    # columns = ("Entry ID", "Invoice Number","Category","Grade","Garden Name","Vendor",
    #         "No. of Units","No. of Units Withdrawn","Unit Weight(in KG)","Rate","Worth")

    columns = ("Entry ID", "Invoice Number","Category","Grade","Garden Name","Vendor",
            "No. of Units","Unit Weight(in KG)","Rate","Worth")

    tree = ttk.Treeview(frame, columns=columns, show="headings")

    # Define column headings and widths
    tree.heading("Entry ID", text="Entry ID")
    tree.column("Entry ID", width=20)

    tree.heading("Invoice Number", text="Invoice Number")
    tree.column("Invoice Number", width=50)

    tree.heading("Category", text="Category")
    tree.column("Category", width=35)

    tree.heading("Grade", text="Grade")
    tree.column("Grade", width=50)

    tree.heading("Garden Name", text="Garden Name")
    tree.column("Garden Name", width=50)

    tree.heading("Vendor", text="Vendor")
    tree.column("Vendor", width=20)

    tree.heading("No. of Units", text="No. of Units")
    tree.column("No. of Units", width=15)

    # tree.heading("No. of Units Withdrawn", text="No. of Units Withdrawn")
    # tree.column("No. of Units Withdrawn", width=55)

    tree.heading("Unit Weight(in KG)", text="Unit weight(in KG)")
    tree.column("Unit Weight(in KG)", width=40)

    tree.heading("Rate", text="Rate")
    tree.column("Rate", width=10)

    tree.heading("Worth", text="Worth")
    tree.column("Worth", width=15)

    tree.pack(fill="both", expand=True)
    tree.bind("<<TreeviewSelect>>", on_select)

    # ---------------- Withdraw Section ----------------
    withdraw_frame = tk.Frame(frame)
    withdraw_frame.pack(pady=25)

    units_withdrawn = tk.IntVar()
    units_limit = tk.IntVar()
    entry_id = tk.IntVar()

    tk.Label(withdraw_frame, text="Maximum number of units that can be withdrawn:",
            font=("Helvetica", 10, "bold")).pack(side="left", padx=5)
    tk.Label(withdraw_frame, textvariable=units_limit, font=("Helvetica", 10)).pack(side="left", padx=5)

    tk.Entry(withdraw_frame, textvariable=units_withdrawn, width=10).pack(side="left", padx=10)

    # Withdraw button
    withdraw_button = tk.Button(withdraw_frame, text="Withdraw", font=("Helvetica", 10, "bold"),
                                command=make_withdrawal)
    withdraw_button.pack(side="left", padx=10)

    # Close button placed to the RIGHT of Withdraw button
    close_button = tk.Button(withdraw_frame, text="Close", font=("Helvetica", 10, "bold"),
                            command=close_window)
    close_button.pack(side="left", padx=10)

    # ---------------- Final Setup ----------------
    show_data()
    root.wait_window(root)
    
    