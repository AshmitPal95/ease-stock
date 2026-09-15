import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import db.inventory_repo

def view():

    def close_window():
        root.destroy()

    def connect():
        return  mysql.connector.connect( host="localhost", user='root',
                                password="Siemens1234$", database="ACCOUNTING_RECORDS") 

    def fetch_data():
        return db.inventory_repo.fetch()

    def modify():
        entry_id = entry_id_var.get()
        invoice_num = invoice_num_var.get()
        category = category_var.get()
        grade = grade_var.get()
        garden_name = garden_name_var.get()
        vendor = vendor_var.get()
        num_of_units = num_units_var.get()
        unit_wt = unit_wt_var.get()
        rate = rate_var.get()

        # Get selected display text
        category_display = category_entry.get()
        vendor_display = vendor_entry.get()

        # Look up IDs from maps
        category_id = category_map.get(category_display)
        vendor_id = vendor_map.get(vendor_display)

        if not category_id or not vendor_id:
            messagebox.showerror("Error", "Invalid category or vendor selection.", parent=root)
            return

        try:
            db.inventory_repo.update( invoice_num, category_id,
                grade, garden_name, vendor_id, num_of_units,
                unit_wt, rate, entry_id )
            show_data()  # refresh treeview after modification
            messagebox.showinfo("Success", "Record updated successfully.", parent=root)
        except Exception as e:
            messagebox.showerror("Error", f"Update failed: {e}", parent=root)


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

    def category_list():
            conn = connect()
            cursor = conn.cursor()
            cursor.execute("SELECT CATEGORY_ID, CATEGORY_NAME FROM CATEGORY_LIST")
            rows = cursor.fetchall()
            cursor.close()
            conn.close()

            # Build dictionary and return display list
            categories = []
            for cid, cname in rows:
                display = f"{cname}"   # show only name, cleaner UI
                category_map[display] = cid
                categories.append(display)
            return categories
    
    def vendor_list():
            conn = connect()
            cursor = conn.cursor()
            cursor.execute("SELECT VENDOR_ID, VENDOR_NAME FROM VENDOR_LIST")
            rows = cursor.fetchall()
            cursor.close()
            conn.close()

            vendors = []
            for vid, vname in rows:
                display = f"{vname}"
                vendor_map[display] = vid
                vendors.append(display)
            return vendors

    def delete():
        entry_id=entry_id_var.get()
        db.inventory_repo.delete(entry_id)

    def on_search(*args):
        filter_text = search_var.get().strip()
        show_data(filter_text)

    def on_select(event=None):
        selected = tree.focus()
        if selected:
            values = tree.item(selected, "values")
            if values:
                entry_id_var.set(values[0])
                invoice_num_var.set(values[1])
                category_var.set(values[2])
                grade_var.set(values[3])
                garden_name_var.set(values[4])
                vendor_var.set(values[5])
                num_units_var.set(values[6])
                unit_wt_var.set(values[7])
                rate_var.set(values[8])

    def clear_search():
        search_var.set("")
        show_data()

    root = tk.Toplevel()
    root.title("View Inventory")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 1100
    window_height = 500
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.transient()   # keep on top of parent
    root.grab_set()    # block interaction with other windows
    root.protocol("WM_DELETE_WINDOW", close_window)

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack(fill="both", expand=True)

    # --- Search bar ---
    search_frame = tk.Frame(frame)
    search_frame.pack(fill="x", pady=(0, 10))

    tk.Label(search_frame, text="Search Invoice:", font=("Helvetica", 10, "bold")).pack(side="left", padx=(0,5))
    search_var = tk.StringVar()
    search_var.trace_add("write", on_search)

    search_entry = tk.Entry(search_frame, textvariable=search_var, width=25)
    search_entry.pack(side="left", padx=(0,5))

    clear_button = tk.Button(search_frame, text="Clear", font=("Helvetica", 10, "bold"), command=clear_search)
    clear_button.pack(side="left", padx=10)

    # --- Treeview ---
    # columns = ("Entry ID", "Invoice Number","Category","Grade","Garden Name","Vendor",
    #         "No. of Units","No. of Units Withdrawn","Unit Weight(in KG)","Rate","Worth")
    columns = ("Entry ID", "Invoice Number","Category","Grade","Garden Name","Vendor",
            "No. of Units","Unit Weight(in KG)","Rate","Worth")
    
    tree = ttk.Treeview(frame, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.pack(fill="both", expand=True)
    tree.bind("<<TreeviewSelect>>", on_select)

    # --- Variables ---
    entry_id_var = tk.IntVar()
    invoice_num_var = tk.IntVar()
    category_var = tk.StringVar()
    grade_var = tk.StringVar()
    garden_name_var = tk.StringVar()
    vendor_var = tk.StringVar()
    num_units_var = tk.IntVar()
    unit_wt_var = tk.DoubleVar()
    rate_var = tk.DoubleVar()

    category_map = {}
    vendor_map = {}


    # --- Form section below Treeview ---
    cat_frame = tk.Frame(frame)
    cat_frame.pack(fill="x", pady=10)

    entry_id_var = tk.IntVar()
    invoice_num_var = tk.IntVar()
    category_var = tk.StringVar()
    grade_var = tk.StringVar()
    garden_name_var = tk.StringVar()
    vendor_var = tk.StringVar()
    num_units_var = tk.IntVar()
    unit_wt_var = tk.DoubleVar()
    rate_var = tk.DoubleVar()

    category_map = {}
    vendor_map = {}

    # Row 1
    tk.Label(cat_frame, text="Entry ID:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    tk.Label(cat_frame, textvariable=entry_id_var, font=("Helvetica", 10, "bold")).grid(row=0, column=1, sticky="w", padx=5, pady=5)

    tk.Label(cat_frame, text="Invoice Number:", font=("Helvetica", 10, "bold")).grid(row=0, column=2, sticky="w", padx=5, pady=5)
    tk.Entry(cat_frame, textvariable=invoice_num_var, width=15).grid(row=0, column=3, sticky="w", padx=5, pady=5)

    tk.Label(cat_frame, text="Category:", font=("Helvetica", 10, "bold")).grid(row=0, column=4, sticky="w", padx=5, pady=5)
    category_entry = ttk.Combobox(cat_frame, textvariable=category_var, values=category_list(), width=20)
    category_entry.grid(row=0, column=5, sticky="w", padx=5, pady=5)

    tk.Label(cat_frame, text="Grade:", font=("Helvetica", 10, "bold")).grid(row=0, column=6, sticky="w", padx=5, pady=5)
    tk.Entry(cat_frame, textvariable=grade_var, width=20).grid(row=0, column=7, sticky="w", padx=5, pady=5)

    # Row 2
    tk.Label(cat_frame, text="Garden Name:", font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w", padx=5, pady=5)
    tk.Entry(cat_frame, textvariable=garden_name_var, width=20).grid(row=1, column=1, sticky="w", padx=5, pady=5)

    tk.Label(cat_frame, text="Vendor:", font=("Helvetica", 10, "bold")).grid(row=1, column=2, sticky="w", padx=5, pady=5)
    vendor_entry = ttk.Combobox(cat_frame, textvariable=vendor_var, values=vendor_list(), width=20)
    vendor_entry.grid(row=1, column=3, sticky="w", padx=5, pady=5)

    tk.Label(cat_frame, text="Number of Units:", font=("Helvetica", 10, "bold")).grid(row=1, column=4, sticky="w", padx=5, pady=5)
    tk.Entry(cat_frame, textvariable=num_units_var, width=20).grid(row=1, column=5, sticky="w", padx=5, pady=5)

    # Row 3
    tk.Label(cat_frame, text="Unit Weight (KG):", font=("Helvetica", 10, "bold")).grid(row=2, column=0, sticky="w", padx=5, pady=5)
    tk.Entry(cat_frame, textvariable=unit_wt_var, width=20).grid(row=2, column=1, sticky="w", padx=5, pady=5)

    tk.Label(cat_frame, text="Rate:", font=("Helvetica", 10, "bold")).grid(row=2, column=2, sticky="w", padx=5, pady=5)
    tk.Entry(cat_frame, textvariable=rate_var, width=20).grid(row=2, column=3, sticky="w", padx=5, pady=5)

    # Buttons aligned in Row 3
    tk.Button(cat_frame, text="Modify", font=("Helvetica", 10, "bold"), command=modify).grid(row=2, column=4, padx=10, pady=5)
    tk.Button(cat_frame, text="Delete", font=("Helvetica", 10, "bold"), command=delete).grid(row=2, column=5, padx=10, pady=5)
    tk.Button(cat_frame, text="Close", font=("Helvetica", 10, "bold"), command=close_window).grid(row=2, column=6, padx=10, pady=5)

    # --- Initial load ---
    show_data()
    root.wait_window(root)



