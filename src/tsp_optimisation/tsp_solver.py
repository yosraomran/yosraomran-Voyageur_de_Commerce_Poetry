from typing import List
from models import Ville, Vehicule, Route
from constraints import verifier_contraintes
from utils import calculer_distance
from exceptions import ContrainteNonSatisfaiteException, CalculErreurException

class TSPSolver:
    def __init__(self, villes: List[Ville], vehicule: Vehicule, routes: List[Route]):
        self.villes = villes
        self.vehicule = vehicule
        self.routes = routes

    def resoudre(self):
        chemin = []
        distance_totale = 0
        ville_actuelle = self.villes[0]  # Départ de la première ville

        try:
            while len(chemin) < len(self.villes):
                prochaine_ville = min(
                    [v for v in self.villes if v not in chemin],
                    key=lambda v: calculer_distance(ville_actuelle, v)
                )
                verifier_contraintes(prochaine_ville, self.vehicule, chemin)
                chemin.append(prochaine_ville)
                distance_totale += calculer_distance(ville_actuelle, prochaine_ville)
                ville_actuelle = prochaine_ville
        except ContrainteNonSatisfaiteException as e:
            print(f"Erreur de contrainte : {str(e)}")
        except CalculErreurException as e:
            print(f"Erreur de calcul : {str(e)}")
        except Exception as e:
            print(f"Erreur inattendue : {str(e)}")
        
        return chemin, distance_totale
