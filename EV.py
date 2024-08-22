import datetime

# Data for Charging Stations
charging_stations = [
    {
        'id': 1,
        'name': 'Duvvada Charging Station',
        'location': 'Duvvada',
        'slots': [None] * 5  # 5 slots per station, initialized as None (available)
    },
    {
        'id': 2,
        'name': 'Vepagunta Charging Station',
        'location': 'Vepagunta',
        'slots': [None] * 10  # 10 slots per station
    },
    {
        'id': 3,
        'name': 'Seethamadhara Charging Station',
        'location': 'Seethamadhara',
        'slots': [None] * 10  # 10 slots per station
    }
]

# Function to search for charging stations by name or location
def search_charging_stations(query=None):
    found_stations = []
    for station in charging_stations:
        if query and (query.lower() in station['name'].lower() or query.lower() in station['location'].lower()):
            found_stations.append(station)
    return found_stations

# Function to display charging stations
def display_stations(stations):
    if not stations:
        print("No stations found!")
        return
    print("\nAvailable Charging Stations:")
    for station in stations:
        print(f"ID: {station['id']}, Name: {station['name']}, Location: {station['location']}")

# Function to book a charging slot
def book_slot(station_id, time_slot):
    for station in charging_stations:
        if station['id'] == station_id:
            if 0 <= time_slot < len(station['slots']):
                if station['slots'][time_slot] is None:
                    station['slots'][time_slot] = 'Booked'
                    print(f"Slot {time_slot + 1} at {station['name']} successfully booked!")
                    return True
                else:
                    print("Slot already booked! Please select a different slot.")
                    return False
            else:
                print("Invalid slot number! Please select a valid slot.")
                return False
    print("Station not found!")
    return False

# Function to cancel a booking
def cancel_booking(station_id, time_slot):
    for station in charging_stations:
        if station['id'] == station_id:
            if 0 <= time_slot < len(station['slots']):
                if station['slots'][time_slot] == 'Booked':
                    station['slots'][time_slot] = None
                    print(f"Booking for Slot {time_slot + 1} at {station['name']} successfully canceled!")
                    return True
                else:
                    print("Slot is not booked! No booking to cancel.")
                    return False
            else:
                print("Invalid slot number! Please select a valid slot.")
                return False
    print("Station not found!")
    return False

# Function to check slot availability
def check_slot_availability(station_id):
    for station in charging_stations:
        if station['id'] == station_id:
            available_slots = [i + 1 for i, slot in enumerate(station['slots']) if slot is None]
            if available_slots:
                print(f"Available slots at {station['name']}: {available_slots}")
            else:
                print(f"No available slots at {station['name']}.")
            return available_slots
    print("Station not found!")
    return []

# Main Program
while True:
    print("\nEV Charging Station Finder and Slot Booking\n")
    print("1. Search for Charging Stations")
    print("2. Book a Slot")
    print("3. Cancel a Booking")
    print("4. Check Slot Availability")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        query = input("Enter station name or location to search: ")
        found_stations = search_charging_stations(query)
        display_stations(found_stations)

    elif choice == '2':
        station_id = int(input("Enter Station ID to book a slot: "))
        time_slot = int(input("Enter Slot Number (1 to 5): ")) - 1
        book_slot(station_id, time_slot)

    elif choice == '3':
        station_id = int(input("Enter Station ID to cancel booking: "))
        time_slot = int(input("Enter Slot Number (1 to 5): ")) - 1
        cancel_booking(station_id, time_slot)

    elif choice == '4':
        station_id = int(input("Enter Station ID to check slot availability: "))
        check_slot_availability(station_id)

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please select a valid option.")
