"""
Module contenant les composants d'ajout de données pour l'application Coupe du Monde.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class AddDataDialog(tk.Toplevel):
    """Dialogue de base pour l'ajout de données."""
    
    def __init__(self, parent, title, add_callback=None):
        super().__init__(parent)
        self.parent = parent
        self.add_callback = add_callback
        
        # Configurer la fenêtre
        self.title(title)
        self.geometry("500x400")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        
        # Créer les widgets
        self.create_widgets()
        
        # Centrer la fenêtre
        self.center_window()
    
    def create_widgets(self):
        """Crée les widgets du dialogue."""
        # Frame principal
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame pour les champs
        self.fields_frame = ttk.Frame(main_frame)
        self.fields_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Frame pour les boutons
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Bouton Ajouter
        add_btn = ttk.Button(buttons_frame, text="Ajouter", command=self.on_add)
        add_btn.pack(side=tk.RIGHT, padx=5)
        
        # Bouton Annuler
        cancel_btn = ttk.Button(buttons_frame, text="Annuler", command=self.destroy)
        cancel_btn.pack(side=tk.RIGHT, padx=5)
    
    def add_entry_field(self, label_text, row, required=False):
        """Ajoute un champ de saisie."""
        # Label
        label = ttk.Label(self.fields_frame, text=label_text)
        label.grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
        
        if required:
            req_label = ttk.Label(self.fields_frame, text="*", foreground="red")
            req_label.grid(row=row, column=1, sticky=tk.W)
        
        # Champ de saisie
        entry = ttk.Entry(self.fields_frame, width=30)
        entry.grid(row=row, column=2, sticky=tk.W, padx=5, pady=5)
        
        return entry
    
    def add_combobox_field(self, label_text, row, values, required=False):
        """Ajoute un champ avec liste déroulante."""
        # Label
        label = ttk.Label(self.fields_frame, text=label_text)
        label.grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
        
        if required:
            req_label = ttk.Label(self.fields_frame, text="*", foreground="red")
            req_label.grid(row=row, column=1, sticky=tk.W)
        
        # Liste déroulante
        combo = ttk.Combobox(self.fields_frame, values=values, width=28)
        combo.grid(row=row, column=2, sticky=tk.W, padx=5, pady=5)
        
        return combo
    
    def add_checkbox_field(self, label_text, row):
        """Ajoute un champ à cocher."""
        # Variable
        var = tk.BooleanVar()
        
        # Case à cocher
        check = ttk.Checkbutton(self.fields_frame, text=label_text, variable=var)
        check.grid(row=row, column=0, columnspan=3, sticky=tk.W, padx=5, pady=5)
        
        return var
    
    def add_spinbox_field(self, label_text, row, from_val, to_val, required=False):
        """Ajoute un champ numérique."""
        # Label
        label = ttk.Label(self.fields_frame, text=label_text)
        label.grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
        
        if required:
            req_label = ttk.Label(self.fields_frame, text="*", foreground="red")
            req_label.grid(row=row, column=1, sticky=tk.W)
        
        # Spinbox
        spinbox = ttk.Spinbox(self.fields_frame, from_=from_val, to=to_val, width=10)
        spinbox.grid(row=row, column=2, sticky=tk.W, padx=5, pady=5)
        
        return spinbox
    
    def add_date_field(self, label_text, row, required=False):
        """Ajoute un champ de date."""
        # Label
        label = ttk.Label(self.fields_frame, text=label_text)
        label.grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
        
        if required:
            req_label = ttk.Label(self.fields_frame, text="*", foreground="red")
            req_label.grid(row=row, column=1, sticky=tk.W)
        
        # Frame pour la date
        date_frame = ttk.Frame(self.fields_frame)
        date_frame.grid(row=row, column=2, sticky=tk.W, padx=5, pady=5)
        
        # Jour
        day_spinbox = ttk.Spinbox(date_frame, from_=1, to=31, width=3)
        day_spinbox.pack(side=tk.LEFT, padx=2)
        
        # Mois
        month_spinbox = ttk.Spinbox(date_frame, from_=1, to=12, width=3)
        month_spinbox.pack(side=tk.LEFT, padx=2)
        
        # Année
        year_spinbox = ttk.Spinbox(date_frame, from_=1900, to=2100, width=5)
        year_spinbox.pack(side=tk.LEFT, padx=2)
        
        # Définir l'année courante
        year_spinbox.set(datetime.now().year)
        
        return (day_spinbox, month_spinbox, year_spinbox)
    
    def get_date_value(self, date_field):
        """Récupère la valeur d'un champ de date."""
        day, month, year = date_field
        try:
            day_val = int(day.get())
            month_val = int(month.get())
            year_val = int(year.get())
            return f"{year_val}-{month_val:02d}-{day_val:02d}"
        except ValueError:
            return None
    
    def on_add(self):
        """Gère l'événement d'ajout."""
        # À implémenter dans les classes enfants
        pass
    
    def center_window(self):
        """Centre la fenêtre par rapport à la fenêtre parente."""
        self.update_idletasks()
        
        # Calculer la position
        parent_x = self.parent.winfo_rootx()
        parent_y = self.parent.winfo_rooty()
        parent_width = self.parent.winfo_width()
        parent_height = self.parent.winfo_height()
        
        width = self.winfo_width()
        height = self.winfo_height()
        
        x = parent_x + (parent_width - width) // 2
        y = parent_y + (parent_height - height) // 2
        
        # Positionner la fenêtre
        self.geometry(f"+{x}+{y}")

