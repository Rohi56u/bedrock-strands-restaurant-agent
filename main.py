import os
from typing import List, Dict, Any
from strands_agents.agent import Agent
from strands_agents.tool import Tool
from strands_agents.llm import LLM
from strands_agents.llm.openai import OpenAILLM
from strands_agents.llm.bedrock import BedrockLLM # Placeholder for Bedrock
from restaurant_tools import get_available_restaurants, make_reservation, cancel_reservation, get_restaurant_menu

# --- Configuration ---
# In a real scenario, you would configure the Bedrock client here.
# For this sandbox, we will use the pre-configured OpenAI-compatible LLM.
# To use Bedrock, you would need AWS credentials and a Bedrock client setup.
# LLM_MODEL = "anthropic.claude-3-sonnet-20240229-v1:0" # Example Bedrock model
LLM_MODEL = "gpt-4.1-mini" # Using pre-configured OpenAI-compatible model

def setup_agent() -> Agent:
    """
    Sets up the Strands Agent with the necessary tools.
    """
    # 1. Define the LLM
    # In a real Bedrock setup, you would use:
    # llm = BedrockLLM(model_id=LLM_MODEL, region_name="us-east-1")
    
    # Using the pre-configured OpenAI-compatible LLM for sandbox execution
    llm = OpenAILLM(model=LLM_MODEL)

    # 2. Define the Tools
    tools: List[Tool] = [
        Tool(
            name="get_available_restaurants",
            description="Finds restaurants that match the user's criteria (cuisine, party size, time).",
            func=get_available_restaurants,
        ),
        Tool(
            name="make_reservation",
            description="Books a table at a specific restaurant. Requires restaurant_id, customer_name, party_size, and time.",
            func=make_reservation,
        ),
        Tool(
            name="cancel_reservation",
            description="Cancels an existing reservation using the booking ID.",
            func=cancel_reservation,
        ),
        # 3. Placeholder for MCP Tool Integration
        # In a real scenario, the MCP tool would be loaded dynamically.
        # For demonstration, we include the simulated function as a regular tool.
        Tool(
            name="get_restaurant_menu",
            description="Retrieves the menu for a restaurant. This simulates an external tool loaded via the Model Context Protocol (MCP).",
            func=get_restaurant_menu,
        ),
    ]

    # 4. Create the Agent
    agent = Agent(
        name="RestaurantBookingAssistant",
        description="An intelligent AI agent that helps users find and book restaurants, and can also cancel reservations.",
        llm=llm,
        tools=tools,
        # You would configure the Bedrock AgentCore runtime here for production deployment
        # runtime=BedrockAgentCoreRuntime(...)
    )
    
    return agent

def run_interaction(agent: Agent, prompt: str):
    """
    Runs a single interaction with the agent and prints the result.
    """
    print("-" * 50)
    print(f"USER: {prompt}")
    print("-" * 50)
    
    # The agent will use its planning and tool orchestration capabilities
    response = agent.run(prompt)
    
    print("\nAGENT RESPONSE:")
    print(response.text)
    print("\n")

if __name__ == "__main__":
    print("Setting up the Restaurant Booking Assistant Agent...")
    agent = setup_agent()
    
    # --- Demonstration Scenarios ---
    
    # Scenario 1: Find a restaurant
    run_interaction(
        agent,
        "I need a table for 4 people at an Italian restaurant tonight at 7:30 PM."
    )
    
    # Scenario 2: Make a reservation (assuming the agent selects La Trattoria - ID 102)
    # The agent should be able to infer the next step from the previous context or a direct command.
    run_interaction(
        agent,
        "Please book a table at La Trattoria for me, my name is Rohit Choudhary."
    )
    
    # Scenario 3: Use the simulated MCP tool (get_restaurant_menu)
    run_interaction(
        agent,
        "What is on the menu at The Spice Route (ID 101)?"
    )
    
    # Scenario 4: Cancel a reservation (Requires knowing a booking ID from data_model.py)
    # We will try to cancel the initial booking made in data_model.py
    from data_model import BOOKINGS
    if BOOKINGS:
        initial_booking_id = BOOKINGS[0]["booking_id"]
        run_interaction(
            agent,
            f"I need to cancel my reservation with booking ID {initial_booking_id}."
        )
    else:
        print("Could not run cancellation scenario: No initial bookings found.")
        
    # Scenario 5: Try to book a large party to test capacity logic
    run_interaction(
        agent,
        "Can I book a table for 100 people at any restaurant?"
    )
    
    print("Demonstration complete.")
