"""
Module contenant les vues de base pour l'application Coupe du Monde.
"""

import tkinter as tk
from tkinter import ttk

from views.search_view import CoupeSearchFrame, EquipeSearchFrame, JoueurSearchFrame
from views.add_data_view import AddCoupeDialog, AddEquipeDialog, AddJoueurDialog
from models.add_data import AddDataModel

class BaseView(ttk.Frame):
    """Vue de base dont héritent toutes les autres vues."""
    
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller
        self.create_widgets()
        
    def create_widgets(self):
        """Méthode à implémenter dans les classes enfants."""
        pass
        
    def load_data(self):
        """Méthode à implémenter dans les classes enfants."""
        pass
    
    def create_toolbar(self):
        """Crée une barre d'outils standard."""
        toolbar = ttk.Frame(self)
        toolbar.pack(fill=tk.X, padx=10, pady=10)
        return toolbar

class CoupeView(BaseView):
    """Vue pour la gestion des Coupes du Monde."""
    
    def create_widgets(self):
        """Crée les widgets de la vue."""
        # Frame pour les contrôles
        control_frame = self.create_toolbar()
        
        # Bouton pour rafraîchir les données
        refresh_btn = ttk.Button(control_frame, text="Rafraîchir", command=self.load_data)
        refresh_btn.pack(side=tk.LEFT, padx=5)
        
        # Bouton pour ajouter une coupe
        add_btn = ttk.Button(control_frame, text="Ajouter une coupe", command=self.on_add_coupe)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        # Ajouter le cadre de recherche
        self.search_frame = CoupeSearchFrame(self, self.on_search)
        self.search_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Treeview pour afficher les données
        columns = ("id", "annee", "date_debut", "date_fin", "nb_equipes", "format", "slogan")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        
        # Définir les en-têtes de colonnes
        self.tree.heading("id", text="ID")
        self.tree.heading("annee", text="Année")
        self.tree.heading("date_debut", text="Date de début")
        self.tree.heading("date_fin", text="Date de fin")
        self.tree.heading("nb_equipes", text="Nb équipes")
        self.tree.heading("format", text="Format")
        self.tree.heading("slogan", text="Slogan")
        
        # Définir la largeur des colonnes
        self.tree.column("id", width=50)
        self.tree.column("annee", width=80)
        self.tree.column("date_debut", width=100)
        self.tree.column("date_fin", width=100)
        self.tree.column("nb_equipes", width=80)
        self.tree.column("format", width=200)
        self.tree.column("slogan", width=200)
        
        # Ajouter une scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Placer le treeview et la scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def load_data(self):
        """Charge les données depuis le contrôleur."""
        # Effacer les données existantes
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Récupérer les données via le contrôleur
        if self.controller:
            coupes = self.controller.get_coupes()
            
            # Ajouter les données au treeview
            if coupes:
                for coupe in coupes:
                    self.tree.insert("", tk.END, values=coupe)
    
    def on_search(self, criteria):
        """Gère l'événement de recherche."""
        # Effacer les données existantes
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Récupérer les données via le contrôleur
        if self.controller:
            if criteria:
                coupes = self.controller.search_coupes(criteria)
            else:
                coupes = self.controller.get_coupes()
            
            # Ajouter les données au treeview
            if coupes:
                for coupe in coupes:
                    self.tree.insert("", tk.END, values=coupe)
    
    def on_add_coupe(self):
        """Gère l'événement d'ajout d'une coupe."""
        dialog = AddCoupeDialog(self, "Ajouter une coupe du monde", self.add_coupe)
        self.wait_window(dialog)
    
    def add_coupe(self, data):
        """Ajoute une coupe du monde."""
        result = AddDataModel.add_coupe(data)
        if result:
            self.load_data()
            return True
        return False

