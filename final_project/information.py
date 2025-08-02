# information.py
# from for oners information

import tkinter as tk
from tkinter import messagebox # Import messagebox for showing alerts

def pregnancy_month(self, value):
    selected_option = value
    if selected_option == "no":
        self.entry_pregnancy_month.config(state=tk.DISABLED, fg="gray")
        self.entry_pregnancy_month.delete(0, tk.END) # Clear content when disabled
    else:
        self.entry_pregnancy_month.config(state=tk.NORMAL, fg="black")


# Label frame Oner's information
def information_frame(self):

    font_size = 10
    input_color = "white"
    self.sex_var = tk.StringVar(value="male") # Changed to self.sex_var
    self.pregnancy_var = tk.StringVar(value="no") # Changed to self.pregnancy_var

    # main frame
    self.info_frame = tk.Frame(
        self.root, bg=self.background_color, height=self.screen_unit * 13
    )
    self.info_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True,padx=5, pady=5)

    # Left fram for owner inormation
    self.left_frame = tk.Frame(self.info_frame, bg=self.background_color)
    self.left_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    # Owner's information
    self.owner_labelFrame = tk.LabelFrame(
        self.left_frame,
        bg=self.background_color,
        text="Owner's Information",
        font=("arial", 12, "bold"),
    )
    self.owner_labelFrame.pack(fill=tk.BOTH, expand=True, pady=5, padx=5)

    # Owner Name
    self.name_lable = tk.Label(
        self.owner_labelFrame,
        text="Owner Name:",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.name_lable.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    self.entry_name = tk.Entry(
        self.owner_labelFrame, width=50, bg=input_color, font=("arial", font_size)
    )
    self.entry_name.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    # Phone Number
    self.phone_label = tk.Label(
        self.owner_labelFrame,
        text="Phone Number:",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.phone_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    self.entry_phone = tk.Entry(
        self.owner_labelFrame, width=50, bg=input_color, font=("arial", font_size)
    )
    self.entry_phone.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    # Address
    self.address_label = tk.Label(
        self.owner_labelFrame,
        text="Address:",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.address_label.grid(row=2, column=0, padx=5, pady=5, sticky="nw")
    self.text_address = tk.Text(
        self.owner_labelFrame,
        height=4,
        width=50,
        bg=input_color,
        font=("arial", font_size),
    )
    self.text_address.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

    # Animal's Information
    self.animal_labelFrame = tk.LabelFrame(
        self.left_frame,
        bg=self.background_color,
        text="Animal's Information",
        font=("arial", 12, "bold"),
    )
    self.animal_labelFrame.pack(fill=tk.BOTH, expand=True, pady=5, padx=5)

    # Tag No
    self.tag_label = tk.Label(
        self.animal_labelFrame,
        text="Tag No:",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.tag_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    self.entry_tag = tk.Entry(
        self.animal_labelFrame, width=50, bg=input_color, font=("arial", font_size)
    )
    self.entry_tag.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    # Species
    self.species_label = tk.Label(
        self.animal_labelFrame,
        text="Species:",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.species_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    self.entry_species = tk.Entry(
        self.animal_labelFrame, width=50, bg=input_color, font=("arial", font_size)
    )
    self.entry_species.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    # Breed
    self.breed_label = tk.Label(
        self.animal_labelFrame,
        text="Breed:",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.breed_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    self.entry_breed = tk.Entry(
        self.animal_labelFrame, width=50, bg=input_color, font=("arial", font_size)
    )
    self.entry_breed.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

    # Milk Yield
    self.milk_yield_label = tk.Label(
        self.animal_labelFrame,
        text="Milk Yield (L/day):",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.milk_yield_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    self.entry_milk_yield = tk.Entry(
        self.animal_labelFrame, width=50, bg=input_color, font=("arial", font_size)
    )
    self.entry_milk_yield.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

    # Age
    self.age_label = tk.Label(
        self.animal_labelFrame,
        text="Age (Months):",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.age_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    self.entry_age = tk.Entry(
        self.animal_labelFrame, width=50, bg=input_color, font=("arial", font_size)
    )
    self.entry_age.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

    # Body Weight
    self.weight_label = tk.Label(
        self.animal_labelFrame,
        text="Body Weight (Kg):",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.weight_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
    self.entry_weight = tk.Entry(
        self.animal_labelFrame, width=50, bg=input_color, font=("arial", font_size)
    )
    self.entry_weight.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

    # Sex
    self.sex_label = tk.Label(
        self.animal_labelFrame,
        text="Sex:",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.sex_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
    self.male_radio = tk.Radiobutton(
        self.animal_labelFrame,
        text="Male",
        variable=self.sex_var,
        value="male",
        background=self.background_color,
        font=("arial", font_size),
    )
    self.male_radio.grid(row=6, column=1, padx=5, pady=5, sticky="w")
    self.female_radio = tk.Radiobutton(
        self.animal_labelFrame,
        text="Female",
        variable=self.sex_var,
        value="female",
        background=self.background_color,
        font=("arial", font_size),
    )
    self.female_radio.grid(row=6, column=1, padx=80, pady=5, sticky="w")

    # Pregnancy Status
    self.pregnancy_label = tk.Label(
        self.animal_labelFrame,
        text="Pregnant:",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.pregnancy_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")
    self.pregnancy_yes_radio = tk.Radiobutton(
        self.animal_labelFrame,
        text="Yes",
        variable=self.pregnancy_var,
        value="yes",
        background=self.background_color,
        font=("arial", font_size),
        command=lambda: pregnancy_month(self, "yes"),
    )
    self.pregnancy_yes_radio.grid(row=7, column=1, padx=5, pady=5, sticky="w")
    self.pregnancy_no_radio = tk.Radiobutton(
        self.animal_labelFrame,
        text="No",
        variable=self.pregnancy_var,
        value="no",
        background=self.background_color,
        font=("arial", font_size),
        command=lambda: pregnancy_month(self, "no"),
    )
    self.pregnancy_no_radio.grid(row=7, column=1, padx=60, pady=5, sticky="w")

    # Pregnancy Month
    self.pregnancy_month_label = tk.Label(
        self.animal_labelFrame,
        text="Pregnancy Month:",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.pregnancy_month_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")
    self.entry_pregnancy_month = tk.Entry(
        self.animal_labelFrame, width=50, bg=input_color, font=("arial", font_size)
    )
    self.entry_pregnancy_month.grid(row=8, column=1, padx=5, pady=5, sticky="ew")
    self.entry_pregnancy_month.config(state=tk.DISABLED, fg="gray") # Initially disabled

    # Total Animals
    self.total_animal_label = tk.Label(
        self.animal_labelFrame,
        text="Total Animals:",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.total_animal_label.grid(row=9, column=0, padx=5, pady=5, sticky="w")
    self.entry_total_animal = tk.Entry(
        self.animal_labelFrame, width=50, bg=input_color, font=("arial", font_size)
    )
    self.entry_total_animal.grid(row=9, column=1, padx=5, pady=5, sticky="ew")

    # Date of Parturition
    self.dateof_parturition_label = tk.Label(
        self.animal_labelFrame,
        text="Date of Parturition:",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.dateof_parturition_label.grid(row=10, column=0, padx=5, pady=5, sticky="w")
    self.entry_dateof_parturition = tk.Entry(
        self.animal_labelFrame, width=50, bg=input_color, font=("arial", font_size)
    )
    self.entry_dateof_parturition.grid(row=10, column=1, padx=5, pady=5, sticky="ew")

    # Date of Oestrus
    self.dateof_oestrus_label = tk.Label(
        self.animal_labelFrame,
        text="Date of Oestrus:",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.dateof_oestrus_label.grid(row=11, column=0, padx=5, pady=5, sticky="w")
    self.entry_dateof_oestrus = tk.Entry(
        self.animal_labelFrame, width=50, bg=input_color, font=("arial", font_size)
    )
    self.entry_dateof_oestrus.grid(row=11, column=1, padx=5, pady=5, sticky="ew")

    # Parity
    self.parity_label = tk.Label(
        self.animal_labelFrame,
        text="Parity:",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.parity_label.grid(row=12, column=0, padx=5, pady=5, sticky="w")
    self.entry_parity = tk.Entry(
        self.animal_labelFrame, width=50, bg=input_color, font=("arial", font_size)
    )
    self.entry_parity.grid(row=12, column=1, padx=5, pady=5, sticky="ew")

    # Duration of Illness
    self.durationof_illness_label = tk.Label(
        self.animal_labelFrame,
        text="Duration of Illness:",
        background=self.background_color,
        font=("arial", font_size, "bold"),
    )
    self.durationof_illness_label.grid(row=13, column=0, padx=5, pady=5, sticky="w")
    self.entry_durationof_illness = tk.Entry(
        self.animal_labelFrame, width=50, bg=input_color, font=("arial", font_size)
    )
    self.entry_durationof_illness.grid(row=13, column=1, padx=5, pady=5, sticky="ew")


    # Right Frame for clinical history
    self.right_frame = tk.Frame(self.info_frame, bg=self.background_color)
    self.right_frame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

    # Clinical History
    self.clinical_history_labelFrame = tk.LabelFrame(
        self.right_frame,
        bg=self.background_color,
        text="Clinical History",
        font=("arial", 12, "bold"),
    )
    self.clinical_history_labelFrame.pack(fill=tk.BOTH, expand=True, pady=5, padx=5)

    # Owner Complaints
    self.owner_complaints_labelFrame = tk.LabelFrame(
        self.clinical_history_labelFrame,
        bg=self.background_color,
        text="Owner Complaints",
        font=("arial", 12, "bold"),
    )
    self.owner_complaints_labelFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=5, padx=5)
    self.text_complaints = tk.Text(
        self.owner_complaints_labelFrame,
        height=5,
        width=50,
        font=("arial",font_size, "normal"),
    )
    self.text_complaints.pack(side=tk.TOP, fill=tk.BOTH, expand=True,pady=5, padx=5)

    # Disease History
    self.disease_history_labelFrame = tk.LabelFrame(
        self.clinical_history_labelFrame,
        bg=self.background_color,
        text="Disease History",
        font=("arial",12, "bold"),
    )
    self.disease_history_labelFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True ,pady=5, padx=5)
    self.text_disease_history = tk.Text(
        self.disease_history_labelFrame,
        height=5,
        width=50,
        font=("arial",font_size, "normal"),
    )
    self.text_disease_history.pack(side=tk.TOP, fill=tk.BOTH, expand=True ,pady=5, padx=5)

    # Treatment History
    self.treatment_history_labelFrame = tk.LabelFrame(
        self.clinical_history_labelFrame,
        bg=self.background_color,
        text="Treatment History",
        font=("arial",12, "bold"),
    )
    self.treatment_history_labelFrame.pack(side=tk.TOP, fill=tk.BOTH,expand=True ,pady=5, padx=5)
    self.text_treatment_history = tk.Text(
        self.treatment_history_labelFrame,
        height=5,
        width=50,
        font=("arial",font_size, "normal"),
    )
    self.text_treatment_history.pack(side=tk.TOP, fill=tk.BOTH, expand=True ,pady=5, padx=5)


    self.management_history_labelFrame = tk.LabelFrame(
        self.clinical_history_labelFrame,
        bg=self.background_color,
        text="Management History",
        font=("arial",12, "bold"),
    )
    self.management_history_labelFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True ,pady=5, padx=5)
    self.text_management_history = tk.Text( # Changed variable name to avoid conflict
        self.management_history_labelFrame,
        height=5,
        width=50,
        font=("arial",font_size, "normal"),
    )
    self.text_management_history.pack(side=tk.TOP, fill=tk.BOTH, expand=True ,pady=5, padx=5)


    # Save Button
    self.save_button = tk.Button(
        self.info_frame, # Placed in info_frame
        text="Save Data",
        command=self.save_data_to_db, # Call the save function from Home_window
        font=("Noto Sans", 12, "bold"),
        bg="#4CAF50", # Green color for save
        fg="white",
        relief=tk.RAISED,
        padx=10,
        pady=5
    )
    self.save_button.pack(side=tk.LEFT, pady=10, padx=10, anchor=tk.NW) # Position at bottom left

    # Clear Button
    self.clear_button = tk.Button(
        self.info_frame, # Placed in info_frame
        text="Clear Form",
        command=self.clear_form, # Call the clear function from Home_window
        font=("Noto Sans", 12, "bold"),
        bg="#FF5722", # Orange color for clear
        fg="white",
        relief=tk.RAISED,
        padx=10,
        pady=5
    )
    self.clear_button.pack(side=tk.LEFT, pady=10, padx=10, anchor=tk.NW) # Position next to save
