
def make_entry():
    import tkinter as tk
    from tkinter import ttk, messagebox
    import db.inventory_repo
    import mysql.connector

    def connect():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="Siemens1234$",
            database="ACCOUNTING_RECORDS"
        )

    # Dictionaries to map display text → ID
    category_map = {}
    vendor_map = {}

    import re

    def insert_entry():
        invoice_num = invoice_num_entry.get().strip()
        grade = grade_entry.get().strip()
        garden_name = garden_name_entry.get().strip()
        num_of_units = num_of_units_entry.get().strip()
        unit_wt = unit_wt_entry.get().strip()
        rate = rate_entry.get().strip()

        # Get selected display text
        category_display = category_entry.get()
        vendor_display = vendor_entry.get()

        # Look up IDs from maps
        category_id = category_map.get(category_display)
        vendor_id = vendor_map.get(vendor_display)

        if not category_id or not vendor_id:
            messagebox.showerror("Error", "Please select both Category and Vendor", parent=root)
            return

        # ---------------- VALIDATION ----------------
        # Invoice number: alphanumeric, max length 10
        if not re.match(r'^[A-Za-z0-9]+$', invoice_num):
            messagebox.showerror("Validation Error", "Invoice number must be alphanumeric", parent=root)
            return
        if len(invoice_num) > 10:
            messagebox.showerror("Validation Error", "Invoice number must not exceed 10 characters", parent=root)
            return

        # Grade: alphanumeric, max length 10
        if not re.match(r'^[A-Za-z0-9]+$', grade):
            messagebox.showerror("Validation Error", "Grade must be alphanumeric", parent=root)
            return
        if len(grade) > 10:
            messagebox.showerror("Validation Error", "Grade must not exceed 10 characters", parent=root)
            return

        # Garden name: alphanumeric with spaces, max length 20
        if not re.match(r'^[A-Za-z0-9 ]+$', garden_name):
            messagebox.showerror("Validation Error", "Garden name must be alphanumeric or contain spaces", parent=root)
            return
        if len(garden_name) > 20:
            messagebox.showerror("Validation Error", "Garden name must not exceed 20 characters", parent=root)
            return



        # Number of units: unsigned integer up to 10000
        try:
            num_of_units_val = int(num_of_units)
            if num_of_units_val < 0:
                raise ValueError
            if num_of_units_val > 10000:
                messagebox.showerror("Validation Error", "Number of units too high (max 10000)", parent=root)
                return
        except ValueError:
            messagebox.showerror("Validation Error", "Number of units must be an integer", parent=root)
            return

        # Unit weight: unsigned decimal up to 3 places, max 500
        try:
            if not re.match(r'^\d+(\.\d{1,3})?$', unit_wt):
                raise ValueError
            unit_wt_val = float(unit_wt)
            if unit_wt_val < 0:
                raise ValueError
            if unit_wt_val > 500:
                messagebox.showerror("Validation Error", "Unit weight too high (max 500)", parent=root)
                return
        except ValueError:
            messagebox.showerror("Validation Error", "Unit weight must be a decimal number (up to 3 places)", parent=root)
            return

        # Rate: currency up to 2 places, max 50000
        try:
            if not re.match(r'^\d+(\.\d{1,2})?$', rate):
                raise ValueError
            rate_val = float(rate)
            if rate_val < 0:
                raise ValueError
            if rate_val > 50000:
                messagebox.showerror("Validation Error", "Unit rate too high (max 50000)", parent=root)
                return
        except ValueError:
            messagebox.showerror("Validation Error", "Rate must be a decimal number (up to 2 places)", parent=root)
            return

        # ---------------- END VALIDATION ----------------

        result = db.inventory_repo.check(invoice_num)
        if result > 0:
            messagebox.showerror("Error", "Entry Already Exists", parent=root)
        else:
            try:
                db.inventory_repo.add(invoice_num, category_id, grade, garden_name,
                                    vendor_id, num_of_units_val, unit_wt_val, rate_val)
                messagebox.showinfo("Operation", "Entry Added Successfully", parent=root)
                clear()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add: {e}", parent=root)

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

    def clear():
        invoice_num_entry.delete(0, tk.END)
        category_entry.set("")
        vendor_entry.set("")
        grade_entry.delete(0, tk.END)
        garden_name_entry.delete(0, tk.END)
        num_of_units_entry.delete(0, tk.END)
        unit_wt_entry.delete(0, tk.END)
        rate_entry.delete(0, tk.END)

 
    root = tk.Toplevel()
    root.title("Add Entry")
    root.transient()
    root.grab_set()

    # Layout
    invoice_num_label = tk.Label(root, text="Enter Invoice Number:", font=("Helvetica", 10, "bold"))
    invoice_num_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    invoice_num_entry = tk.Entry(root, width=50)
    invoice_num_entry.grid(row=0, column=1, padx=10, pady=5)

    category_label = tk.Label(root, text="Select Category:", font=("Helvetica", 10, "bold"))
    category_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    category_entry = ttk.Combobox(root, values=category_list(), width=47, state="readonly")
    category_entry.grid(row=1, column=1, padx=10, pady=5)

    grade_label = tk.Label(root, text="Enter Grade:", font=("Helvetica", 10, "bold"))
    grade_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    grade_entry = tk.Entry(root, width=50)
    grade_entry.grid(row=2, column=1, padx=10, pady=5)

    garden_name_label = tk.Label(root, text="Enter Garden Name:", font=("Helvetica", 10, "bold"))
    garden_name_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    garden_name_entry = tk.Entry(root, width=50)
    garden_name_entry.grid(row=3, column=1, padx=10, pady=5)

    vendor_label = tk.Label(root, text="Select Vendor:", font=("Helvetica", 10, "bold"))
    vendor_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    vendor_entry = ttk.Combobox(root, values=vendor_list(), width=47, state="readonly")
    vendor_entry.grid(row=4, column=1, padx=10, pady=5)

    num_of_units_label = tk.Label(root, text="Enter Number of Units:", font=("Helvetica", 10, "bold"))
    num_of_units_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    num_of_units_entry = tk.Entry(root, width=50)
    num_of_units_entry.grid(row=5, column=1, padx=10, pady=5)

    unit_wt_label = tk.Label(root, text="Enter Unit Weight (in KG):", font=("Helvetica", 10, "bold"))
    unit_wt_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
    unit_wt_entry = tk.Entry(root, width=50)
    unit_wt_entry.grid(row=6, column=1, padx=10, pady=5)

    rate_label = tk.Label(root, text="Enter Rate:", font=("Helvetica", 10, "bold"))
    rate_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
    rate_entry = tk.Entry(root, width=50)
    rate_entry.grid(row=7, column=1, padx=10, pady=5)

    button_frame = tk.Frame(root)
    button_frame.grid(row=8, column=0, columnspan=2, pady=20)
    submit_button = tk.Button(button_frame, text="Submit", width=20, height=2,
                            font=("Helvetica", 10, "bold"), command=insert_entry)
    submit_button.pack(side="left", padx=10)
    clear_button = tk.Button(button_frame, text="Clear", width=20, height=2,
                            font=("Helvetica", 10, "bold"), command=clear)
    clear_button.pack(side="left", padx=10)

    root.wait_window(root)


