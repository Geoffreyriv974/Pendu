import tkinter as tk

exit_picture = None

def rules():
    global exit_picture

    windows_rules = tk.Toplevel()
    windows_rules.config(bg="#FEFEE0")
    windows_rules.attributes('-fullscreen', True)

    #importation es images
    exit_picture = tk.PhotoImage(file="image/croix.png")


    def exit_windows():
        windows_rules.destroy()

    btn_exit = tk.Button(windows_rules, image=exit_picture, relief="raised", borderwidth=10, bg="red", command=exit_windows)
    btn_exit.place(x=700, y=700)