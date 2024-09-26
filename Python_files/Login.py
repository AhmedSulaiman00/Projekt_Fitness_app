import customtkinter as ctk
import mysql.connector
from tkinter import messagebox

# Variable zum Speichern der User ID
user_id = None

# Funktion zum Schließen der App
def close_app():
    if messagebox.askokcancel("Beenden", "Möchten Sie die App wirklich schließen?"):
        root.destroy()

# Funktion zum Einloggen eines Benutzers
def login_user():
    global user_id
    vorname = entry_vorname.get().capitalize()
    nachname = entry_nachname.get().capitalize()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="fitlife_workout_app"
    )

    if mydb.is_connected():
        try:
            cursor = mydb.cursor()
            # Abfrage mit Vorname und Nachname
            query = """
                SELECT ID 
                FROM benutzer 
                WHERE Vorname = %s AND Nachname = %s
            """
            values = (vorname, nachname)
            cursor.execute(query, values)
            result = cursor.fetchone()

            if result:
                user_id = result[0]  # Speichere die Benutzer-ID
                messagebox.showinfo("Erfolg", f"Willkommen, {vorname} {nachname}! Ihre Benutzer-ID ist {user_id}.")
            else:
                messagebox.showinfo("Info", "Dieser Benutzername existiert nicht. Bitte erstellen Sie ein Konto.")
        
        except mysql.connector.Error as err:
            messagebox.showerror("Fehler", f"Fehler: {err}")
        
        finally:
            cursor.close()
            mydb.close()
    else:
        messagebox.showerror("Fehler", "Fehler beim Verbinden zur Datenbank.")

# Hauptfenster erstellen
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Benutzer Login")
root.geometry("400x300")

# Rahmen (Frame) hinzufügen
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Stil für Überschrift
title_label = ctk.CTkLabel(master=frame, text="Login", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

# Label und Eingabefelder für Vorname und Nachname
entry_vorname = ctk.CTkEntry(master=frame, placeholder_text="Vorname", width=200)
entry_vorname.pack(pady=10)

entry_nachname = ctk.CTkEntry(master=frame, placeholder_text="Nachname", width=200)
entry_nachname.pack(pady=10)

# Button zum Einloggen
login_button = ctk.CTkButton(master=frame, text="Einloggen", command=login_user)
login_button.pack(pady=10)

# Button zum Schließen der App
close_button = ctk.CTkButton(master=frame, text="Beenden", fg_color="red", command=close_app)
close_button.pack(pady=10)

# Tkinter-Loop starten
root.mainloop()
