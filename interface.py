import tkinter as tk
from tkinter import messagebox

def dire_bonjour():
    nom = entree_nom.get() # On récupère le texte écrit dans la case
    if nom:
        messagebox.showinfo("Message", f"Bonjour {nom} ! Bienvenue dans ton premier logiciel.")
    else:
        messagebox.showwarning("Attention", "Tu as oublié de taper ton nom !")

# 1. Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Mon Premier Logiciel")
fenetre.geometry("300x200") # Largeur x Hauteur

# 2. Ajout des éléments (Widgets)
label_instruction = tk.Label(fenetre, text="Entre ton nom ci-dessous :", pady=10)
label_instruction.pack()

entree_nom = tk.Entry(fenetre) # La zone de texte
entree_nom.pack(pady=5)

bouton_valider = tk.Button(fenetre, text="Valider", command=dire_bonjour, bg="lightblue")
bouton_valider.pack(pady=20)

# 3. Lancement de l'interface
fenetre.mainloop()