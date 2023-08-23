class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []
        # Populate the flights list with data
        self.flights.append(Flight("AI161E90", "BLR", "BOM", 5600))
        self.flights.append(Flight("BR161F91", "BOM", "BBI", 6750))
        self.flights.append(Flight("AI161F99", "BBI", "BLR", 8210))
        self.flights.append(Flight("VS171E20", "JLR", "BBI", 5500))
        self.flights.append(Flight("AS171G30", "HYD", "JLR", 4400))
        self.flights.append(Flight("AI131F49", "HYD", "BOM", 3499))
        
    def search_by_city(self, city):
        result = []
        for flight in self.flights:
            if flight.source == city or flight.destination == city:
                result.append(flight)
        return result
    
    def search_flights_from(self, city):
        result = []
        for flight in self.flights:
            if flight.source == city:
                result.append(flight)
        return result
    
    def search_between_cities(self, source, destination):
        result = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination:
                result.append(flight)
        return result

def main():
    flight_table = FlightTable()
    
    print("Choose a search parameter:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        city = input("Enter the city: ")
        result = flight_table.search_by_city(city)
    elif choice == 2:
        city = input("Enter the source city: ")
        result = flight_table.search_flights_from(city)
    elif choice == 3:
        source = input("Enter the source city: ")
        destination = input("Enter the destination city: ")
        result = flight_table.search_between_cities(source, destination)
    else:
        print("Invalid choice")
        return
    
    if result:
        print("Flight ID   From   To     Price")
        for flight in result:
            print(f"{flight.flight_id}   {flight.source}   {flight.destination}   {flight.price}")
    else:
        print("No flights found for the given criteria.")

if __name__ == "__main__":
    main()
