import customtkinter as ctk

root = ctk.CTk()
root.geometry("600x600")


frame = ctk.CTkScrollableFrame(root, width=400, height=400, bg_color="blue")
frame.grid()

frame2 = ctk.CTkFrame(frame, width=600, height=800, fg_color="black")
frame2.grid()


root.mainloop()