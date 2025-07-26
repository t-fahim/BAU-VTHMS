# from for oners information

import tkinter as tk


def pregnancy_month(self, value):
    selected_option = value
    if selected_option == "no":
        self.entry_pregnancy_month.config(state=tk.DISABLED, fg="gray")
    else:
        self.entry_pregnancy_month.config(state=tk.NORMAL, fg="black")


# Label frame Oner's information
def information_frame(self):

    font_size = 10
    input_color = "white"
    sex = tk.StringVar(value="male")
    pregnancy = tk.StringVar(value="no")

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
        text="Owner's Information : ",
        font=("arial", 14, "bold"),
    )
    self.owner_labelFrame.pack(
        fill=tk.BOTH,
        expand=True,
        padx=5,pady=5
    )

    # top row
    self.top_frame = tk.Frame(self.owner_labelFrame, bg=self.background_color)
    self.top_frame.pack(fill=tk.X, side=tk.TOP, expand=True,padx=3, pady=2)

    self.label_name = tk.Label(
        self.top_frame,
        bg=self.background_color,
        text="Owner's Name : ",
        font=("arial", font_size, "normal"),
        borderwidth=0
    )
    self.label_name.pack(side=tk.LEFT,)
    self.entry_name = tk.Entry(
        self.top_frame, bg=input_color, font=("arial", font_size, "normal")
    )
    self.entry_name.pack(side=tk.LEFT, fill=tk.X, expand=True,padx=5)

    self.label_phone = tk.Label(
        self.top_frame,
        bg=self.background_color,
        text="Phone Number : ",
        font=("arial", font_size, "normal"),
    )
    self.label_phone.pack(side=tk.LEFT,padx=5)
    self.entry_phone = tk.Entry(
        self.top_frame,
        bg=input_color,
        width=15,
        font=("arial", font_size, "normal"),
    )
    self.entry_phone.pack(side=tk.LEFT)

    # bottom row
    self.bottom_frame = tk.Frame(self.owner_labelFrame, bg=self.background_color)
    self.bottom_frame.pack(fill=tk.X, expand=True, side=tk.TOP,padx=3, pady=3)

    self.label_address = tk.Label(
        self.bottom_frame,
        bg=self.background_color,
        text="Address : ",
        font=("arial", font_size, "normal"),
    )
    self.label_address.pack(side=tk.LEFT)
    self.text_address = tk.Text(
        self.bottom_frame,
        bg=input_color,
        width=50,
        height=2,
        font=("arial", font_size, "normal"),
    )
    self.text_address.pack(fill=tk.BOTH, expand=True)

    # Patient information ---------------------------
    self.patient_labelFrame = tk.LabelFrame(
        self.left_frame,
        bg=self.background_color,
        text="Patient Information : ",
        font=("arial", 14, "bold"),
    )
    self.patient_labelFrame.pack(side=tk.TOP, expand=True, fill=tk.X,pady=5,padx=5)

    self.label_tag = tk.Label(
        self.patient_labelFrame,
        bg=self.background_color,
        text="Tag No. : ",
        font=("arial", font_size, "normal"),
    )
    self.label_tag.grid(row=0, column=0, sticky=tk.E,pady=3)
    self.entry_tag = tk.Entry(
        self.patient_labelFrame,
        bg=input_color,
        # width=25,
        font=("arial", font_size, "normal"),
    )
    self.entry_tag.grid(row=0, column=1, columnspan=3, sticky=tk.EW ,pady=3)

    self.label_species = tk.Label(
        self.patient_labelFrame,
        bg=self.background_color,
        text="Species : ",
        font=("arial", font_size, "normal"),
    )
    self.label_species.grid(row=1, column=0, sticky=tk.E ,pady=3)
    self.entry_species = tk.Entry(
        self.patient_labelFrame,
        bg=input_color,
        width=45,
        font=("arial", font_size, "normal"),
    )
    self.entry_species.grid(row=1, column=1, columnspan=3, sticky=tk.W ,pady=3)

    self.label_breed = tk.Label(
        self.patient_labelFrame,
        bg=self.background_color,
        text="Breed : ",
        font=("arial", font_size, "normal"),
    )
    self.label_breed.grid(row=2, column=0, sticky=tk.E ,pady=3)
    self.entry_breed = tk.Entry(
        self.patient_labelFrame,
        bg=input_color,
        width=45,
        font=("arial", font_size, "normal"),
    )
    self.entry_breed.grid(row=2, column=1, columnspan=3, sticky=tk.W ,pady=3)

    self.label_milk_yield = tk.Label(
        self.patient_labelFrame,
        bg=self.background_color,
        text="Milk yield(L/d) : ",
        font=("arial", font_size, "normal"),
    )
    self.label_milk_yield.grid(row=2, column=4, sticky=tk.E ,pady=3)
    self.entry_milk_yield = tk.Entry(
        self.patient_labelFrame,
        bg=input_color,
        width=5,
        font=("arial", font_size, "normal"),
    )
    self.entry_milk_yield.grid(row=2, column=5, columnspan=1, sticky=tk.W ,pady=3)
    self.label_age = tk.Label(
        self.patient_labelFrame,
        bg=self.background_color,
        text="Age(year) : ",
        font=("arial", font_size, "normal"),
    )
    self.label_age.grid(row=0, column=4, sticky=tk.E ,pady=3)
    self.entry_age = tk.Entry(
        self.patient_labelFrame,
        bg=input_color,
        width=5,
        font=("arial", font_size, "normal"),
    )
    self.entry_age.grid(row=0, column=5, sticky=tk.W ,pady=3)

    self.label_weight = tk.Label(
        self.patient_labelFrame,
        bg=self.background_color,
        text="Body Weight(kg) : ",
        font=("arial", font_size, "normal"),
    )
    self.label_weight.grid(row=1, column=4, sticky=tk.E ,pady=3)
    self.entry_weight = tk.Entry(
        self.patient_labelFrame,
        bg=input_color,
        width=5,
        font=("arial", font_size, "normal"),
    )
    self.entry_weight.grid(row=1, column=5, sticky=tk.W ,pady=3)

    self.label_sex = tk.Label(
        self.patient_labelFrame,
        bg=self.background_color,
        text="Sex : ",
        font=("arial", font_size, "normal"),
    )
    self.label_sex.grid(row=3, column=0, sticky=tk.E ,pady=3)
    self.radio_male = tk.Radiobutton(
        self.patient_labelFrame,
        bg=self.background_color,
        variable=sex,
        value="male",
        text="Male",
        font=("arial", font_size, "normal"),
    )
    self.radio_male.grid(row=3, column=1 ,pady=3)
    self.radio_female = tk.Radiobutton(
        self.patient_labelFrame,
        bg=self.background_color,
        variable=sex,
        value="female",
        text="Female",
        font=("arial", font_size, "normal"),
    )
    self.radio_female.grid(row=3, column=2, sticky=tk.W ,pady=3)

    self.label_pregnancy = tk.Label(
        self.patient_labelFrame,
        bg=self.background_color,
        text="Pregnancy : ",
        font=("arial", font_size, "normal"),
    )
    self.label_pregnancy.grid(row=4, column=0, sticky=tk.E ,pady=3)
    self.radio_pregnant_yes = tk.Radiobutton(
        self.patient_labelFrame,
        bg=self.background_color,
        variable=pregnancy,
        text="YES",
        value="yes",
        command=lambda: pregnancy_month(self, "yes"),
        font=("arial", font_size, "normal"),
    )  # give command for show number of month.
    self.radio_pregnant_yes.grid(row=4, column=1 ,pady=3)
    self.radio_pregnant_no = tk.Radiobutton(
        self.patient_labelFrame,
        bg=self.background_color,
        variable=pregnancy,
        text="NO",
        value="no",
        command=lambda: pregnancy_month(self, "no"),
        font=("arial", font_size, "normal"),
    )
    self.radio_pregnant_no.grid(row=4, column=2, sticky=tk.W ,pady=3)

    self.label_pregnancy_month = tk.Label(
        self.patient_labelFrame,
        bg=self.background_color,
        text="Pregnancy Month : ",
        font=("arial", font_size, "normal"),
    )
    self.label_pregnancy_month.grid(row=4, column=3, sticky=tk.E ,pady=3)

    self.entry_pregnancy_month = tk.Entry(
        self.patient_labelFrame,
        bg=input_color,
        width=10,
        font=("arial", font_size, "normal"),
    )
    self.entry_pregnancy_month.grid(row=4, column=4, sticky=tk.W ,pady=3)

    self.label_total_animal = tk.Label(
        self.patient_labelFrame,
        bg=self.background_color,
        text="Total animals : ",
        font=("arial", font_size, "normal"),
    )
    self.label_total_animal.grid(row=6, column=0, columnspan=1, sticky=tk.E ,pady=3)
    self.entry_total_animal = tk.Entry(
        self.patient_labelFrame,
        bg=input_color,
        width=10,
        font=("arial", font_size, "normal"),
    )
    self.entry_total_animal.grid(row=6, column=1, sticky=tk.W ,pady=3)

    self.label_dateof_parturition = tk.Label(
        self.patient_labelFrame,
        bg=self.background_color,
        text="Date of Partition : ",
        font=("arial", font_size, "normal"),
    )
    self.label_dateof_parturition.grid(row=5, column=0, columnspan=1, sticky=tk.E ,pady=3)
    self.entry_dateof_parturition = tk.Entry(
        self.patient_labelFrame,
        bg=input_color,
        width=10,
        font=("arial", font_size, "normal"),
    )
    self.entry_dateof_parturition.grid(row=5, column=1, columnspan=1, sticky=tk.W ,pady=3)

    self.label_dateof_oestrus = tk.Label(
        self.patient_labelFrame,
        bg=self.background_color,
        text="Date of Oestrus : ",
        font=("arial", font_size, "normal"),
    )
    self.label_dateof_oestrus.grid(row=5, column=3, columnspan=1, sticky=tk.E ,pady=3)
    self.entry_dateof_oestrus = tk.Entry(
        self.patient_labelFrame,
        bg=input_color,
        width=10,
        font=("arial", font_size, "normal"),
    )
    self.entry_dateof_oestrus.grid(row=5, column=4, columnspan=1, sticky=tk.W ,pady=3)

    self.label_parity = tk.Label(
        self.patient_labelFrame,
        bg=self.background_color,
        text="Parity: ",
        font=("arial", font_size, "normal"),
    )
    self.label_parity.grid(row=3, column=3, columnspan=1, sticky=tk.E ,pady=3)
    self.entry_parity = tk.Entry(
        self.patient_labelFrame,
        bg=input_color,
        width=20,
        font=("arial", font_size, "normal"),
    )
    self.entry_parity.grid(row=3, column=4, columnspan=1, sticky=tk.W ,pady=3)

    self.label_durationof_illness = tk.Label(
        self.patient_labelFrame,
        bg=self.background_color,
        text="Duration of illness : ",
        font=("arial", font_size, "normal"),
    )
    self.label_durationof_illness.grid(row=6, column=2, columnspan=2, sticky=tk.E ,pady=3)
    self.entry_durationof_illness = tk.Entry(
        self.patient_labelFrame,
        bg=input_color,
        width=10,
        font=("arial", font_size, "normal"),
    )
    self.entry_durationof_illness.grid(row=6, column=4, columnspan=1, sticky=tk.W ,pady=3)

    self.owner_complaints_labelFrame = tk.LabelFrame(
        self.left_frame,
        bg=self.background_color,
        text="Owner's Complaints : ",
        font=("arial", 14, "bold"),
    )
    self.owner_complaints_labelFrame.pack(side=tk.TOP, fill=tk.X,padx=5,pady=5)
    self.text_complaints = tk.Text(
        self.owner_complaints_labelFrame, height=5, font=("arial", font_size, "normal")
    )
    self.text_complaints.pack(side=tk.TOP, fill=tk.X,padx=5,pady=5)

    # Right fram for clinical History
    self.right_frame = tk.Frame(self.info_frame, bg=self.background_color)
    self.right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, pady=5, padx=5)

    # CLinical hisrory frame
    self.clinical_history_labelFrame = tk.LabelFrame(
        self.right_frame, bg=self.background_color, text="Clinical History", font=("arial", 14, "bold")
    )
    self.clinical_history_labelFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True,pady=0, padx=0)

    self.disease_history_labelFrame = tk.LabelFrame(
        self.clinical_history_labelFrame,
        bg=self.background_color,
        text="Disease History",
        font=("arial", 12, "bold"),
    )
    self.disease_history_labelFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True ,pady=5, padx=5)
    self.text_disease_history = tk.Text(
        self.disease_history_labelFrame,
        height=5,
        width=50,
        font=("arial", font_size, "normal"),
    )
    self.text_disease_history.pack(side=tk.TOP, fill=tk.BOTH, expand=True ,pady=5, padx=5)

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
    self.text_disease_history = tk.Text(
        self.management_history_labelFrame,
        height=5,
        width=50,
        font=("arial",font_size, "normal"),
    )
    self.text_disease_history.pack(side=tk.TOP, fill=tk.BOTH, expand=True ,pady=5, padx=5)
