import tkinter as tk
import rules
import difficulty

windows_menu = tk.Tk()
windows_menu.config(bg="#FEFEE0")
windows_menu.attributes('-fullscreen', True)

#importation des images
rules_picture = tk.PhotoImage(file="image/regles.png")
exit_picture = tk.PhotoImage(file="image/croix.png")

#fonction appeler pour fermer la fenetre
def windows_exit():
    windows_menu.destroy()

#fonction appeler pour accèder au règles
def windows_rules():
    rules.rules()


#fonction appeler pour choisir le mode multijoueur
def windows_difficulty_solo():
    difficulty.difficulty_solo()


def windows_difficulty_multi():
    difficulty.dificulty_multi()

#boucle pour l'affichage de tout les pendu
for i in range(12):
    for j in range(13):
        small_text = tk.Label(windows_menu, text="Pendu", fg="black", bg="#FEFEE0", font=("inconsolata", 10), pady=25, padx=38)
        small_text.grid(row=i, column=j)


global_frame = tk.Frame(windows_menu, relief="raised", bg="#FEFEE0", borderwidth=10)
global_frame.grid(row=3, column=4, columnspan=5, rowspan=6)

big_text = tk.Label(global_frame, text="PENDU", font=("inconsolata", 70), bg="#FEFEE0", fg="black")
big_text.grid(row=2, column=3, columnspan=5, rowspan=2)

cache = tk.Frame(global_frame, bg="#FEFEE0", height=10, width=20, borderwidth=5)
cache.grid(row=4, column=3, columnspan=5, rowspan=4, ipadx=70, ipady=10)
# bouton pour accéder au différent mode.
btn_start_solo = tk.Button(cache, text="Solo", relief="raised", width=9, borderwidth=10, font=("inconsolata", 20), bg="black", fg="#FEFEE0", command=windows_difficulty_solo)
btn_start_solo.pack()
btn_start_multi = tk.Button(cache, text="Multijoueur", relief="raised", width=9, borderwidth=10, font=("inconsolata", 20), bg="black", fg="#FEFEE0", command=windows_difficulty_multi)
btn_start_multi.pack()
btn_rules = tk.Button(cache, image=rules_picture, relief="raised", borderwidth=10, bg="#499C30", command=windows_rules)
btn_rules.pack(side='left')
btn_delete = tk.Button(cache, image=exit_picture, relief="raised", borderwidth=10,bg="red", command=windows_exit)
btn_delete.pack(side="right")

windows_menu.mainloop()