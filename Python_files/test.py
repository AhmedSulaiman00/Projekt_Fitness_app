import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x350")

wkExercise_results_dict = {
    "Wiederholungen" : [],
    "Gewicht": [],
    "Schwierigkeit" : []
}

def login():
    wkExercise_results_dict["Wiederholungen"].append(entry1.get())
    wkExercise_results_dict["Gewicht"].append(entry2.get())
    wkExercise_results_dict["Schwierigkeit"].append(entry3.get())

def druck():
    for key in wkExercise_results_dict:
        for i in wkExercise_results_dict[key]:
            print(i)

frame = ctk.CTkScrollableFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

frame3 = ctk.CTkScrollableFrame(master=root)
frame3.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Workout hinzufügen")
label.pack(pady=12)

entryCal = ctk.CTkEntry(master=frame, placeholder_text="Datum")
entryCal.pack(padx=20, pady=7, fill="both")

entrywkTyp = ctk.CTkEntry(master=frame, placeholder_text="Typ des Workouts")
entrywkTyp.pack(padx=20, fill="both", pady=(0,7))

frame2 = ctk.CTkFrame(master=frame, border_width=5)
frame2.pack(fill="both", padx=20, pady=(0,7))


wkÜbungen = []
wkSets = []

def addÜbung():
    wkÜbungen.append(ctk.CTkFrame(master=frame, border_width=5))
    wkÜbungen[-1].pack(fill="both", padx=20, pady=7)


# i=0
# while i < 3:
#     entries.append(ctk.CTkEntry(master=frame))
#     entries[i].pack(pady=(0,7))
#     i +=1

button = ctk.CTkButton(master=frame, text="Neues set hinzufügen", command=login)
button.pack(pady=7, padx=10)

button2 = ctk.CTkButton(master=frame, text="neue Übung hinzufügen", command=addÜbung)
button2.pack(pady=7, padx=10)

root.mainloop()