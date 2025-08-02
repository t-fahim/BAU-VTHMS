# view_data.py
import tkinter as tk
from tkinter import ttk
import psycopg2
from psycopg2 import Error

def connect_db():
    """Establishes a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            user="your_username",     # Replace with your PostgreSQL username
            password="your_password", # Replace with your PostgreSQL password
            host="127.0.0.1",
            port="5432",
            database="vth_database"
        )
        return conn
    except Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def view_all_patient_data():
    """Creates a new window to display all patient data from the database."""
    view_window = tk.Toplevel()
    view_window.title("All Patient Data")
    view_window.geometry("1200x600") # Adjust size as needed

    tree_frame = tk.Frame(view_window)
    tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    tree_scroll_y = ttk.Scrollbar(tree_frame, orient="vertical")
    tree_scroll_y.pack(side="right", fill="y")

    tree_scroll_x = ttk.Scrollbar(tree_frame, orient="horizontal")
    tree_scroll_x.pack(side="bottom", fill="x")

    tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)
    tree.pack(fill=tk.BOTH, expand=True)

    tree_scroll_y.config(command=tree.yview)
    tree_scroll_x.config(command=tree.xview)

    conn = None
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM patients ORDER BY owner_name ASC")
            records = cursor.fetchall()

            if records:
                # Get column names from cursor description
                column_names = [desc[0] for desc in cursor.description]
                tree["columns"] = column_names
                tree["show"] = "headings"

                for col in column_names:
                    tree.heading(col, text=col.replace('_', ' ').title())
                    tree.column(col, width=100, anchor="w") # Set a default width

                for row in records:
                    tree.insert("", tk.END, values=row)
            else:
                tk.Label(view_window, text="No patient data found.", font=("Arial", 14)).pack(pady=20)

    except Error as e:
        tk.messagebox.showerror("Database Error", f"Error retrieving data: {e}")
        print(f"Error retrieving data: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