class AddCoupeDialog(AddDataDialog):
    """Dialogue pour l'ajout d'une coupe du monde."""
    
    def create_widgets(self):
        """Crée les widgets du dialogue."""
        super().create_widgets()
        
        # Ajouter les champs spécifiques
        self.annee_field = self.add_spinbox_field("Année", 0, 1900, 2100, True)
        self.date_debut_field = self.add_date_field("Date de début", 1, True)
        self.date_fin_field = self.add_date_field("Date de fin", 2, True)
        self.nb_equipes_field = self.add_spinbox_field("Nombre d'équipes", 3, 1, 100, True)
        self.format_field = self.add_entry_field("Format", 4, True)
        self.slogan_field = self.add_entry_field("Slogan", 5)
        
        # Ajouter un label pour les champs obligatoires
        ttk.Label(self.fields_frame, text="* Champs obligatoires", foreground="red").grid(
            row=6, column=0, columnspan=3, sticky=tk.W, padx=5, pady=10)
    
    def on_add(self):
        """Gère l'événement d'ajout."""
        # Récupérer les valeurs
        try:
            annee = int(self.annee_field.get())
            date_debut = self.get_date_value(self.date_debut_field)
            date_fin = self.get_date_value(self.date_fin_field)
            nb_equipes = int(self.nb_equipes_field.get())
            format_val = self.format_field.get().strip()
            slogan = self.slogan_field.get().strip()
            
            # Vérifier les champs obligatoires
            if not (annee and date_debut and date_fin and nb_equipes and format_val):
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoires.")
                return
            
            # Créer les données
            data = {
                'annee': annee,
                'date_debut': date_debut,
                'date_fin': date_fin,
                'nb_equipes': nb_equipes,
                'format': format_val,
                'slogan': slogan if slogan else None
            }
            
            # Appeler le callback
            if self.add_callback:
                result = self.add_callback(data)
                if result:
                    messagebox.showinfo("Succès", "Coupe du monde ajoutée avec succès.")
                    self.destroy()
                else:
                    messagebox.showerror("Erreur", "Erreur lors de l'ajout de la coupe du monde.")
        
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

