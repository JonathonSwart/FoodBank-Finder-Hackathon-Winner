import googlemaps
from .bank import Bank
# from bank import Bank
from geopy.distance import geodesic as GD
import requests

api_key = "GOOGLE_API_KEY"


def get_banks(zip, radius):
    radius = int(radius) * 1000
    results_list = []
    map_client = googlemaps.Client(api_key)

    query = "Food Banks near " + zip
    response = map_client.places(query=query, radius=radius)
    results = response.get('results')

    for result in results:
        address = result['formatted_address']
        name = result['name']
        rating = result['rating']
        lat1 = result['geometry']['location']['lat']
        long1 = result['geometry']['location']['lng']
        if 'opening_hours' in result:
            is_open = result['opening_hours']['open_now']
        else:
            is_open = "Not Listed"
        lat2, long2 = get_long_lat(zip)
        distance = get_distance(lat1, lat2, long1, long2)
        obj = Bank(name, address, is_open, rating, distance)
        results_list.append(obj)

    return results_list


def get_distance(lat1, lat2, long1, long2):
    origin = (lat1, long1)
    destination = (lat2, long2)
    distance = GD(origin, destination).km
    return str(round(float(distance), 1))


def get_long_lat(zip):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={zip}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    return latitude, longitude


def find_highlights(bank_list):
    highest_rated = bank_list[0]
    closest_distance = bank_list[0]
    for bank in bank_list:
        if bank.rating > highest_rated.rating:
            highest_rated = bank
        if bank.distance < closest_distance.distance:
            closest_distance = bank

    return highest_rated, closest_distance
