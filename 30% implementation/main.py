import os
import tkinter as tk
from banner import create_banner
from menu_bar import create_menu
from information import information_frame
from footer import create_footer
from PIL import Image, ImageTk


class Home_window:
    def __init__(self, root):
        # Variables
        self.banner_color = "#0C0950"
        self.background_color = "#FBE4D6"
        self.menubar_color = "#CA7842"
        # Get the folder where the script is located
        self.base_dir = os.path.dirname(__file__)

        #input variable
        self.sex = tk.StringVar()

        self.root = root
        self.root.title("Veterinary Teaching Hospital")  # Set Title
        self.root.configure(bg=self.background_color)  # Set background color

        # Get screen width and height.
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.screen_unit = self.screen_height/20

        # Setting window width and height.
        self.root.geometry(str(self.screen_width) + "x" + str(self.screen_height))
        self.root.minsize(1000,650)

        # Setting icon
        vth_icon_path = os.path.join(self.base_dir, "..", "images", "vth_icon.png")
        icon_img = Image.open(vth_icon_path)
        icon_img = icon_img.resize((32,32))
        icon = ImageTk.PhotoImage(icon_img)
        self.root.iconphoto(False, icon)

        # Creating banner using creat_banner function in banner module.
        create_banner(self)

        # Creating menubar using creat_menu function in menu_bar module
        create_menu(self)

        # Creating information frame using information_frame in information module
        information_frame(self)

        # Creating footer frame using creat_footer in footer module
        create_footer(self)


# Creating home window.
window = tk.Tk()
home_window = Home_window(window)
window.mainloop()
