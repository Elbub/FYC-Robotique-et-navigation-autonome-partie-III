from datetime import datetime, timedelta
from path_planning import get_optimal_route
# from path_planning_correction import get_optimal_route


def departure_arrival(departure_location: str, arrival_location: str, departure_time: datetime):
    print(f"_____________ Trajet de {departure_location} à {arrival_location} _____________")
    arrival_time = departure_time + timedelta(hours = 2)
    departure_to_arrival = get_optimal_route(
        departure_location,
        arrival_location,
        departure_time = departure_time,
        arrival_maximal_time = arrival_time
    )
    for station in departure_to_arrival:
        print(f"{station}")


if __name__ == "__main__":
    # Horaires théoriques
    departure_arrival("Poissy", "Beynes", datetime(2024, 8, 7, 17, 00))
    departure_arrival("Trappes", "Beynes", datetime(2024, 8, 7, 18, 00))
    
    # Prévision du retard
    departure_arrival("Poissy", "Beynes", datetime(2024, 8, 7, 18, 00))
    departure_arrival("Trappes", "Beynes", datetime(2024, 8, 7, 19, 00))