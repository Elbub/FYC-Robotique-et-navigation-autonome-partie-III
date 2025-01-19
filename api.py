from typing import List, Dict
from datetime import datetime, timedelta
import json


class Platform:
    def __init__(self
                 , id_platform: int
                 , minimal_arrival_time: datetime
                 , routes: List["Route"] = []
                 , line: str = "N/A"
                 , station_name: str = "N/A"
                 ):
        self.id_platform = id_platform
        self.minimal_arrival_time = minimal_arrival_time
        self.routes = routes
        self.line = line
        self.station_name = station_name
        self.parent: "Platform" = None
             

class Route:
    def __init__(self
                 , id_departure_platform: int
                 , id_arrival_platform: int
                 , departure_time: datetime
                 , arrival_time: datetime
                 , on_foot_travel_time: timedelta
                 ):
        self.id_departure_platform = id_departure_platform
        self.id_arrival_platform = id_arrival_platform
        if(on_foot_travel_time != None):
            self.is_on_foot: bool = True
            self.on_foot_travel_time = timedelta(
                hours = on_foot_travel_time.hour
                , minutes = on_foot_travel_time.minute
                , seconds = on_foot_travel_time.second
            )
        else :
            self.is_on_foot: bool = False
        self.departure_time = departure_time
        self.arrival_time = arrival_time


def get_platform_id(platform_name: str, platforms: Dict[int, "Platform"]):
    for id, platform_data in platforms.items():
        if platform_data.station_name == platform_name:
            return int(id)


def get_platforms_data():
    with open("platforms_data.json", "r") as f:
        platforms_data = json.load(f)
        platforms: Dict[int, "Platform"] = {}
        for id, platform_data in platforms_data.items():
            platform = Platform(int(id)
                                , minimal_arrival_time = None
                                , routes = []
                                , line = platform_data["line"]
                                , station_name = platform_data["station_name"]
                                )
            platforms[int(id)] = platform
        return platforms


def get_routes():
    with open("routes.json", "r") as f:
        routes = json.load(f)
        refined_routes = []
        for route in routes:
            refined_route: "Route" = Route(int(route["id_departure_platform"])
                                           , int(route["id_arrival_platform"])
                                           , datetime.strptime(route["departure_time"], "%Y-%m-%d %H:%M:%S") if route["departure_time"] != None else None
                                           , datetime.strptime(route["arrival_time"], "%Y-%m-%d %H:%M:%S") if route["arrival_time"] != None else None
                                           , datetime.strptime(route["on_foot_travel_time"], "%H:%M:%S") if route["on_foot_travel_time"] != None else None
            )
            refined_routes.append(refined_route)
        return refined_routes
    
    