from typing import List, Dict, Any
from data_model import RESTAURANTS, BOOKINGS, get_restaurant_by_id, generate_booking_id

# --- Custom Tools for Strands Agent ---

def get_available_restaurants(cuisine: str, party_size: int, time: str) -> List[Dict[str, Any]]:
    """
    Searches for available restaurants based on cuisine, party size, and time.

    :param cuisine: The desired cuisine (e.g., "Indian", "Italian").
    :param party_size: The number of people in the party.
    :param time: The desired reservation time (e.g., "19:30").
    :return: A list of available restaurants with their ID, name, and current capacity.
    """
    print(f"Tool called: get_available_restaurants(cuisine={cuisine}, party_size={party_size}, time={time})")
    
    available_list = []
    for restaurant in RESTAURANTS:
        # Simple check: capacity is sufficient and cuisine matches (case-insensitive)
        if restaurant["available_tables"] >= party_size and restaurant["cuisine"].lower() == cuisine.lower():
            available_list.append({
                "id": restaurant["id"],
                "name": restaurant["name"],
                "cuisine": restaurant["cuisine"],
                "available_capacity": restaurant["available_tables"],
            })
            
    return available_list

def make_reservation(restaurant_id: int, customer_name: str, party_size: int, time: str) -> Dict[str, Any]:
    """
    Attempts to make a reservation at the specified restaurant.

    :param restaurant_id: The ID of the restaurant to book.
    :param customer_name: The name for the reservation.
    :param party_size: The number of people in the party.
    :param time: The reservation time.
    :return: A dictionary with the booking status and details.
    """
    print(f"Tool called: make_reservation(id={restaurant_id}, name={customer_name}, size={party_size}, time={time})")
    
    restaurant = get_restaurant_by_id(restaurant_id)
    
    if not restaurant:
        return {"status": "failure", "message": f"Restaurant with ID {restaurant_id} not found."}
        
    if restaurant["available_tables"] < party_size:
        return {"status": "failure", "message": f"Not enough capacity at {restaurant['name']} for a party of {party_size}. Available: {restaurant['available_tables']}."}
        
    # Make the booking
    restaurant["available_tables"] -= party_size
    booking_id = generate_booking_id()
    
    new_booking = {
        "booking_id": booking_id,
        "restaurant_id": restaurant_id,
        "customer_name": customer_name,
        "party_size": party_size,
        "time": time,
    }
    BOOKINGS.append(new_booking)
    
    return {
        "status": "success",
        "message": f"Reservation confirmed! Booking ID: {booking_id}.",
        "details": new_booking,
        "new_capacity": restaurant["available_tables"],
    }

def cancel_reservation(booking_id: str) -> Dict[str, str]:
    """
    Cancels an existing reservation using the booking ID.

    :param booking_id: The unique ID of the reservation to cancel.
    :return: A dictionary with the cancellation status message.
    """
    print(f"Tool called: cancel_reservation(booking_id={booking_id})")
    
    for i, booking in enumerate(BOOKINGS):
        if booking["booking_id"] == booking_id:
            # Find the restaurant and restore capacity
            restaurant = get_restaurant_by_id(booking["restaurant_id"])
            if restaurant:
                restaurant["available_tables"] += booking["party_size"]
            
            # Remove the booking
            BOOKINGS.pop(i)
            
            return {"status": "success", "message": f"Reservation {booking_id} for {booking['customer_name']} at {restaurant['name']} has been successfully cancelled."}
            
    return {"status": "failure", "message": f"Reservation with ID {booking_id} not found."}

# --- Placeholder for MCP Tool ---

def get_restaurant_menu(restaurant_id: int) -> Dict[str, Any]:
    """
    (Simulated MCP Tool) Retrieves a sample menu for the specified restaurant.
    In a real scenario, this would be an external tool loaded via the Model Context Protocol (MCP).

    :param restaurant_id: The ID of the restaurant.
    :return: A dictionary containing the restaurant name and a sample menu.
    """
    print(f"Tool called: get_restaurant_menu(restaurant_id={restaurant_id}) - SIMULATED MCP TOOL")
    
    restaurant = get_restaurant_by_id(restaurant_id)
    
    if not restaurant:
        return {"status": "failure", "message": f"Restaurant with ID {restaurant_id} not found."}
        
    # Simple simulated menu
    menu = {
        "The Spice Route": ["Butter Chicken", "Naan Bread", "Vegetable Biryani"],
        "La Trattoria": ["Margherita Pizza", "Spaghetti Carbonara", "Tiramisu"],
        "Tokyo Sushi Bar": ["Salmon Nigiri", "California Roll", "Miso Soup"],
    }
    
    return {
        "status": "success",
        "restaurant_name": restaurant["name"],
        "menu": menu.get(restaurant["name"], ["No menu available"]),
        "note": "This is a simulated response from an external MCP tool.",
    }
