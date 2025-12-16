# Restaurant Booking Assistant Agent Design

This document outlines the data model and custom tools required for the Strands Agent-based restaurant booking assistant, as specified in the Workshop 4 project.

## 1. Data Model (Simulated Database)

To keep the project self-contained and runnable without external dependencies, we will use in-memory Python data structures to simulate a database.

### 1.1. Restaurant Data (`RESTAURANTS`)

A list of dictionaries representing the available restaurants. The `available_tables` field will be dynamically updated upon booking.

| Field | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `id` | `int` | Unique identifier for the restaurant. | `101` |
| `name` | `str` | Name of the restaurant. | `"The Spice Route"` |
| `cuisine` | `str` | Type of food served. | `"Indian"` |
| `max_capacity` | `int` | Maximum number of people the restaurant can seat. | `50` |
| `available_tables` | `int` | Current available capacity. | `40` |

### 1.2. Booking Data (`BOOKINGS`)

A list of dictionaries to store successful reservations.

| Field | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `booking_id` | `str` | Unique ID for the reservation (e.g., a UUID). | `"BKG-20251216-001"` |
| `restaurant_id` | `int` | ID of the booked restaurant. | `101` |
| `customer_name` | `str` | Name of the person who made the booking. | `"Rohit Choudhary"` |
| `party_size` | `int` | Number of people in the party. | `4` |
| `time` | `str` | Time of the reservation (e.g., "HH:MM"). | `"19:30"` |

## 2. Custom Tools for Strands Agent

These tools will be implemented as Python functions and registered with the Strands Agent to allow it to perform actions.

### 2.1. `get_available_restaurants`

| Parameter | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| `cuisine` | `str` | The desired cuisine (e.g., "Indian", "Italian"). | Yes |
| `party_size` | `int` | The number of people in the party. | Yes |
| `time` | `str` | The desired reservation time (e.g., "19:30"). | Yes |

**Function:** Searches the `RESTAURANTS` data for entries where `available_tables` >= `party_size` and `cuisine` matches.

### 2.2. `make_reservation`

| Parameter | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| `restaurant_id` | `int` | The ID of the restaurant to book. | Yes |
| `customer_name` | `str` | The name for the reservation. | Yes |
| `party_size` | `int` | The number of people in the party. | Yes |
| `time` | `str` | The reservation time. | Yes |

**Function:** Checks if the restaurant is available. If yes, it decrements `available_tables` and adds a new entry to `BOOKINGS`. Returns the new `booking_id` or an error message.

### 2.3. `cancel_reservation`

| Parameter | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| `booking_id` | `str` | The unique ID of the reservation to cancel. | Yes |

**Function:** Finds the booking in `BOOKINGS`. If found, it removes the booking and increments the corresponding restaurant's `available_tables`. Returns a success or failure message.

## 3. Model Context Protocol (MCP) Integration Placeholder

The workshop requires demonstrating MCP integration. We will include a placeholder tool and configuration to show how an external MCP server would be connected.

### 3.1. MCP Tool Example: `get_restaurant_menu`

This tool would typically be hosted on a separate MCP server. For this project, we will define the tool's signature and include comments on how to configure the Strands Agent to use an external MCP client.

| Parameter | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| `restaurant_id` | `int` | The ID of the restaurant. | Yes |

**Function:** (Simulated) Returns a sample menu for the specified restaurant. This demonstrates extending the agent's capabilities with external, dynamically loaded tools.

---
*This design will guide the implementation in the subsequent phases.*
