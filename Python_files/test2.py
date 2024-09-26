import customtkinter as ctk
import calendar
import datetime
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#global variables
liste_uebung = []
liste_set = [] 

#functions
def create_uebung():
    liste_uebung.append(ctk.CTkFrame(master=frame2, width = 320, fg_color = '#D9D9D9', border_width = 2, border_color = '#000'))
    reihe = liste_uebung.index(liste_uebung[-1])
    liste_uebung[reihe].grid(row = reihe, column = 0, pady = 10, padx = 27.5)
    liste_uebung[reihe].columnconfigure(0, weight = 1)
    liste_uebung[reihe].columnconfigure(1, weight = 1)
    liste_uebung[reihe].columnconfigure(2, weight = 1)
    liste_uebung[reihe].rowconfigure(0, weight = 1)
    liste_uebung[reihe].rowconfigure(1, weight = 1)
    liste_uebung[reihe].rowconfigure(2, weight = 1)


def create_set():
    ...

#window
root = ctk.CTk(fg_color = '#706262')
root.geometry("398x822")

#define grid
root.rowconfigure(0)
root.rowconfigure(1, minsize = 600)
root.rowconfigure(2)
root.columnconfigure(0, weight = 1)

#frames
frame1 = ctk.CTkFrame(master = root, height = 120, fg_color = 'transparent')
frame1.grid(row = 0, column = 0,sticky = 'ew', padx = 10, pady = (10, 0))
frame1.columnconfigure(0, weight = 1)
frame1.columnconfigure(1, weight = 1)
frame1.columnconfigure(2, weight = 1)

frame2 = ctk.CTkScrollableFrame(master = root, height = 580, corner_radius = 20, fg_color = '#ECDEDE')
frame2.grid(row = 1, column = 0, sticky = 'nsew', padx = 10, pady = (10, 0))
frame2.columnconfigure(0, weight = 1)

buttonframe = ctk.CTkFrame(master = root, height = 56, fg_color = 'transparent')
buttonframe.grid(row = 2, column = 0, sticky = 'ew', padx = 10, pady = (10, 0), ipady = 10)
buttonframe.columnconfigure(0, weight = 1)
buttonframe.columnconfigure(1, weight = 1)
buttonframe.rowconfigure(0, weight = 1)
buttonframe.rowconfigure(1, weight = 1)


#buttons
button_workout_add = ctk.CTkButton(master = buttonframe, text = '+  Neue Übung hinzufügen', 
    font = ('helvetica',20), text_color = '#000', fg_color = '#D9D9D9', border_width = 2, border_color = '#000', command = create_uebung)
button_workout_add.grid(row = 0, columnspan = 2, sticky = 'ew', padx = 5)

button1 = ctk.CTkButton(master = buttonframe, text = '<   Abbrechen',
    fg_color = '#000000', font = ('helvetica',20), corner_radius = 20)
button1.grid(row = 1, column = 0, sticky = 'ew', padx = 5)

button2 = ctk.CTkButton(master = buttonframe, text = 'Fertigstellen   >',
    fg_color = '#2C9822', font = ('helvetica',20), corner_radius = 20)
button2.grid(row = 1, column = 1, sticky = 'ew', padx = 5)

#entries
entry_datum_year = ctk.CTkEntry(master = frame1, placeholder_text = 'YYYY',
    height = 36, corner_radius = 20, fg_color = '#ECDEDE', text_color = "#000000")
entry_datum_year.grid(row = 0, column = 0, sticky = 'ew', padx = 5, pady = 3.5)

entry_datum_month = ctk.CTkEntry(master = frame1, placeholder_text = 'MM',
    height = 36, corner_radius = 20, fg_color = '#ECDEDE', text_color = "#000000")
entry_datum_month.grid(row = 0, column = 1, sticky = 'ew', padx = 5, pady = 3.5)

entry_datum_day = ctk.CTkEntry(master = frame1, placeholder_text = 'DD',
    height = 36, corner_radius = 20, fg_color = '#ECDEDE', text_color = "#000000")
entry_datum_day.grid(row = 0, column = 2, sticky = 'ew', padx = 5, pady = 3.5)

entry_uebung_typ = ctk.CTkEntry(master = frame1, height = 36, placeholder_text = "Typ des Workouts", corner_radius = 20, fg_color = '#ECDEDE')
entry_uebung_typ.grid(row = 1,columnspan = 3, sticky = 'ew', padx = 5, pady = 3.5)


#run 
root.mainloop()