import tkinter as tk

import solo_mode_easy
import solo_mode_hard
import solo_mode_normal

import multi_mode_basic

exit_picture = None

def difficulty_solo():
    global exit_picture

    def exit_windows():
        windows_difficulty.destroy()

    def open_easy():
        solo_mode_easy.random_word_easy()

    def open_normal():
        solo_mode_normal.random_word_normal()

    def open_hard():
        solo_mode_hard.random_word_hard()

    windows_difficulty = tk.Toplevel()
    windows_difficulty.config(bg="#FEFEE0")
    windows_difficulty.attributes('-fullscreen', True)

    exit_picture = tk.PhotoImage(file="image/croix.png")

    # boucle pour l'affichage de tout les pendu
    for i in range(12):
        for j in range(13):
            small_text = tk.Label(windows_difficulty, text="Pendu", fg="black", bg="#FEFEE0", font=("inconsolata", 10),pady=25, padx=38)
            small_text.grid(row=i, column=j)

    global_frame = tk.Frame(windows_difficulty, relief="raised", bg="#FEFEE0", borderwidth=10)
    global_frame.grid(row=3, column=4, columnspan=5, rowspan=6)

    big_text = tk.Label(global_frame, text="DIFFICULTÉ", font=("inconsolata", 42), bg="#FEFEE0", fg="black")
    big_text.grid(row=2, column=3, columnspan=5, rowspan=2)

    cache = tk.Frame(global_frame, bg="#FEFEE0", height=10, width=20, borderwidth=5)
    cache.grid(row=4, column=3, columnspan=5, rowspan=4, ipadx=70, ipady=10)

    btn_easy = tk.Button(cache,  text="Facile", width=9, relief="raised", borderwidth=10, font=("inconsolata", 20), bg="black", fg="#FEFEE0", command=open_easy)
    btn_easy.pack()
    btn_normal = tk.Button(cache, text="Normal", width=9, relief="raised", borderwidth=10, font=("inconsolata", 20), bg="black", fg="#FEFEE0", command=open_normal)
    btn_normal.pack()
    btn_hard = tk.Button(cache, text="Difficile", width=9, relief="raised", borderwidth=10, font=("inconsolata", 20), bg="black", fg="#FEFEE0", command=open_hard)
    btn_hard.pack()

    btn_exit = tk.Button(cache, image=exit_picture, relief="raised", borderwidth=10, bg="red", command=exit_windows)
    btn_exit.pack()

def dificulty_multi():
    global exit_picture

    def exit_windows():
        windows_difficulty.destroy()

    def basic():
        multi_mode_basic.basic_mode()

    def duel():
        print("cc")

    windows_difficulty = tk.Toplevel()
    windows_difficulty.config(bg="#FEFEE0")
    windows_difficulty.attributes('-fullscreen', True)

    exit_picture = tk.PhotoImage(file="image/croix.png")

    # boucle pour l'affichage de tout les pendu
    for i in range(12):
        for j in range(13):
            small_text = tk.Label(windows_difficulty, text="Pendu", fg="black", bg="#FEFEE0", font=("inconsolata", 10),pady=25, padx=38)
            small_text.grid(row=i, column=j)

    global_frame = tk.Frame(windows_difficulty, relief="raised", bg="#FEFEE0", borderwidth=10)
    global_frame.grid(row=3, column=4, columnspan=5, rowspan=6)

    big_text = tk.Label(global_frame, text="MODE-DE-JEU", font=("inconsolata", 42), bg="#FEFEE0", fg="black")
    big_text.grid(row=2, column=3, columnspan=5, rowspan=2)

    cache = tk.Frame(global_frame, bg="#FEFEE0", height=10, width=20, borderwidth=5)
    cache.grid(row=4, column=3, columnspan=5, rowspan=4, ipadx=70, ipady=10)

    btn_basic = tk.Button(cache,  text="Basique", width=9, relief="raised", borderwidth=10, font=("inconsolata", 20), bg="black", fg="#FEFEE0", command=basic)
    btn_basic.pack()
    btn_duel = tk.Button(cache, text="Duel", width=9, relief="raised", borderwidth=10, font=("inconsolata", 20), bg="black", fg="#FEFEE0", command=duel)
    btn_duel.pack()

    btn_exit = tk.Button(cache, image=exit_picture, relief="raised", borderwidth=10, bg="red", command=exit_windows)
    btn_exit.pack()