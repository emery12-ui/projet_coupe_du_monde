"""
Module contenant les fonctionnalités d'ajout de données pour l'application Coupe du Monde.
"""

from models.database import DatabaseConnection

class AddDataModel:
    """Modèle pour les fonctionnalités d'ajout de données."""
    
    @staticmethod
    def add_coupe(data):
        """Ajoute une nouvelle coupe du monde."""
        query = """
            INSERT INTO coupe_du_monde (annee, date_debut, date_fin, nb_equipes, format, slogan)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id_coupe
        """
        params = (
            data.get('annee'),
            data.get('date_debut'),
            data.get('date_fin'),
            data.get('nb_equipes'),
            data.get('format'),
            data.get('slogan')
        )
        
        return DatabaseConnection.execute_query(query, params, fetchone=True, commit=True)
    
    @staticmethod
    def add_equipe(data):
        """Ajoute une nouvelle équipe."""
        query = """
            INSERT INTO equipe (pays, confederation, classement_fifa, nb_participations)
            VALUES (%s, %s, %s, %s)
            RETURNING id_equipe
        """
        params = (
            data.get('pays'),
            data.get('confederation'),
            data.get('classement_fifa'),
            data.get('nb_participations')
        )
        
        return DatabaseConnection.execute_query(query, params, fetchone=True, commit=True)
    
    @staticmethod
    def add_joueur(data):
        """Ajoute un nouveau joueur."""
        query = """
            INSERT INTO joueur (nom, prenom, date_naissance, nationalite, poste)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id_joueur
        """
        params = (
            data.get('nom'),
            data.get('prenom'),
            data.get('date_naissance'),
            data.get('nationalite'),
            data.get('poste')
        )
        
        return DatabaseConnection.execute_query(query, params, fetchone=True, commit=True)
    
    @staticmethod
    def add_stade(data):
        """Ajoute un nouveau stade."""
        query = """
            INSERT INTO stade (nom, ville, pays, capacite)
            VALUES (%s, %s, %s, %s)
            RETURNING id_stade
        """
        params = (
            data.get('nom'),
            data.get('ville'),
            data.get('pays'),
            data.get('capacite')
        )
        
        return DatabaseConnection.execute_query(query, params, fetchone=True, commit=True)
    
    @staticmethod
    def add_arbitre(data):
        """Ajoute un nouvel arbitre."""
        query = """
            INSERT INTO arbitre (nom, prenom, nationalite)
            VALUES (%s, %s, %s)
            RETURNING id_arbitre
        """
        params = (
            data.get('nom'),
            data.get('prenom'),
            data.get('nationalite')
        )
        
        return DatabaseConnection.execute_query(query, params, fetchone=True, commit=True)
    
    @staticmethod
    def add_match(data):
        """Ajoute un nouveau match."""
        # Insérer le match
        query_match = """
            INSERT INTO match (id_coupe, date, heure, id_equipe1, id_equipe2, id_stade, id_arbitre_principal, phase_competition)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id_match
        """
        params_match = (
            data.get('id_coupe'),
            data.get('date'),
            data.get('heure'),
            data.get('id_equipe1'),
            data.get('id_equipe2'),
            data.get('id_stade'),
            data.get('id_arbitre_principal'),
            data.get('phase_competition')
        )
        
        id_match = DatabaseConnection.execute_query(query_match, params_match, fetchone=True, commit=True)
        
        if id_match:
            # Insérer le résultat du match
            query_resultat = """
                INSERT INTO resultat_match (id_match, score_equipe1, score_equipe2, score_mi_temps_equipe1, score_mi_temps_equipe2,
                                           prolongation, tirs_au_but, score_tirs_au_but_equipe1, score_tirs_au_but_equipe2)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            params_resultat = (
                id_match[0],
                data.get('score_equipe1'),
                data.get('score_equipe2'),
                data.get('score_mi_temps_equipe1'),
                data.get('score_mi_temps_equipe2'),
                data.get('prolongation', False),
                data.get('tirs_au_but', False),
                data.get('score_tirs_au_but_equipe1'),
                data.get('score_tirs_au_but_equipe2')
            )
            
            DatabaseConnection.execute_query(query_resultat, params_resultat, commit=True)
        
        return id_match
    
    @staticmethod
    def add_joueur_match(data):
        """Ajoute un joueur à un match."""
        query = """
            INSERT INTO participation_joueur_match (id_match, id_joueur, titulaire, minute_entree, minute_sortie, buts, passes_decisives)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            data.get('id_match'),
            data.get('id_joueur'),
            data.get('titulaire'),
            data.get('minute_entree'),
            data.get('minute_sortie'),
            data.get('buts'),
            data.get('passes_decisives')
        )
        
        return DatabaseConnection.execute_query(query, params, commit=True)
    
    @staticmethod
    def add_sanction(data):
        """Ajoute une sanction à un joueur dans un match."""
        query = """
            INSERT INTO sanction (id_match, id_joueur, type, minute, raison)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id_sanction
        """
        params = (
            data.get('id_match'),
            data.get('id_joueur'),
            data.get('type'),
            data.get('minute'),
            data.get('raison')
        )
        
        return DatabaseConnection.execute_query(query, params, fetchone=True, commit=True)
    
    @staticmethod
    def get_all_equipes():
        """Récupère toutes les équipes pour les listes déroulantes."""
        return DatabaseConnection.execute_query(
            "SELECT id_equipe, pays FROM equipe ORDER BY pays",
            fetchall=True
        )
    
    @staticmethod
    def get_all_stades():
        """Récupère tous les stades pour les listes déroulantes."""
        return DatabaseConnection.execute_query(
            "SELECT id_stade, nom, ville, pays FROM stade ORDER BY nom",
            fetchall=True
        )
    
    @staticmethod
    def get_all_arbitres():
        """Récupère tous les arbitres pour les listes déroulantes."""
        return DatabaseConnection.execute_query(
            "SELECT id_arbitre, nom, prenom, nationalite FROM arbitre ORDER BY nom, prenom",
            fetchall=True
        )
    
    @staticmethod
    def get_all_coupes():
        """Récupère toutes les coupes du monde pour les listes déroulantes."""
        return DatabaseConnection.execute_query(
            "SELECT id_coupe, annee FROM coupe_du_monde ORDER BY annee",
            fetchall=True
        )
    
    @staticmethod
    def get_all_joueurs():
        """Récupère tous les joueurs pour les listes déroulantes."""
        return DatabaseConnection.execute_query(
            "SELECT id_joueur, nom, prenom, nationalite FROM joueur ORDER BY nom, prenom",
            fetchall=True
        )
