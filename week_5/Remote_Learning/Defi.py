from datetime import datetime

class Airline:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.planes = []

    def addAirplanes(self,airplanes):
        self.planes += airplanes


class Airplane:
    def __init__(self, id, current_location, company, next_flights):
        self.id = id
        self.current_location =current_location
        self.company = company
        self.next_flights = next_flights

    def fly(self,destination):
        self.current_location = destination

    def location_on_date(self, date):
        for avion in self.next_flights:
            if avion.date == date:
                print(avion.destination)

    def available_on_date(self, date, location):
        if self.current_location == location:
            if self.next_flights == []:
                return True
            else:
                for avion in self.next_flights:
                    if date == avion.date:
                        return False
                # Si la date est supérieur au dernier vol de la liste alors nous vérifions la destination. Si elle est égale à "locatoin" alors un vol est possible
                if date > self.next_flights[-1].date and avion.destination == location:
                        return True
        return False


class Flight:
    def __init__(self, destination, origin, plane, date=datetime.now()):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = destination.city + source.id + date

    def land(self):
        self.plane.destination = self.destination
        self.plane.next_flights.pop(0)

class Airport:
    def __init__(self, city,planes):
        self.city = city
        self.planes = planes
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, datetime):
        for plane in self.planes.next_flights:
            if plane.destination == destination and datetime == plane.date:
                self.scheduled_departures.append(plane.plane)
            else:
                print('Aucun avion disponible')

    def info(self, start_date, end_date):
        for vol in self.scheduled_departures:
            if vol.date <= start_date and vol.date >= end_date :
                print(vol.id)


