# Importiere die Bibliothek geopy, um die Distanz zu berechnen
import csv
import socket
from folium.utilities import os
from geopy.distance import geodesic
# Eine Klasse, die die Informationen �ber eine Stadt speichert
class City:
    cities = {}
    def __init__(self,id, name, gps, rating, hotel_cost, ticket_cost, driving_cost, distance_km, days_of_stay):
        self.name = name
        self.id = id
        self.gps = gps # Ein Tupel aus (latitude, longitude)
        self.rating = rating
        self.hotel_cost = float(hotel_cost) # Pro Nacht
        self.ticket_cost = float(ticket_cost)
        self.driving_cost = float(driving_cost)
        self.distance_km = float(distance_km)
        self.days_of_stay = int(days_of_stay)
    def to_dict(self):
        # Convert the City object to a dictionary
        return {
            'id': self.id,
            'name': self.name,
            'gps': self.gps,
            'rating': self.rating,
            'hotel_cost': self.hotel_cost,
            'ticket_cost': self.ticket_cost,
            'driving_cost': self.driving_cost,
            'distance_km': self.distance_km,
            'days_of_stay': self.days_of_stay
        }
        
    def update_hotel_cost(self, new_hotel_cost):
        self.hotel_cost = float(new_hotel_cost)

    def update_ticket_cost(self, new_ticket_cost):
        self.ticket_cost = float(new_ticket_cost)

    def update_rating(self, new_rating):
        self.rating = new_rating  
        
    def update_days_of_stay(self, new_days_of_stay):
        self.days_of_stay = new_days_of_stay
        
    def get_cost(self):
        cost = self.hotel_cost + self.ticket_cost + self.driving_cost
        return cost
    
    def update_driving_cost(self, new_driving_cost):
        self.driving_cost = float(new_driving_cost)
        
    def update_distance_km(self, new_distance_km):
        self.distance_km = float(new_distance_km)
    
def get_cities():
    cities = {} 
    # Schritt 2: �ffnen der CSV-Datei und Erstellen von City-Objekten
    csv_path = f'C:\\Users\\{os.getlogin()}\\source\\repos\\Intelligenter_Reiseassistent\\Intelligenter_Reiseassistent\\static\csv\\cities.csv'
    with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        # next(reader)  # �berspringen Sie die Kopfzeile, falls vorhanden
        # Schritt 3: Erstellen von City-Objekten und Hinzuf�gen zur Liste
        for row in reader:
            # Angenommen, jede Zeile hat Stadtname, Bev�lkerung und Land in dieser Reihenfolge
            city = City(row[0], row[1],(row[4],row[5]),0 , row[6], row[7], 0.0, 0.0, 0)
            cities[city.name] = city
    return cities

