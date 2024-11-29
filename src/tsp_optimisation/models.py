from typing import Tuple
from exceptions import DonneesInvalidesException

class Ville:
    def __init__(self, id: int, x: float, y: float, demande: int, fenetre_temporelle: Tuple[int, int]):
        if demande < 0:
            raise DonneesInvalidesException(f"Demande invalide pour la ville {id}: {demande}.")
        if fenetre_temporelle[0] > fenetre_temporelle[1]:
            raise DonneesInvalidesException(f"Fenêtre temporelle invalide pour la ville {id}: {fenetre_temporelle}.")
        self.id = id
        self.x = x
        self.y = y
        self.demande = demande
        self.fenetre_temporelle = fenetre_temporelle

class Vehicule:
    def __init__(self, capacite_max: int):
        if capacite_max <= 0:
            raise DonneesInvalidesException(f"Capacité maximale invalide: {capacite_max}.")
        self.capacite_max = capacite_max
        self.charge_actuelle = 0

class Route:
    def __init__(self, ville1: Ville, ville2: Ville, distance: float):
        if distance < 0:
            raise DonneesInvalidesException("La distance entre deux villes doit être positive.")
        self.ville1 = ville1
        self.ville2 = ville2
        self.distance = distance
