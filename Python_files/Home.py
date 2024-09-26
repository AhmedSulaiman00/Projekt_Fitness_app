import customtkinter as ctk
import subprocess  # Falls du externe Skripte ausführen willst

# Funktion zum Ausführen externer Python-Skripte
def open_create_user_script():
    subprocess.run(["python", "Create_User.py"])

def open_login_script():
    subprocess.run(["python", "Login.py"])

# Hauptfenster für die Home-Seite erstellen
ctk.set_appearance_mode("dark")  # Dark Mode
ctk.set_default_color_theme("blue")  # Blaues Farbschema

root = ctk.CTk()
root.title("Home Page")
root.geometry("400x400")

# Rahmen für das Layout
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Titel der Home-Seite
title_label = ctk.CTkLabel(master=frame, text="FitLife Gym App", font=("Helvetica", 18, "bold"))
title_label.pack(pady=20)

# Button für Benutzererstellung (externes Skript)
create_user_script_button = ctk.CTkButton(master=frame, text="Create User", command=open_create_user_script, fg_color="#e74c3c")
create_user_script_button.pack(pady=10)

# Button für Login (externes Skript)
login_script_button = ctk.CTkButton(master=frame, text="Login", command=open_login_script, fg_color="#f39c12")
login_script_button.pack(pady=10)

# Tkinter-Loop starten
root.mainloop()
