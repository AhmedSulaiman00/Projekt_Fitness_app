import customtkinter as ctk
import mysql.connector
from tkinter import messagebox
from tkinter import Toplevel, Label

# Funktion zum Schließen der App
def close_app():
    root.destroy()

# Funktion zum Erstellen eines neuen Benutzers
def create_user():
    vorname = entry_vorname.get().capitalize()
    nachname = entry_nachname.get().capitalize()
    geburtsdatum = entry_geburtsdatum.get()

    benutzername = f"{vorname} {nachname}"

    if benutzername and geburtsdatum:
        try:
            # Verbindung zur Datenbank herstellen
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="fitlife_workout_app"
            )
            
            if mydb.is_connected():
                cursor = mydb.cursor()
                
                # SQL-INSERT-Befehl zum Hinzufügen eines neuen Benutzers
                sql = "INSERT INTO benutzer (Vorname, Nachname, Geburtsdatum) VALUES (%s, %s, %s)"
                values = (vorname, nachname, geburtsdatum)
                cursor.execute(sql, values)
                
                # Änderungen speichern
                mydb.commit()
                
                # Erfolgreiche Erstellung
                messagebox.showinfo("Erfolg", f"Benutzer '{benutzername}' wurde erfolgreich erstellt!")
                
        except mysql.connector.Error as err:
            messagebox.showerror("Fehler", f"Fehler beim Speichern in der Datenbank: {err}")
        
        finally:
            cursor.close()
            mydb.close()
    else:
        messagebox.showerror("Fehler", "Bitte füllen Sie alle Felder aus.")

# Funktion, um den Tooltip anzuzeigen
def show_tooltip(event):
    global tooltip
    tooltip = Toplevel(root)
    tooltip.overrideredirect(True)
    tooltip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
    label = Label(tooltip, text="Format: YYYY-MM-DD", bg="#f7f7f7", relief="solid", borderwidth=1)
    label.pack()

# Funktion, um den Tooltip zu verstecken
def hide_tooltip(event):
    if tooltip:
        tooltip.destroy()

# Hauptfenster erstellen
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Benutzer erstellen")
root.geometry("400x400")

# Rahmen (Frame) hinzufügen
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Stil für Überschrift (Title)
title_label = ctk.CTkLabel(master=frame, text="Neuen Benutzer erstellen", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

# Eingabefelder für Vorname und Nachname
entry_vorname = ctk.CTkEntry(master=frame, placeholder_text="Vorname", width=180)
entry_vorname.pack(pady=10)

entry_nachname = ctk.CTkEntry(master=frame, placeholder_text="Nachname", width=180)
entry_nachname.pack(pady=10)

# Geburtsdatum-Eingabefeld und "i" im Kreis
geburtsdatum_frame = ctk.CTkFrame(master=frame)
geburtsdatum_frame.pack(pady=10)

# Zentrierung von Geburtsdatum-Eingabefeld und Info-Symbol
entry_geburtsdatum = ctk.CTkEntry(master=geburtsdatum_frame, placeholder_text="Geburtsdatum", width=170)
entry_geburtsdatum.pack(side="left", padx=(0, 5))

# Info-Symbol (i im Kreis)
info_label = ctk.CTkLabel(master=geburtsdatum_frame, text="ⓘ", font=("Arial", 14))
info_label.pack(side="left")

# Event-Bindungen für Tooltip
info_label.bind("<Enter>", show_tooltip)
info_label.bind("<Leave>", hide_tooltip)

# Custom Buttons
create_button = ctk.CTkButton(master=frame, text="Benutzer erstellen", command=create_user)
create_button.pack(pady=10)

close_button = ctk.CTkButton(master=frame, text="Beenden", fg_color="red", command=close_app)
close_button.pack(pady=10)

# Tkinter-Loop starten
root.mainloop()
