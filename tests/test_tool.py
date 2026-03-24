```json
{
    "tests/test_tool.py": {
        "content": "
import logging
from typing import Dict, List
from letta import LettaAgent, MemoryBlock
from haystack import Document

def initialize_tool(agent: LettaAgent) -> None:
    """
    Initialize the tool with the given agent.

    Args:
    agent (LettaAgent): The agent to initialize the tool with.
    """
    try:
        logging.info('Initializing tool')
        agent.core_memory.update({'tool_initialized': True})
    except Exception as e:
        logging.error(f'Error initializing tool: {e}')

def update_non_stationary_drift_index(agent: LettaAgent, index: float) -> None:
    """
    Update the non-stationary drift index in the agent's memory.

    Args:
    agent (LettaAgent): The agent to update the index for.
    index (float): The new non-stationary drift index.
    """
    try:
        logging.info('Updating non-stationary drift index')
        agent.core_memory.update({'non_stationary_drift_index': index})
    except Exception as e:
        logging.error(f'Error updating non-stationary drift index: {e}')

def perform_stochastic_regime_switch(agent: LettaAgent, regime: str) -> None:
    """
    Perform a stochastic regime switch in the agent's memory.

    Args:
    agent (LettaAgent): The agent to perform the regime switch for.
    regime (str): The new regime.
    """
    try:
        logging.info('Performing stochastic regime switch')
        agent.core_memory.update({'stochastic_regime_switch': regime})
    except Exception as e:
        logging.error(f'Error performing stochastic regime switch: {e}')

def recall_memory(agent: LettaAgent) -> Dict:
    """
    Recall the agent's memory.

    Args:
    agent (LettaAgent): The agent to recall memory for.

    Returns:
    Dict: The recalled memory.
    """
    try:
        logging.info('Recalling memory')
        return agent.core_memory.get_all()
    except Exception as e:
        logging.error(f'Error recalling memory: {e}')
        return {}

def simulate_rocket_science(agent: LettaAgent) -> None:
    """
    Simulate the 'Rocket Science' problem.

    Args:
    agent (LettaAgent): The agent to simulate the problem for.
    """
    try:
        logging.info('Simulating Rocket Science problem')
        # Initialize tool
        initialize_tool(agent)
        
        # Update non-stationary drift index
        update_non_stationary_drift_index(agent, 0.5)
        
        # Perform stochastic regime switch
        perform_stochastic_regime_switch(agent, 'regime_1')
        
        # Recall memory
        memory = recall_memory(agent)
        logging.info(f'Recalled memory: {memory}')
    except Exception as e:
        logging.error(f'Error simulating Rocket Science problem: {e}')

if __name__ == '__main__':
    # Create a new Letta agent
    agent = LettaAgent()
    
    # Simulate the Rocket Science problem
    simulate_rocket_science(agent)
",
        "commit_message": "feat: implement specialized test_tool logic"
    }
}
```