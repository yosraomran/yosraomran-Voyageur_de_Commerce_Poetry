from models import Ville, Vehicule, Route
from tsp_solver import TSPSolver
from exceptions import ContrainteNonSatisfaiteException, DonneesInvalidesException, CalculErreurException
from utils import calculer_distance

def main():
    try:
        # Définir les villes
        ville1 = Ville(1, 0, 0, 5, (0, 10))
        ville2 = Ville(2, 3, 4, 3, (2, 8))
        ville3 = Ville(3, 6, 8, 7, (5, 15))

        # Vérification des données utilisateur
        if ville1.demande < 0 or ville2.demande < 0 or ville3.demande < 0:
            raise DonneesInvalidesException("La demande d'une ville ne peut pas être négative.")

        villes = [ville1, ville2, ville3]

        # Définir le véhicule
        vehicule = Vehicule(capacite_max=10)

        # Définir les routes
        route1 = Route(ville1, ville2, calculer_distance(ville1, ville2))
        route2 = Route(ville2, ville3, calculer_distance(ville2, ville3))
        route3 = Route(ville1, ville3, calculer_distance(ville1, ville3))
        routes = [route1, route2, route3]

        # Créer le solveur TSP
        solver = TSPSolver(villes=villes, vehicule=vehicule, routes=routes)

        # Résoudre le problème
        chemin, distance_totale = solver.resoudre()

        # Afficher les résultats
        print("Chemin trouvé :")
        for ville in chemin:
            print(f"Ville ID: {ville.id}, Demande: {ville.demande}")

        print(f"Distance totale : {distance_totale:.2f}")

    except ContrainteNonSatisfaiteException as e:
        print(f"Erreur de contrainte : {e}")

    except DonneesInvalidesException as e:
        print(f"Erreur de données : {e}")

    except CalculErreurException as e:
        print(f"Erreur de calcul : {e}")

    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

if __name__ == "__main__":
    main()
