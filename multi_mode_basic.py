import tkinter as tk
import random

def basic_mode():
    global nb_life

    windows_basic_mode = tk.Tk()
    windows_basic_mode.config(bg="#FEFEE0")
    windows_basic_mode.attributes('-fullscreen', True)

    nb_life = 10
    v_life = tk.StringVar(value="Vie restante : " + str(nb_life))
    print(v_life)

    def suppr_entry_1(event):
        if name_player_1.get() == "Entrez votre pseudo":
            name_player_1.delete(0, tk.END)

    def suppr_entry_2(event):
        if name_player_2.get() == "Entrez votre pseudo":
            name_player_2.delete(0, tk.END)


    def replace_entry_1(event):
        global name_player_1_label, pseudo_1
        text_pseudo_1 = name_player_1.get()
        name_player_1.destroy()
        pseudo_1 = text_pseudo_1

        name_player_1_label = tk.Label(frame_name_player_1, bg="#FEFEE0", font=("inconsolata", 20), text=text_pseudo_1)
        name_player_1_label.pack(side="right")

    def replace_entry_2(event):
        global name_player_2_label, pseudo_2
        text_pseudo_2 = name_player_2.get()
        pseudo_2 = text_pseudo_2
        name_player_2.destroy()

        name_player_2_label = tk.Label(frame_name_player_2, bg="#FEFEE0", font=("inconsolata", 20), text=text_pseudo_2)
        name_player_2_label.pack(side="right")

    def start_game():
        global player_choice_word

        def suppr_entry_word(event):

            if player_choice_word.get() == "Choissisez votre mot":
                player_choice_word.delete(0, tk.END)

        def transform_word(event):
            global transform_player_choice_word

            def one_caractere(event):
                if len(enter_letter.get()) >= 1:
                    return 'break'

            def unique_letter(P):
                return P.isalpha() or P == ""

            def suppr_entry(event):

                enter_letter.delete(0, tk.END)


            btn_exit_2.destroy()

            pendu_picture = tk.Label(windows_basic_mode, bg="#FEFEE0")
            pendu_picture.pack()

            transform_player_choice_word = player_choice_word.get()
            print(transform_player_choice_word)

            longueur = len(transform_player_choice_word)
            display = ["_"] * longueur

            label = tk.Label(windows_basic_mode, text=display, bg="#FEFEE0", font=("inconsolata", 35))
            label.pack(pady=50)

            entry_var = tk.StringVar()
            enter_letter = tk.Entry(windows_basic_mode, textvariable=entry_var, width=2, font=("inconsolata", 35),borderwidth=3)
            enter_letter.pack(pady=20, ipady=10)
            enter_letter.bind('<Key>', one_caractere)
            enter_letter.bind('<Return>', suppr_entry)
            validation = windows_basic_mode.register(unique_letter)
            enter_letter.config(validate="key", validatecommand=(validation, "%P"))

            pendu_use_letter = tk.Label(windows_basic_mode, bg="#FEFEE0", font=("inconsolata", 35))
            pendu_use_letter.pack(fill="both", ipady=20)

            look_life = tk.Label(windows_basic_mode, text="bonjour", background="#FEFEE0", fg="green",font=("inconsolata", 25))
            look_life.pack()

            frame_player_choice_word.destroy()

            btn_exit_3 = tk.Button(windows_basic_mode, relief="raised", borderwidth=10, bg="red", command=exit_windows)
            btn_exit_3.pack()

        frame_name_player_1.destroy()
        frame_name_player_2.destroy()
        btn_random_player.destroy()
        btn_exit.destroy()

        two_pseudo = [pseudo_1, pseudo_2]
        choice_pseudo_random = random.choice(two_pseudo)

        label_random_player = tk.Label(windows_basic_mode, bg="#FEFEE0", font=("inconsolata", 20))
        label_random_player.pack(pady=50)

        label_random_player.config(text="Le joueur choisi est : " + str(choice_pseudo_random))

        frame_player_choice_word = tk.Frame(windows_basic_mode, bg="#FEFEE0")
        frame_player_choice_word.pack()

        player_choice_word = tk.Entry(frame_player_choice_word, font=("inconsolata", 20), borderwidth=3)
        player_choice_word.insert(0, "Choissisez votre mot")
        player_choice_word.bind("<FocusIn>", suppr_entry_word)
        player_choice_word.bind("<Return>", transform_word)
        player_choice_word.pack(pady=50)

        btn_exit_2 = tk.Button(windows_basic_mode, text="x", relief="raised", borderwidth=10, bg="red", command=exit_windows)
        btn_exit_2.pack()

    def exit_windows():
        windows_basic_mode.destroy()

    frame_name_player_1 = tk.Frame(windows_basic_mode, bg="#FEFEE0")
    frame_name_player_1.pack(pady=40)
    player_1 = tk.Label(frame_name_player_1, text="Joueur 1 :", font=("inconsolata", 20), bg="#FEFEE0")
    player_1.pack(side="left")
    name_player_1 = tk.Entry(frame_name_player_1, width=20, font=("inconsolata", 20), borderwidth=3)
    name_player_1.insert(0, "Entrez votre pseudo")
    name_player_1.bind("<FocusIn>", suppr_entry_1)
    name_player_1.bind("<Return>", replace_entry_1)
    name_player_1.pack(side="right")

    frame_name_player_2 = tk.Frame(windows_basic_mode, bg="#FEFEE0")
    frame_name_player_2.pack( pady=40)
    player_2 = tk.Label(frame_name_player_2, text="Joueur 2 :", font=("inconsolata", 20), bg="#FEFEE0")
    player_2.pack(side="left")
    name_player_2 = tk.Entry(frame_name_player_2, width=20, font=("inconsolata", 20), borderwidth=3)
    name_player_2.insert(0, "Entrez votre pseudo")
    name_player_2.bind("<FocusIn>", suppr_entry_2)
    name_player_2.bind("<Return>", replace_entry_2)
    name_player_2.pack(side="right")

    btn_random_player = tk.Button(windows_basic_mode, text="Lancer le jeu", relief="raised", width=12, borderwidth=10,font=("inconsolata", 20), bg="black", fg="blue", command=start_game)
    btn_random_player.pack(pady=20)

    btn_exit = tk.Button(windows_basic_mode, relief="raised", borderwidth=10, bg="red", command=exit_windows)
    btn_exit.pack()
