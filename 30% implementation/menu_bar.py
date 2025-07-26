#Creating menu bar off home page

import tkinter as tk

def create_menu(self):
    self.menu_frame = tk.Frame(self.root,background=self.menubar_color,height=self.screen_unit)
    self.menu_frame.pack(fill=tk.BOTH)