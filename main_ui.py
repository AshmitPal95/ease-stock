import tkinter as tk
def entry_maker():
    import entry_maker
    entry_maker.make_entry()
def viewer():
    import view_inventory
    view_inventory.view()
def withdraw():
    import withdrawal_maker
    withdrawal_maker.withdraw()
def add_category():
    import add_category
    add_category.add()
def view_category():
    import view_category
    view_category.view()
def add_vendor():
    import add_vendor
    add_vendor.add()
def view_vendor():
    import view_vendor
    view_vendor.view()
def view_history():
    import view_history
    view_history.view()

def main():
    root = tk.Tk()
    root.title("Inventory Management System")  
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    window_width = 450
    window_height = 580  
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2) 
   
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label=tk.Label(text="Select your choice",font=("Helvetica", 14, "bold"))
    label.pack(pady=15)

    entry_button = tk.Button(root, text="Add Entry", width=25, height=2, font=("Helvetica", 10, "bold"),command=entry_maker)
    entry_button.pack(pady=10)

    view_button = tk.Button(root, text="View Inventory", width=25, height=2,font=("Helvetica", 10, "bold"),command=viewer)
    view_button.pack(pady=10)

    withdraw_button=tk.Button(root,text="Make Withdrawal",width=25,height=2,font=("Helvetica", 10, "bold"),command=withdraw)
    withdraw_button.pack(pady=10)

    add_category_button=tk.Button(root, text="Add Category", width=25, height=2,font=("Helvetica", 10, "bold"),command=add_category)
    add_category_button.pack(pady=10)

    view_category_button=tk.Button(root, text="View Categories", width=25, height=2,font=("Helvetica", 10, "bold"), command=view_category)
    view_category_button.pack(pady=10)

    add_vendor_button=tk.Button(root, text="Add Vendor", width=25, height=2,font=("Helvetica", 10, "bold"),command=add_vendor)
    add_vendor_button.pack(pady=10)

    view_vendor_button=tk.Button(root, text="View Vendors", width=25, height=2,font=("Helvetica", 10, "bold"),command=view_vendor)
    view_vendor_button.pack(pady=10)

    history_button=tk.Button(root, text="History", width=25, height=2,font=("Helvetica", 10, "bold"), command=view_history)
    history_button.pack(pady=10)
        
    root.mainloop()

