import tkinter as tk
from tkinter import ttk, messagebox

def view():
    import db.history_repo

    # Fetch history data from repo
    def fetch_data():
        return db.history_repo.fetch_history()  # <-- implement this in your repo

    # Display data in treeview, with optional filter
    def show_data(filter_text=""):
        for item in tree.get_children():
            tree.delete(item)
        rows = fetch_data()
        for row in rows:
            history_id, invoice_number, category_id, grade, garden_name, vendor_id, num_of_units, unit_wt, rate, operation_type, transaction_date = row
            # Filter by invoice_number starting characters
            if filter_text:
                if not str(invoice_number).startswith(filter_text):
                    continue
            tree.insert("", "end", values=row)

    # Search callback
    def on_search(*args):
        filter_text = search_var.get().strip()
        show_data(filter_text)

    # Clear search
    def clear_search():
        search_var.set("")
        show_data()

    # Close window
    def close_window():
        root.destroy()

    # ---------------- Window Setup ----------------
    root = tk.Toplevel()
    root.title("History Records")

    # Center the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 1100
    window_height = 500
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.transient()
    root.grab_set()
    root.protocol("WM_DELETE_WINDOW", close_window)

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(fill="both", expand=True)

    # ---------------- Search Section ----------------
    search_frame = tk.Frame(frame)
    search_frame.pack(fill="x", pady=(0, 10))

    tk.Label(search_frame, text="Search Invoice:", font=("Helvetica", 10, "bold")).pack(side="left", padx=(0,5))
    search_var = tk.StringVar()
    search_var.trace_add("write", on_search)

    search_entry = tk.Entry(search_frame, textvariable=search_var, width=25)
    search_entry.pack(side="left", padx=(0,5))

    clear_button = tk.Button(search_frame, text="Clear", font=("Helvetica", 10, "bold"), command=clear_search)
    clear_button.pack(side="left", padx=10)

    # ---------------- Treeview Section ----------------
    columns = ("History ID", "Invoice Number", "Category", "Grade", "Garden Name", "Vendor",
               "No. of Units", "Unit Weight(in KG)", "Rate", "Operation Type", "Transaction Date")

    tree = ttk.Treeview(frame, columns=columns, show="headings")

    # Define headings and widths
    tree.heading("History ID", text="History ID")
    tree.column("History ID", width=60)

    tree.heading("Invoice Number", text="Invoice Number")
    tree.column("Invoice Number", width=100)

    tree.heading("Category", text="Category")
    tree.column("Category", width=80)

    tree.heading("Grade", text="Grade")
    tree.column("Grade", width=80)

    tree.heading("Garden Name", text="Garden Name")
    tree.column("Garden Name", width=120)

    tree.heading("Vendor", text="Vendor")
    tree.column("Vendor", width=80)

    tree.heading("No. of Units", text="No. of Units")
    tree.column("No. of Units", width=100)

    tree.heading("Unit Weight(in KG)", text="Unit Weight(in KG)")
    tree.column("Unit Weight(in KG)", width=120)

    tree.heading("Rate", text="Rate")
    tree.column("Rate", width=80)

    tree.heading("Operation Type", text="Operation Type")
    tree.column("Operation Type", width=120)

    tree.heading("Transaction Date", text="Transaction Date")
    tree.column("Transaction Date", width=120)

    tree.pack(fill="both", expand=True)

    # ---------------- Close Button ----------------
    btn_frame = tk.Frame(frame)
    btn_frame.pack(pady=10)

    close_button = tk.Button(btn_frame, text="Close", font=("Helvetica", 10, "bold"), command=close_window)
    close_button.pack(side="right", padx=10)

    # ---------------- Final Setup ----------------
    show_data()
    root.wait_window(root)
