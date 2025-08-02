# database_ops.py
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

def insert_patient_data(data):
    """Inserts patient data into the 'patients' table."""
    conn = None
    try:
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            sql = """
            INSERT INTO patients (
                owner_name, phone_number, address, tag_no, species, breed,
                milk_yield, age, body_weight, sex, pregnancy, pregnancy_month,
                total_animals, date_of_parturition, date_of_oestrus, parity,
                duration_of_illness, owner_complaints, disease_history,
                treatment_history, management_history
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, data)
            conn.commit()
            print("Data inserted successfully!")
            return True
    except Error as e:
        print(f"Error inserting data: {e}")
        if conn:
            conn.rollback() # Rollback in case of error
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()