class AddEquipeDialog(AddDataDialog):
    """Dialogue pour l'ajout d'une équipe."""
    
    def create_widgets(self):
        """Crée les widgets du dialogue."""
        super().create_widgets()
        
        # Ajouter les champs spécifiques
        self.pays_field = self.add_entry_field("Pays", 0, True)
        self.confederation_field = self.add_combobox_field("Confédération", 1, 
                                                         ["UEFA", "CONMEBOL", "CONCACAF", "CAF", "AFC", "OFC"], True)
        self.classement_field = self.add_spinbox_field("Classement FIFA", 2, 1, 211, True)
        self.participations_field = self.add_spinbox_field("Nombre de participations", 3, 0, 50, True)
        
        # Ajouter un label pour les champs obligatoires
        ttk.Label(self.fields_frame, text="* Champs obligatoires", foreground="red").grid(
            row=4, column=0, columnspan=3, sticky=tk.W, padx=5, pady=10)
    
    def on_add(self):
        """Gère l'événement d'ajout."""
        # Récupérer les valeurs
        try:
            pays = self.pays_field.get().strip()
            confederation = self.confederation_field.get().strip()
            classement = int(self.classement_field.get())
            participations = int(self.participations_field.get())
            
            # Vérifier les champs obligatoires
            if not (pays and confederation):
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoires.")
                return
            
            # Créer les données
            data = {
                'pays': pays,
                'confederation': confederation,
                'classement_fifa': classement,
                'nb_participations': participations
            }
            
            # Appeler le callback
            if self.add_callback:
                result = self.add_callback(data)
                if result:
                    messagebox.showinfo("Succès", "Équipe ajoutée avec succès.")
                    self.destroy()
                else:
                    messagebox.showerror("Erreur", "Erreur lors de l'ajout de l'équipe.")
        
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

class AddJoueurDialog(AddDataDialog):
    """Dialogue pour l'ajout d'un joueur."""
    
    def create_widgets(self):
        """Crée les widgets du dialogue."""
        super().create_widgets()
        
        # Ajouter les champs spécifiques
        self.nom_field = self.add_entry_field("Nom", 0, True)
        self.prenom_field = self.add_entry_field("Prénom", 1, True)
        self.date_naissance_field = self.add_date_field("Date de naissance", 2, True)
        self.nationalite_field = self.add_entry_field("Nationalité", 3, True)
        self.poste_field = self.add_combobox_field("Poste", 4, 
                                                ["Gardien", "Défenseur", "Milieu", "Attaquant"], True)
        
        # Ajouter un label pour les champs obligatoires
        ttk.Label(self.fields_frame, text="* Champs obligatoires", foreground="red").grid(
            row=5, column=0, columnspan=3, sticky=tk.W, padx=5, pady=10)
    
    def on_add(self):
        """Gère l'événement d'ajout."""
        # Récupérer les valeurs
        try:
            nom = self.nom_field.get().strip()
            prenom = self.prenom_field.get().strip()
            date_naissance = self.get_date_value(self.date_naissance_field)
            nationalite = self.nationalite_field.get().strip()
            poste = self.poste_field.get().strip()
            
            # Vérifier les champs obligatoires
            if not (nom and prenom and date_naissance and nationalite and poste):
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoires.")
                return
            
            # Créer les données
            data = {
                'nom': nom,
                'prenom': prenom,
                'date_naissance': date_naissance,
                'nationalite': nationalite,
                'poste': poste
            }
            
            # Appeler le callback
            if self.add_callback:
                result = self.add_callback(data)
                if result:
                    messagebox.showinfo("Succès", "Joueur ajouté avec succès.")
                    self.destroy()
                else:
                    messagebox.showerror("Erreur", "Erreur lors de l'ajout du joueur.")
        
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

