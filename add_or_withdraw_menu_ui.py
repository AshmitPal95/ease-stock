import tkinter as tk
def main():

    def entry_maker():
        import entry_maker
        entry_maker.make_entry()

    def withdraw():
        import withdrawal_maker
        withdrawal_maker.withdraw()

    def add_category():
        import add_category
        add_category.add()

    def add_vendor():
        import add_vendor
        add_vendor.add()

    def back():
        root.destroy()
        import main_menu_ui
        main_menu_ui.main()


    root = tk.Tk()
    root.title("Add/Withdraw Menu")  
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    window_width = 400
    window_height = 450  
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label=tk.Label(root,text="Select your choice",font=("Helvetica", 14, "bold"))
    label.pack(pady=15)

    add_entry_button=tk.Button(root, text="Add Entry", width=25, height=2,font=("Helvetica", 10, "bold"),command=entry_maker)
    add_entry_button.pack(pady=10)

    withdraw_button=tk.Button(root,text="Make Withdrawal",width=25,height=2,font=("Helvetica", 10, "bold"),command=withdraw)
    withdraw_button.pack(pady=10)
    
    add_category_button=tk.Button(root, text="Add Category", width=25, height=2,font=("Helvetica", 10, "bold"),command=add_category)
    add_category_button.pack(pady=10)

    add_vendor_button=tk.Button(root, text="Add Vendor", width=25, height=2,font=("Helvetica", 10, "bold"),command=add_vendor)
    add_vendor_button.pack(pady=10)

    back_button=tk.Button(root, text="Back", width=25, height=2,font=("Helvetica", 10, "bold"),command=back)
    back_button.pack(pady=40)

    root.mainloop()