class EquipeView(BaseView):
    """Vue pour la gestion des équipes."""
    
    def create_widgets(self):
        """Crée les widgets de la vue."""
        # Frame pour les contrôles
        control_frame = self.create_toolbar()
        
        # Bouton pour rafraîchir les données
        refresh_btn = ttk.Button(control_frame, text="Rafraîchir", command=self.load_data)
        refresh_btn.pack(side=tk.LEFT, padx=5)
        
        # Bouton pour ajouter une équipe
        add_btn = ttk.Button(control_frame, text="Ajouter une équipe", command=self.on_add_equipe)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        # Ajouter le cadre de recherche
        self.search_frame = EquipeSearchFrame(self, self.on_search)
        self.search_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Treeview pour afficher les données
        columns = ("id", "pays", "confederation", "classement_fifa", "nb_participations")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        
        # Définir les en-têtes de colonnes
        self.tree.heading("id", text="ID")
        self.tree.heading("pays", text="Pays")
        self.tree.heading("confederation", text="Confédération")
        self.tree.heading("classement_fifa", text="Classement FIFA")
        self.tree.heading("nb_participations", text="Nb participations")
        
        # Définir la largeur des colonnes
        self.tree.column("id", width=50)
        self.tree.column("pays", width=150)
        self.tree.column("confederation", width=100)
        self.tree.column("classement_fifa", width=100)
        self.tree.column("nb_participations", width=100)
        
        # Ajouter une scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Placer le treeview et la scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def load_data(self):
        """Charge les données depuis le contrôleur."""
        # Effacer les données existantes
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Récupérer les données via le contrôleur
        if self.controller:
            equipes = self.controller.get_equipes()
            
            # Ajouter les données au treeview
            if equipes:
                for equipe in equipes:
                    self.tree.insert("", tk.END, values=equipe)
    
    def on_search(self, criteria):
        """Gère l'événement de recherche."""
        # Effacer les données existantes
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Récupérer les données via le contrôleur
        if self.controller:
            if criteria:
                equipes = self.controller.search_equipes(criteria)
            else:
                equipes = self.controller.get_equipes()
            
            # Ajouter les données au treeview
            if equipes:
                for equipe in equipes:
                    self.tree.insert("", tk.END, values=equipe)
    
    def on_add_equipe(self):
        """Gère l'événement d'ajout d'une équipe."""
        dialog = AddEquipeDialog(self, "Ajouter une équipe", self.add_equipe)
        self.wait_window(dialog)
    
    def add_equipe(self, data):
        """Ajoute une équipe."""
        result = AddDataModel.add_equipe(data)
        if result:
            self.load_data()
            return True
        return False

class JoueurView(BaseView):
    """Vue pour la gestion des joueurs."""
    
    def create_widgets(self):
        """Crée les widgets de la vue."""
        # Frame pour les contrôles
        control_frame = self.create_toolbar()
        
        # Bouton pour rafraîchir les données
        refresh_btn = ttk.Button(control_frame, text="Rafraîchir", command=self.load_data)
        refresh_btn.pack(side=tk.LEFT, padx=5)
        
        # Bouton pour ajouter un joueur
        add_btn = ttk.Button(control_frame, text="Ajouter un joueur", command=self.on_add_joueur)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        # Ajouter le cadre de recherche
        self.search_frame = JoueurSearchFrame(self, self.on_search)
        self.search_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Treeview pour afficher les données
        columns = ("id", "nom", "prenom", "date_naissance", "nationalite", "poste")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        
        # Définir les en-têtes de colonnes
        self.tree.heading("id", text="ID")
        self.tree.heading("nom", text="Nom")
        self.tree.heading("prenom", text="Prénom")
        self.tree.heading("date_naissance", text="Date de naissance")
        self.tree.heading("nationalite", text="Nationalité")
        self.tree.heading("poste", text="Poste")
        
        # Définir la largeur des colonnes
        self.tree.column("id", width=50)
        self.tree.column("nom", width=150)
        self.tree.column("prenom", width=150)
        self.tree.column("date_naissance", width=100)
        self.tree.column("nationalite", width=100)
        self.tree.column("poste", width=100)
        
        # Ajouter une scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Placer le treeview et la scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def load_data(self):
        """Charge les données depuis le contrôleur."""
        # Effacer les données existantes
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Récupérer les données via le contrôleur
        if self.controller:
            joueurs = self.controller.get_joueurs()
            
            # Ajouter les données au treeview
            if joueurs:
                for joueur in joueurs:
                    self.tree.insert("", tk.END, values=joueur)
    
    def on_search(self, criteria):
        """Gère l'événement de recherche."""
        # Effacer les données existantes
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Récupérer les données via le contrôleur
        if self.controller:
            if criteria:
                joueurs = self.controller.search_joueurs(criteria)
            else:
                joueurs = self.controller.get_joueurs()
            
            # Ajouter les données au treeview
            if joueurs:
                for joueur in joueurs:
                    self.tree.insert("", tk.END, values=joueur)
    
    def on_add_joueur(self):
        """Gère l'événement d'ajout d'un joueur."""
        dialog = AddJoueurDialog(self, "Ajouter un joueur", self.add_joueur)
        self.wait_window(dialog)
    
    def add_joueur(self, data):
        """Ajoute un joueur."""
        result = AddDataModel.add_joueur(data)
        if result:
            self.load_data()
            return True
        return False