class AddMatchDialog(AddDataDialog):
    """Dialogue pour l'ajout d'un match."""
    
    def __init__(self, parent, title, add_callback=None, controller=None):
        self.controller = controller
        super().__init__(parent, title, add_callback)
    
    def create_widgets(self):
        """Crée les widgets du dialogue."""
        super().create_widgets()
        
        # Récupérer les données pour les listes déroulantes
        coupes = []
        equipes = []
        stades = []
        arbitres = []
        
        if self.controller:
            from models.add_data import AddDataModel
            
            coupes_data = AddDataModel.get_all_coupes()
            if coupes_data:
                coupes = [f"{c[1]} (ID: {c[0]})" for c in coupes_data]
            
            equipes_data = AddDataModel.get_all_equipes()
            if equipes_data:
                equipes = [f"{e[1]} (ID: {e[0]})" for e in equipes_data]
            
            stades_data = AddDataModel.get_all_stades()
            if stades_data:
                stades = [f"{s[1]}, {s[2]}, {s[3]} (ID: {s[0]})" for s in stades_data]
            
            arbitres_data = AddDataModel.get_all_arbitres()
            if arbitres_data:
                arbitres = [f"{a[1]} {a[2]} ({a[3]}) (ID: {a[0]})" for a in arbitres_data]
        
        # Ajouter les champs spécifiques
        self.coupe_field = self.add_combobox_field("Coupe du Monde", 0, coupes, True)
        self.date_field = self.add_date_field("Date", 1, True)
        self.heure_field = self.add_entry_field("Heure (HH:MM)", 2, True)
        self.equipe1_field = self.add_combobox_field("Équipe 1", 3, equipes, True)
        self.equipe2_field = self.add_combobox_field("Équipe 2", 4, equipes, True)
        self.stade_field = self.add_combobox_field("Stade", 5, stades, True)
        self.arbitre_field = self.add_combobox_field("Arbitre principal", 6, arbitres, True)
        self.phase_field = self.add_combobox_field("Phase", 7, 
                                                ["Groupe", "Huitième de finale", "Quart de finale", 
                                                 "Demi-finale", "Match pour la 3e place", "Finale"], True)
        
        # Résultat
        ttk.Label(self.fields_frame, text="Résultat", font=("Arial", 10, "bold")).grid(
            row=8, column=0, columnspan=3, sticky=tk.W, padx=5, pady=5)
        
        # Score
        score_frame = ttk.Frame(self.fields_frame)
        score_frame.grid(row=9, column=0, columnspan=3, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(score_frame, text="Score:").pack(side=tk.LEFT, padx=5)
        self.score1_field = ttk.Spinbox(score_frame, from_=0, to=20, width=3)
        self.score1_field.pack(side=tk.LEFT, padx=2)
        
        ttk.Label(score_frame, text="-").pack(side=tk.LEFT, padx=2)
        self.score2_field = ttk.Spinbox(score_frame, from_=0, to=20, width=3)
        self.score2_field.pack(side=tk.LEFT, padx=2)
        
        # Score mi-temps
        mi_temps_frame = ttk.Frame(self.fields_frame)
        mi_temps_frame.grid(row=10, column=0, columnspan=3, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(mi_temps_frame, text="Score mi-temps:").pack(side=tk.LEFT, padx=5)
        self.mi_temps1_field = ttk.Spinbox(mi_temps_frame, from_=0, to=20, width=3)
        self.mi_temps1_field.pack(side=tk.LEFT, padx=2)
        
        ttk.Label(mi_temps_frame, text="-").pack(side=tk.LEFT, padx=2)
        self.mi_temps2_field = ttk.Spinbox(mi_temps_frame, from_=0, to=20, width=3)
        self.mi_temps2_field.pack(side=tk.LEFT, padx=2)
        
        # Prolongation et tirs au but
        self.prolongation_var = self.add_checkbox_field("Prolongation", 11)
        self.tirs_au_but_var = self.add_checkbox_field("Tirs au but", 12)
        
        # Score tirs au but
        tab_frame = ttk.Frame(self.fields_frame)
        tab_frame.grid(row=13, column=0, columnspan=3, sticky=tk.W, padx=5, pady=5)
        
        ttk.Label(tab_frame, text="Score tirs au but:").pack(side=tk.LEFT, padx=5)
        self.tab1_field = ttk.Spinbox(tab_frame, from_=0, to=20, width=3)
        self.tab1_field.pack(side=tk.LEFT, padx=2)
        
        ttk.Label(tab_frame, text="-").pack(side=tk.LEFT, padx=2)
        self.tab2_field = ttk.Spinbox(tab_frame, from_=0, to=20, width=3)
        self.tab2_field.pack(side=tk.LEFT, padx=2)
        
        # Ajouter un label pour les champs obligatoires
        ttk.Label(self.fields_frame, text="* Champs obligatoires", foreground="red").grid(
            row=14, column=0, columnspan=3, sticky=tk.W, padx=5, pady=10)
    
    def on_add(self):
        """Gère l'événement d'ajout."""
        # Récupérer les valeurs
        try:
            # Extraire les IDs des valeurs sélectionnées
            coupe_str = self.coupe_field.get()
            equipe1_str = self.equipe1_field.get()
            equipe2_str = self.equipe2_field.get()
            stade_str = self.stade_field.get()
            arbitre_str = self.arbitre_field.get()
            
            # Extraire les IDs
            import re
            
            id_coupe = int(re.search(r'ID: (\d+)', coupe_str).group(1)) if coupe_str else None
            id_equipe1 = int(re.search(r'ID: (\d+)', equipe1_str).group(1)) if equipe1_str else None
            id_equipe2 = int(re.search(r'ID: (\d+)', equipe2_str).group(1)) if equipe2_str else None
            id_stade = int(re.search(r'ID: (\d+)', stade_str).group(1)) if stade_str else None
            id_arbitre = int(re.search(r'ID: (\d+)', arbitre_str).group(1)) if arbitre_str else None
            
            # Autres valeurs
            date = self.get_date_value(self.date_field)
            heure = self.heure_field.get().strip()
            phase = self.phase_field.get().strip()
            
            # Scores
            score1 = int(self.score1_field.get())
            score2 = int(self.score2_field.get())
            mi_temps1 = int(self.mi_temps1_field.get())
            mi_temps2 = int(self.mi_temps2_field.get())
            
            # Options
            prolongation = self.prolongation_var.get()
            tirs_au_but = self.tirs_au_but_var.get()
            
            # Scores tirs au but
            tab1 = int(self.tab1_field.get()) if tirs_au_but else None
            tab2 = int(self.tab2_field.get()) if tirs_au_but else None
            
            # Vérifier les champs obligatoires
            if not (id_coupe and date and heure and id_equipe1 and id_equipe2 and id_stade and id_arbitre and phase):
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoires.")
                return
            
            # Vérifier que les équipes sont différentes
            if id_equipe1 == id_equipe2:
                messagebox.showerror("Erreur", "Les deux équipes doivent être différentes.")
                return
            
            # Créer les données
            data = {
                'id_coupe': id_coupe,
                'date': date,
                'heure': heure,
                'id_equipe1': id_equipe1,
                'id_equipe2': id_equipe2,
                'id_stade': id_stade,
                'id_arbitre_principal': id_arbitre,
                'phase_competition': phase,
                'score_equipe1': score1,
                'score_equipe2': score2,
                'score_mi_temps_equipe1': mi_temps1,
                'score_mi_temps_equipe2': mi_temps2,
                'prolongation': prolongation,
                'tirs_au_but': tirs_au_but,
                'score_tirs_au_but_equipe1': tab1,
                'score_tirs_au_but_equipe2': tab2
            }
            
            # Appeler le callback
            if self.add_callback:
                result = self.add_callback(data)
                if result:
                    messagebox.showinfo("Succès", "Match ajouté avec succès.")
                    self.destroy()
                else:
                    messagebox.showerror("Erreur", "Erreur lors de l'ajout du match.")
        
        except (ValueError, AttributeError) as e:
            messagebox.showerror("Erreur", f"Veuillez entrer des valeurs valides. {str(e)}")
