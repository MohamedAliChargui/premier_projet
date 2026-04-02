import customtkinter as ctk

# Configuration globale
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Python Cyber Dashboard v1.0")
        self.geometry("700x450")

        # Configuration de la grille principale (2 colonnes, 1 ligne)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- 1. BARRE LATÉRALE (NAVIGATION) ---
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="PRO-APP", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text="Statistiques", command=self.sidebar_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Thème:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 20))

        # --- 2. ZONE PRINCIPALE (CONTENU) ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.label_main = ctk.CTkLabel(self.main_frame, text="Bienvenue sur votre espace de travail", font=ctk.CTkFont(size=22))
        self.label_main.pack(pady=20)

        # Une barre de progression pour faire "Pro"
        self.progressbar = ctk.CTkProgressBar(self.main_frame, width=300)
        self.progressbar.pack(pady=10)
        self.progressbar.set(0.6) # Remplie à 60%

        # Zone d'entrée stylée
        self.entry = ctk.CTkEntry(self.main_frame, placeholder_text="Tapez une commande...", width=300, height=40)
        self.entry.pack(pady=20)

        # Bouton d'action avec effet de couleur
        self.main_button = ctk.CTkButton(self.main_frame, text="EXÉCUTER", fg_color="#2ecc71", hover_color="#27ae60", width=150)
        self.main_button.pack(pady=10)

    def sidebar_event(self):
        print("Bouton latéral cliqué")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()