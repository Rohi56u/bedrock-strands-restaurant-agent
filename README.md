# AI for Bharat Workshop 4 Project: Restaurant Booking Assistant Agent

This project implements the **Restaurant Booking Assistant** as described in the "AI for Bharat Workshop 4: Build intelligent AI Agents with Amazon Bedrock & Strands." It demonstrates the use of the open-source **Strands Agents SDK** for native planning and tool orchestration, custom tool creation, and a placeholder for **Model Context Protocol (MCP)** integration.

## Project Overview

The core of this project is a Strands Agent that can:
1.  **Search** for available restaurants based on cuisine, party size, and time.
2.  **Book** a table at a selected restaurant.
3.  **Cancel** an existing reservation.
4.  **Simulate** an external tool call (e.g., fetching a menu) via a function that represents an MCP-loaded tool.

## Architecture and Components

| Component | File | Description |
| :--- | :--- | :--- |
| **Data Model** | `data_model.py` | Contains the simulated in-memory database for `RESTAURANTS` and `BOOKINGS`. |
| **Custom Tools** | `restaurant_tools.py` | Implements the core business logic functions (`get_available_restaurants`, `make_reservation`, `cancel_reservation`, and the simulated `get_restaurant_menu` MCP tool). |
| **Agent Setup** | `main.py` | Sets up the Strands Agent, registers the custom tools, and runs demonstration scenarios. |
| **Dependencies** | `requirements.txt` | Lists the necessary Python packages, including `strands-agents` and `pydantic`. |

## Setup and Installation

### Prerequisites

*   Python 3.9+
*   `pip` package manager

### Steps

1.  **Clone the repository** (or download the files):
    ```bash
    git clone <YOUR_GITHUB_REPO_URL>
    cd bedrock-strands-restaurant-agent
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure LLM (Optional but Recommended):**
    The `main.py` script uses a pre-configured OpenAI-compatible LLM for sandbox execution. For a real-world Bedrock deployment, you would need to:
    *   Set up your AWS credentials.
    *   Uncomment and configure the `BedrockLLM` in `main.py`.
    *   Set the `OPENAI_API_KEY` environment variable for the default sandbox setup.

## Running the Agent

Execute the main script to run the demonstration scenarios:

```bash
python3 main.py
```

### Demonstration Scenarios

The `main.py` script includes five pre-defined scenarios to test the agent's capabilities:

1.  **Finding a Restaurant:** Tests the agent's ability to use `get_available_restaurants`.
2.  **Making a Reservation:** Tests the agent's ability to use `make_reservation`.
3.  **MCP Tool Simulation:** Tests the agent's ability to use the simulated `get_restaurant_menu` tool, which represents an external service loaded via MCP.
4.  **Cancelling a Reservation:** Tests the agent's ability to use `cancel_reservation`.
5.  **Capacity Check:** Tests the business logic for handling insufficient capacity.

## Model Context Protocol (MCP) Integration

The `get_restaurant_menu` function in `restaurant_tools.py` serves as a conceptual demonstration of an MCP-integrated tool.

In a production environment, this tool would be hosted on a separate **MCP Server**. The Strands Agent would use a `DynamicMCPClient` to connect to this server and dynamically load the tool's schema and functionality at runtime, extending the agent's capabilities without modifying its core code. This adheres to the workshop's goal of integrating MCP to extend agent capabilities with external tools.
