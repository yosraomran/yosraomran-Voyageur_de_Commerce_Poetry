import math
from models import Ville
from exceptions import CalculErreurException

def calculer_distance(ville1: Ville, ville2: Ville) -> float:
    try:
        return math.sqrt((ville1.x - ville2.x) ** 2 + (ville1.y - ville2.y) ** 2)
    except Exception as e:
        raise CalculErreurException(
            f"Erreur de calcul de la distance entre les villes {ville1.id} et {ville2.id}: {str(e)}"
        )
