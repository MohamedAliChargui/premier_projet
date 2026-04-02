import tkinter as tk
from tkinter import messagebox

def dire_bonjour():
    nom = entree_nom.get()
    if nom:
        label_bienvenue.config(text=f"Salut {nom} !", fg="#00FF00") # Vert fluo
    else:
        messagebox.showwarning("Erreur", "Le champ est vide !")

# Configuration de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Logiciel Pro")
fenetre.geometry("400x300")
fenetre.configure(bg="#2C3E50") # Bleu nuit sombre

# Titre stylisé
tk.Label(fenetre, text="IDENTIFICATION", font=("Arial", 16, "bold"), 
         bg="#2C3E50", fg="white", pady=20).pack()

# Zone de saisie (Entry) avec couleurs sombres
entree_nom = tk.Entry(fenetre, font=("Arial", 14), bg="#34495E", fg="white", 
                      insertbackground="white", borderwidth=0)
entree_nom.pack(pady=10)

# Bouton avec design "Flat"
bouton_valider = tk.Button(fenetre, text="ACCÉDER", command=dire_bonjour, 
                           bg="#E74C3C", fg="white", font=("Arial", 10, "bold"),
                           padx=20, pady=10, activebackground="#C0392B", 
                           activeforeground="white", cursor="hand2")
bouton_valider.pack(pady=20)

# Label pour le résultat
label_bienvenue = tk.Label(fenetre, text="", font=("Arial", 12), bg="#2C3E50", fg="white")
label_bienvenue.pack()

fenetre.mainloop()