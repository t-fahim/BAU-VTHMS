# Creating banner.

import os
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw


def create_banner(self):
    # ------------- Window banner start here -----------------

    # Banner Frame
    self.frame_banner = tk.Frame(
        self.root, bg=self.banner_color, height=self.screen_unit*3
    )  # Height is set to 1/7 of total height.
    self.frame_banner.pack(side=tk.TOP, fill=tk.BOTH)

    # Lable for Veterinary Teaching Hospital.
    self.txt_label_vth = tk.Label(
        self.frame_banner,
        text="Veterinary Teaching Hospital",
        background=self.banner_color,
        foreground="white",
        font=("Noto Sans", 36),
    )
    self.txt_label_vth.place(relx=0.5, rely=0.3, anchor="center")

    # Lable for Bangladesh Agricultural University
    self.txt_label_bau = tk.Label(
        self.frame_banner,
        text="Bangladesh Agricultural University",
        background=self.banner_color,
        foreground="white",
        font=("Noto Sans", 20),
    )
    self.txt_label_bau.place(relx=0.5, rely=0.8, anchor="center")

    # Bau logo insertion (right image)
    image_height = int(self.screen_height / 8)
    image_width = int(self.screen_height / 8)
    bau_image_path = os.path.join(self.base_dir, "..", "images", "bau_logo.png")
    bau_logo_image = Image.open(bau_image_path)
    bau_logo_image = bau_logo_image.resize(
        (image_height, image_width)
    )  # Optional: ensure it's the right size
    self.bau_logo = ImageTk.PhotoImage(bau_logo_image)

    self.image_label_bau = tk.Label(
        self.frame_banner, image=self.bau_logo, bg=self.banner_color
    )
    self.image_label_bau.image = self.bau_logo
    self.image_label_bau.place(
        relx=1.0,
        rely=0.5,
        x=-int(self.screen_width / 15),
        y=0,
        width=image_width,
        height=image_height,
        anchor="e",
    )

    # Veterinary_teaching_hospital logo insertion (left inage)
    vth_image_path = os.path.join(self.base_dir, "..", "images", "vth_logo.png")
    vth_logo_image = Image.open(vth_image_path)
    vth_logo_image = vth_logo_image.resize((image_height, image_width))
    # self.vth_logo = make_circle_image(vth_image_path,image_height)
    self.vth_logo = ImageTk.PhotoImage(vth_logo_image)

    self.image_label_vth = tk.Label(
        self.frame_banner, image=self.vth_logo, bg=self.banner_color
    )
    self.image_label_vth.image = self.vth_logo
    self.image_label_vth.place(
        relx=0.0,
        rely=0.5,
        x=int(self.screen_width / 15),
        y=0,
        width=image_width,
        height=image_height,
        anchor="w",
    )
