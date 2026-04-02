import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor

class MaFenetrePro(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mon Logiciel Pro v1.0")
        self.setGeometry(100, 100, 450, 350)
        self.setStyleSheet("background-color: #1E1E2E;") # Fond très sombre (style Catppuccin)

        # Widget central (le conteneur)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(40, 40, 40, 40)
        self.layout.setSpacing(15)

        # 1. Titre (Stylisé avec CSS)
        self.label_titre = QLabel("AUTHENTIFICATION")
        self.label_titre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_titre.setStyleSheet("""
            color: #CDD6F4; 
            font-size: 24px; 
            font-weight: bold; 
            margin-bottom: 20px;
        """)
        self.layout.addWidget(self.label_titre)

        # 2. Zone de Saisie (Stylisée)
        self.entree_nom = QLineEdit()
        self.entree_nom.setPlaceholderText("Entrez votre identifiant...")
        self.entree_nom.setStyleSheet("""
            QLineEdit {
                background-color: #313244;
                color: #CDD6F4;
                border: 2px solid #45475A;
                border-radius: 8px;
                padding: 12px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #89B4FA; # Bordure bleue au focus
            }
        """)
        self.layout.addWidget(self.entree_nom)

        # 3. Bouton (Stylisé avec effet hover)
        self.bouton_valider = QPushButton("VALIDER")
        self.bouton_valider.setCursor(Qt.CursorShape.PointingHandCursor)
        self.bouton_valider.setStyleSheet("""
            QPushButton {
                background-color: #89B4FA;
                color: #11111B;
                border-radius: 8px;
                padding: 12px;
                font-size: 14px;
                font-weight: bold;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #B4BEFE; # Plus clair au survol
            }
            QPushButton:pressed {
                background-color: #74C7EC; # Plus sombre au clic
            }
        """)
        self.bouton_valider.clicked.connect(self.action_valider)
        self.layout.addWidget(self.bouton_valider)

        # 4. Message de retour
        self.label_message = QLabel("")
        self.label_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_message.setStyleSheet("color: #A6ADC8; font-size: 14px;")
        self.layout.addWidget(self.label_message)

    def action_valider(self):
        nom = self.entree_nom.text()
        if nom:
            self.label_message.setText(f"Bienvenue, {nom} !")
            self.label_message.setStyleSheet("color: #A6E3A1; font-size: 14px;") # Vert
        else:
            self.label_message.setText("Erreur : Le champ est vide.")
            self.label_message.setStyleSheet("color: #F38BA8; font-size: 14px;") # Rouge

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = MaFenetrePro()
    fenetre.show()
    sys.argv.append("--disable-web-security") # Parfois nécessaire pour les styles
    sys.exit(app.exec())