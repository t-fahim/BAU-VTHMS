# main.py
import os
import tkinter as tk
from tkinter import messagebox # Import messagebox for showing alerts
from banner import create_banner
from menu_bar import create_menu
from information import information_frame
from footer import create_footer
from PIL import Image, ImageTk
from database_ops import insert_patient_data # Import the function
from view_data import view_all_patient_data # Import the new function

class Home_window:
    def __init__(self, root):
        # Variables
        self.banner_color = "#0C0950"
        self.background_color = "#FBE4D6"
        self.menubar_color = "#CA7842"
        # Get the folder where the script is located
        self.base_dir = os.path.dirname(__file__)

        #input variable - these will be set in information_frame
        self.sex_var = tk.StringVar()
        self.pregnancy_var = tk.StringVar()


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
        # Pass self to create_menu so it can access instance methods like view_all_patient_data
        create_menu(self)

        # Creating information frame using information_frame in information module
        information_frame(self) # This will now also create the save button

        # Creating footer frame using creat_footer in footer module
        create_footer(self)

    def save_data_to_db(self):
        """Retrieves data from the form and saves it to the database."""
        try:
            owner_name = self.entry_name.get()
            phone_number = self.entry_phone.get()
            address = self.text_address.get("1.0", tk.END).strip()
            tag_no = self.entry_tag.get()
            species = self.entry_species.get()
            breed = self.entry_breed.get()

            # Handle potential conversion errors for numerical fields
            try:
                milk_yield = float(self.entry_milk_yield.get()) if self.entry_milk_yield.get() else None
            except ValueError:
                milk_yield = None

            try:
                age = int(self.entry_age.get()) if self.entry_age.get() else None
            except ValueError:
                age = None

            try:
                body_weight = float(self.entry_weight.get()) if self.entry_weight.get() else None
            except ValueError:
                body_weight = None

            sex = self.sex_var.get()
            pregnancy_str = self.pregnancy_var.get()
            pregnancy = True if pregnancy_str == "yes" else False

            try:
                pregnancy_month = int(self.entry_pregnancy_month.get()) if self.entry_pregnancy_month.get() and pregnancy else None
            except ValueError:
                pregnancy_month = None

            try:
                total_animals = int(self.entry_total_animal.get()) if self.entry_total_animal.get() else None
            except ValueError:
                total_animals = None

            date_of_parturition = self.entry_dateof_parturition.get()
            date_of_oestrus = self.entry_dateof_oestrus.get()
            parity = self.entry_parity.get()
            duration_of_illness = self.entry_durationof_illness.get()
            owner_complaints = self.text_complaints.get("1.0", tk.END).strip()
            disease_history = self.text_disease_history.get("1.0", tk.END).strip()
            treatment_history = self.text_treatment_history.get("1.0", tk.END).strip()
            management_history = self.text_management_history.get("1.0", tk.END).strip()


            data = (
                owner_name, phone_number, address, tag_no, species, breed,
                milk_yield, age, body_weight, sex, pregnancy, pregnancy_month,
                total_animals, date_of_parturition, date_of_oestrus, parity,
                duration_of_illness, owner_complaints, disease_history,
                treatment_history, management_history
            )

            if insert_patient_data(data):
                messagebox.showinfo("Success", "Patient data saved successfully!")
                self.clear_form() # Clear form after successful save
            else:
                messagebox.showerror("Error", "Failed to save patient data. Check console for details.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            print(f"An error occurred while saving data: {e}")

    def clear_form(self):
        """Clears all input fields in the form."""
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.text_address.delete("1.0", tk.END)
        self.entry_tag.delete(0, tk.END)
        self.entry_species.delete(0, tk.END)
        self.entry_breed.delete(0, tk.END)
        self.entry_milk_yield.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_weight.delete(0, tk.END)
        self.sex_var.set("male") # Reset radio button
        self.pregnancy_var.set("no") # Reset radio button
        self.entry_pregnancy_month.config(state=tk.DISABLED)
        self.entry_pregnancy_month.delete(0, tk.END)
        self.entry_total_animal.delete(0, tk.END)
        self.entry_dateof_parturition.delete(0, tk.END)
        self.entry_dateof_oestrus.delete(0, tk.END)
        self.entry_parity.delete(0, tk.END)
        self.entry_durationof_illness.delete(0, tk.END)
        self.text_complaints.delete("1.0", tk.END)
        self.text_disease_history.delete("1.0", tk.END)
        self.text_treatment_history.delete("1.0", tk.END)
        self.text_management_history.delete("1.0", tk.END)


# Creating home window.
window = tk.Tk()
home_window = Home_window(window)
window.mainloop()
