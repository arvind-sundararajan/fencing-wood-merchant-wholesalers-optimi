```json
{
    "utils/state_management.py": {
        "content": "
import logging
from typing import Dict, List
from letta import MemoryManager, CoreMemory, SelfEditingMemory

logger = logging.getLogger(__name__)

class StateManager:
    """
    Manages the state of the autonomous fencing supply chain optimizer.
    
    Attributes:
    non_stationary_drift_index (int): The index of the non-stationary drift.
    stochastic_regime_switch (bool): Whether the stochastic regime switch is enabled.
    """

    def __init__(self, non_stationary_drift_index: int, stochastic_regime_switch: bool):
        """
        Initializes the StateManager.
        
        Args:
        non_stationary_drift_index (int): The index of the non-stationary drift.
        stochastic_regime_switch (bool): Whether the stochastic regime switch is enabled.
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch
        self.memory_manager = MemoryManager()

    def update_core_memory(self, memory_blocks: List[Dict]) -> None:
        """
        Updates the core memory of the Letta agent.
        
        Args:
        memory_blocks (List[Dict]): The memory blocks to update.
        """
        try:
            core_memory = CoreMemory()
            core_memory.update(memory_blocks)
            self.memory_manager.update_core_memory(core_memory)
            logger.info('Core memory updated successfully')
        except Exception as e:
            logger.error(f'Error updating core memory: {e}')

    def edit_self_editing_memory(self, core_tools: List[Dict]) -> None:
        """
        Edits the self-editing memory of the Letta agent.
        
        Args:
        core_tools (List[Dict]): The core tools to use for editing.
        """
        try:
            self_editing_memory = SelfEditingMemory()
            self_editing_memory.edit(core_tools)
            logger.info('Self-editing memory edited successfully')
        except Exception as e:
            logger.error(f'Error editing self-editing memory: {e}')

    def recall_memory(self, conversation_persistence: Dict) -> None:
        """
        Recalls the memory of the Letta agent.
        
        Args:
        conversation_persistence (Dict): The conversation persistence to recall.
        """
        try:
            recalled_memory = self.memory_manager.recall_memory(conversation_persistence)
            logger.info('Memory recalled successfully')
            return recalled_memory
        except Exception as e:
            logger.error(f'Error recalling memory: {e}')

    def archival_memory(self, long_term_storage: Dict) -> None:
        """
        Archives the memory of the Letta agent.
        
        Args:
        long_term_storage (Dict): The long-term storage to archive.
        """
        try:
            self.memory_manager.archive_memory(long_term_storage)
            logger.info('Memory archived successfully')
        except Exception as e:
            logger.error(f'Error archiving memory: {e}')

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    state_manager = StateManager(non_stationary_drift_index=10, stochastic_regime_switch=True)
    memory_blocks = [{'key': 'value'}]
    core_tools = [{'tool': 'edit'}]
    conversation_persistence = {'conversation': 'persistence'}
    long_term_storage = {'long_term': 'storage'}
    
    state_manager.update_core_memory(memory_blocks)
    state_manager.edit_self_editing_memory(core_tools)
    state_manager.recall_memory(conversation_persistence)
    state_manager.archival_memory(long_term_storage)
",
        "commit_message": "feat: implement specialized state_management logic"
    }
}
```