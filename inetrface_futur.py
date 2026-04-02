import customtkinter as ctk

# Configuration du thème (C'est ici que la magie opère)
ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Dashboard Moderne")
        self.geometry("400x450")

        # Configuration de la grille
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # 1. Titre avec une police moderne
        self.label = ctk.CTkLabel(self, text="BIENVENUE", font=ctk.CTkFont(size=25, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        # 2. Zone de saisie avec coins arrondis automatiques
        self.entry = ctk.CTkEntry(self, placeholder_text="Nom d'utilisateur", width=250, height=45)
        self.entry.grid(row=1, column=0, padx=20, pady=10)

        # 3. Un switch (interrupteur) stylé
        self.switch = ctk.CTkSwitch(self, text="Mode Expert")
        self.switch.grid(row=2, column=0, padx=20, pady=10)

        # 4. Le bouton principal (avec animation au survol par défaut)
        self.button = ctk.CTkButton(self, text="CONNEXION", command=self.button_event, 
                                    corner_radius=10, height=45, width=200)
        self.button.grid(row=3, column=0, padx=20, pady=20)

    def button_event(self):
        print(f"Connexion de : {self.entry.get()}")
        self.label.configure(text=f"Bonjour, {self.entry.get()} !", text_color="#1f6aa5")

if __name__ == "__main__":
    app = App()
    app.mainloop()