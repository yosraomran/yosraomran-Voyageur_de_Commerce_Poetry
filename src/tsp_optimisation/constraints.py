from models import Ville, Vehicule
from exceptions import ContrainteNonSatisfaiteException

def verifier_contraintes(ville: Ville, vehicule: Vehicule, chemin: list) -> bool:
    if vehicule.charge_actuelle + ville.demande > vehicule.capacite_max:
        raise ContrainteNonSatisfaiteException(
            f"Le véhicule ne peut pas satisfaire la demande de la ville {ville.id}."
        )

    heure_actuelle = len(chemin)  # Simplification pour l'exemple
    ouverture, fermeture = ville.fenetre_temporelle
    if not (ouverture <= heure_actuelle <= fermeture):
        raise ContrainteNonSatisfaiteException(
            f"La ville {ville.id} ne peut pas être visitée à l'heure {heure_actuelle}."
        )

    return True

