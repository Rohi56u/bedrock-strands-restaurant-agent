import uuid

# --- Simulated Database ---

# Restaurant Data
RESTAURANTS = [
    {
        "id": 101,
        "name": "The Spice Route",
        "cuisine": "Indian",
        "max_capacity": 50,
        "available_tables": 50,
    },
    {
        "id": 102,
        "name": "La Trattoria",
        "cuisine": "Italian",
        "max_capacity": 40,
        "available_tables": 40,
    },
    {
        "id": 103,
        "name": "Tokyo Sushi Bar",
        "cuisine": "Japanese",
        "max_capacity": 30,
        "available_tables": 30,
    },
]

# Booking Data
BOOKINGS = []

def get_restaurant_by_id(restaurant_id: int):
    """Helper function to get a restaurant by its ID."""
    for restaurant in RESTAURANTS:
        if restaurant["id"] == restaurant_id:
            return restaurant
    return None

def generate_booking_id():
    """Generates a unique booking ID."""
    return f"BKG-{uuid.uuid4().hex[:8].upper()}"

# Pre-populate some bookings for demonstration
def setup_initial_data():
    global BOOKINGS
    # Simulate a booking for The Spice Route (ID 101)
    restaurant_101 = get_restaurant_by_id(101)
    if restaurant_101:
        party_size = 5
        if restaurant_101["available_tables"] >= party_size:
            restaurant_101["available_tables"] -= party_size
            BOOKINGS.append({
                "booking_id": generate_booking_id(),
                "restaurant_id": 101,
                "customer_name": "Initial Customer",
                "party_size": party_size,
                "time": "18:00",
            })

setup_initial_data()

print(f"Initial Restaurants: {RESTAURANTS}")
print(f"Initial Bookings: {BOOKINGS}")
