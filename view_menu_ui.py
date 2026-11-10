import tkinter as tk
def main():
    def viewer():
        import view_inventory
        view_inventory.view()

    def view_category():
        import view_category
        view_category.view()

    def view_vendor():
        import view_vendor
        view_vendor.view()

    def view_history():
        import view_history
        view_history.view() 

    def view_godown():
        import view_godown
        view_godown.view()  

    def back():
        root.destroy()
        import main_menu_ui
        main_menu_ui.main()   

    root = tk.Tk()
    root.title("View Menu")  
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() 
    window_width = 400
    window_height = 500
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    root.geometry(f"{window_width}x{window_height}+{x}+{y}") 

    label=tk.Label(root,text="Select your choice",font=("Helvetica", 14, "bold"))
    label.pack(pady=15)

    view_button = tk.Button(root, text="View Inventory", width=25, height=2,font=("Helvetica", 10, "bold"),command=viewer)
    view_button.pack(pady=10) 

    view_category_button=tk.Button(root, text="View Categories", width=25, height=2,font=("Helvetica", 10, "bold"), command=view_category)
    view_category_button.pack(pady=10)
    
    view_vendor_button=tk.Button(root, text="View Vendors", width=25, height=2,font=("Helvetica", 10, "bold"),command=view_vendor)
    view_vendor_button.pack(pady=10)
    
    history_button=tk.Button(root, text="View History", width=25, height=2,font=("Helvetica", 10, "bold"), command=view_history)
    history_button.pack(pady=10)

    view_godown_button=tk.Button(root, text="View Godown", width=25, height=2,font=("Helvetica", 10, "bold"), command=view_godown)
    view_godown_button.pack(pady=10)

    back_button=tk.Button(root, text="Back", width=25, height=2,font=("Helvetica", 10, "bold"),command=back)
    back_button.pack(pady=40)

    root.mainloop()