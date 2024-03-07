import tkinter as tk
import random

exit_picture = None
def random_word_easy():
    global windows_mod, exit_picture, zero, un, deux,trois, quatre, cinq, six, sept, huit, neuf, dix, sauver, display, random_word, nb_life

    windows_mod = tk.Toplevel()
    windows_mod.config(bg="#FEFEE0")
    windows_mod.attributes('-fullscreen', True)

    exit_picture = tk.PhotoImage(file="image/croix.png")
    zero = tk.PhotoImage(file="image/pendu.png")
    un = tk.PhotoImage(file="image/1.png")
    deux = tk.PhotoImage(file="image/2.png")
    trois = tk.PhotoImage(file="image/3.png")
    quatre = tk.PhotoImage(file="image/4.png")
    cinq = tk.PhotoImage(file="image/5.png")
    six = tk.PhotoImage(file="image/6.png")
    sept = tk.PhotoImage(file="image/7.png")
    huit = tk.PhotoImage(file="image/8.png")
    neuf = tk.PhotoImage(file="image/9.png")
    dix = tk.PhotoImage(file="image/10.png")
    sauver = tk.PhotoImage(file="image/sauver.png")

    nb_life = 10
    v_life = tk.StringVar(value="Vie restante : " + str(nb_life))

    with open("./liste_de_mots_facile.txt", "r", encoding="utf-8") as list:
        complete_list = list.readlines()

    random_word = random.choice(complete_list)
    print(random_word)

    def generer_mot():

        btn_exit.destroy()
        frame_generate.destroy()

        def one_caractere(event):
            if len(enter_letter.get()) >= 1:
                return 'break'

        def suppr_entry(event):
            global nb_life

            letter = enter_letter.get()
            enter_letter.delete(0, tk.END)

            recup_use_letter = pendu_use_letter.cget("text")

            if letter in recup_use_letter:
                nb_life -= 1
                v_life.set("Vie restante : " + str(nb_life))
            else:
                recup_use_letter += letter
                pendu_use_letter.config(text=recup_use_letter)
                enter_letter.delete(0, tk.END)

                if letter in random_word:
                    for i in range(len(random_word)):
                        if random_word[i] == letter:
                            display[i] = letter
                else:
                    nb_life -= 1
                    v_life.set("Vie restante : " + str(nb_life))

            if nb_life < 7 and nb_life > 3:
                look_life.config(fg="orange")
            elif nb_life < 4:
                look_life.config(fg="red")

            if nb_life == 9:
                pendu_picture.config(image=neuf)
            elif nb_life == 8:
                pendu_picture.config(image=huit)
            elif nb_life == 7:
                pendu_picture.config(image=sept)
            elif nb_life == 6:
                pendu_picture.config(image=six)
            elif nb_life == 5:
                pendu_picture.config(image=cinq)
            elif nb_life == 4:
                pendu_picture.config(image=quatre)
            elif nb_life == 3:
                pendu_picture.config(image=trois)
            elif nb_life == 2:
                pendu_picture.config(image=deux)
            elif nb_life == 1:
                pendu_picture.config(image=un)
            elif nb_life == 0:
                pendu_picture.config(image=zero)

            label.config(text=display)

            #défaite
            if nb_life == 0:
                enter_letter.destroy()
                pendu_use_letter.destroy()
                look_life.destroy()
                label.destroy()
                btn_exit_1.destroy()

                display_game_over = tk.Label(windows_mod, text="PENDU", fg="red", bg="#FEFEE0", font=("inconsolata", 50))
                display_game_over.pack()

                label_2 = tk.Label(windows_mod, text=random_word, bg="#FEFEE0", font=("inconsolata", 35))
                label_2.pack()

                look_life_2 = tk.Label(windows_mod, textvariable=v_life, background="#FEFEE0", fg="red",font=("inconsolata", 25))
                look_life_2.pack()

                btn_exit_2 = tk.Button(windows_mod, image=exit_picture, relief="raised", borderwidth=10, bg="red",command=exit_windows)
                btn_exit_2.pack(anchor="center", pady=10)

            #victoire
            if "_" not in display:
                enter_letter.destroy()
                pendu_use_letter.destroy()
                look_life.destroy()
                label.destroy()
                btn_exit_1.destroy()

                pendu_picture.config(image=sauver)

                display_win = tk.Label(windows_mod, text="SAUVER", fg="green", bg="#FEFEE0", font=("inconsolata", 50))
                display_win.pack()

                label_2 = tk.Label(windows_mod, text=display, bg="#FEFEE0", font=("inconsolata", 35))
                label_2.pack()

                look_life_2 = tk.Label(windows_mod, textvariable=v_life, background="#FEFEE0", fg="red",font=("inconsolata", 25))
                look_life_2.pack()

                btn_exit_2 = tk.Button(windows_mod, image=exit_picture, relief="raised", borderwidth=10, bg="red",command=exit_windows)
                btn_exit_2.pack(anchor="center", pady=10)


        def unique_letter(P):
            return P.isalpha() or P == ""


        pendu_picture = tk.Label(windows_mod, bg="#FEFEE0", image=dix)
        pendu_picture.pack(fill="both", expand=True)

        longueur = len(random_word) -1
        display = ["_"] * longueur

        # Créer un label pour afficher le mot généré
        label = tk.Label(windows_mod, text=display, bg="#FEFEE0", font=("inconsolata", 35))
        label.pack()

        entry_var = tk.StringVar()
        enter_letter = tk.Entry(windows_mod,  textvariable=entry_var, width=2, font=("inconsolata", 35), borderwidth=3)
        enter_letter.pack(pady=20, ipady=10)
        enter_letter.bind('<Key>', one_caractere)
        enter_letter.bind('<Return>', suppr_entry)
        validation = windows_mod.register(unique_letter)
        enter_letter.config(validate="key", validatecommand=(validation, "%P"))

        pendu_use_letter = tk.Label(windows_mod, bg="#FEFEE0", font=("inconsolata", 35))
        pendu_use_letter.pack(fill="both", ipady=20)

        look_life = tk.Label(windows_mod, textvariable=v_life, background="#FEFEE0", fg="green",font=("inconsolata", 25))
        look_life.pack()

        btn_exit_1 = tk.Button(windows_mod, image=exit_picture, relief="raised", borderwidth=10, bg="red",command=exit_windows)
        btn_exit_1.pack(anchor="center", pady=10)

    frame_generate = tk.Frame(windows_mod,  background="#FEFEE0")
    frame_generate.pack(fill="both", expand=True)

    # Créer un bouton pour générer un mot aléatoire
    btn_generate = tk.Button(frame_generate, text="Générer le mots",relief="raised", borderwidth=10, font=("inconsolata", 15), bg="black", foreground="green", command=generer_mot)
    btn_generate.pack(anchor="center", pady=60)

    def exit_windows():
        windows_mod.destroy()

    btn_exit = tk.Button(windows_mod, image=exit_picture, relief="raised", borderwidth=10, bg="red", command=exit_windows)
    btn_exit.pack(anchor="center", pady=10)
