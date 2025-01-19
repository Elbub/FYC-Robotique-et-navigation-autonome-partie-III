from typing import List, Dict
from api import Platform, Route, get_platform_id, get_routes, get_platforms_data
from datetime import datetime


def get_optimal_route(departure_station: str
                      , arrival_station: str
                      , departure_time: datetime
                      , arrival_maximal_time: datetime
                     ):
    
    ### Initialisation des quais et des trajets
    
    # Récupérer les quais et les trajets.
    platforms: Dict[int, "Platform"] = get_platforms_data()
    routes: List[Route] = get_routes()
    # Récupérer les ID de départ et d'arrivée plutôt que les noms.
    id_departure_platform = get_platform_id(departure_station, platforms)
    id_arrival_platform = get_platform_id(arrival_station, platforms)
    # Fixer la distance du point de départ à 0 et celle de tous les autres à ∞ (datetime max parmi les données).
    for platform in platforms.values():
        platform.minimal_arrival_time = arrival_maximal_time
    platforms[id_departure_platform].minimal_arrival_time = departure_time
    # Relier les arrêtes (trajets) à leur noeud d'origine (quai de départ).
    for route in routes:
        platforms[route.id_departure_platform].routes.append(route)
    
    
    ### Parcours du graphe
    

    # Noter les noeuds non traités.
    unchecked_platforms: set[int] = set(platforms.keys())

    # Tant que nous ne sommes pas au point d'arrivée :
    while (True):
        # Prendre un point encore non traité dont l'heure d'arrivée est la plus faible.
        current_platform = Platform(-1, arrival_maximal_time)
        for id_platform in unchecked_platforms:
            if current_platform.minimal_arrival_time > platforms[id_platform].minimal_arrival_time:
                current_platform = platforms[id_platform]
        # Vérifier les conditions d'arrêt (arrivée atteinte ou plus de trajet disponible).
        if current_platform == platforms[id_arrival_platform]:
            break
        if (current_platform.id_platform == -1):
            return ["Aucun trajet disponible."]
        else:
            unchecked_platforms.remove(current_platform.id_platform)
        if (not unchecked_platforms):
            return ["Aucun trajet disponible."]
        # Mettre à jour l'heure d'arrivée de ses voisins non traités (heure de départ du quai courant + durée du trajet)
        # et se définir comme leur parent, si elle est plus faible.
        # Attention :
        # - Deux type de trajets à prendre en compte : les trajets en train et les jonctions à pied.
        # - On ne peut pas prendre un train qui est déjà parti.
        for route in current_platform.routes :
            if (not route.id_arrival_platform in unchecked_platforms):
                continue
            if (route.is_on_foot):
                if (platforms[route.id_arrival_platform].minimal_arrival_time > current_platform.minimal_arrival_time + route.on_foot_travel_time):
                    platforms[route.id_arrival_platform].minimal_arrival_time = current_platform.minimal_arrival_time + route.on_foot_travel_time
                    platforms[route.id_arrival_platform].parent = current_platform
            elif (
                route.departure_time >= current_platform.minimal_arrival_time
                and platforms[route.id_arrival_platform].minimal_arrival_time > route.arrival_time
                ):
                platforms[route.id_arrival_platform].minimal_arrival_time = route.arrival_time
                platforms[route.id_arrival_platform].parent = current_platform
    
    # Récupérer le trajet global sous forme d'une liste (gares et lignes).
    # Pour plus de lisibilité, voici un format type : f"{platform.station_name} - Ligne {platform.line}"
    optimal_route = [f"{current_platform.station_name} - Ligne {current_platform.line} - {current_platform.minimal_arrival_time}"]
    while (current_platform.id_platform != id_departure_platform):
        current_platform = current_platform.parent
        optimal_route.append(f"{current_platform.station_name} - Ligne {current_platform.line} - {current_platform.minimal_arrival_time}")
    optimal_route.reverse()
    
    # Fin de l'algorithme
    return optimal_route


