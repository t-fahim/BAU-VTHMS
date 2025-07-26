#this module is for footer button and info

import tkinter as tk

def create_footer(self):

    self.button_frame = tk.Frame(self.root,height=self.screen_unit)
    self.button_frame.pack(side=tk.TOP, fill=tk.BOTH,expand=True)

    self.footer_info_frame = tk.Frame(self.root, height=20)
    self.footer_info_frame.pack(side=tk.BOTTOM, anchor=tk.S, fill=tk.X, expand=True, padx=0, pady=0)

    self.footer_text = tk.Label(self.footer_info_frame,bg=self.menubar_color, text="Created by students of B.Sc in Bioinformatics Engineering,BAU")
    self.footer_text.pack(side=tk.BOTTOM, fill=tk.X, expand=True,anchor=tk.CENTER,pady=0,padx=0)