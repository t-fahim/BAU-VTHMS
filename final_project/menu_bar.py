# menu_bar.py
#Creating menu bar off home page

import tkinter as tk
from view_data import view_all_patient_data # Import the function

def create_menu(self):
    self.menu_frame = tk.Frame(self.root,background=self.menubar_color,height=self.screen_unit)
    self.menu_frame.pack(fill=tk.BOTH)

    # Add a "View Data" button
    self.view_data_button = tk.Button(
        self.menu_frame,
        text="View All Data",
        command=view_all_patient_data, # Call the imported function
        font=("Noto Sans", 12),
        bg=self.menubar_color,
        fg="white",
        relief=tk.FLAT # Make it look like part of the menu bar
    )
    self.view_data_button.pack(side=tk.LEFT, padx=10) # Pack it on the left side of the menu bar
