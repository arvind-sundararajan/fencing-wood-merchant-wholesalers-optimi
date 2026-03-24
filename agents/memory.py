```json
{
    "agents/memory.py": {
        "content": "
import logging
from typing import Dict, List
from letta import Memory, CoreMemory, SelfEditingMemory

class FencingMemoryManager:
    """
    Manages the memory of the fencing supply chain optimizer agent.
    """
    def __init__(self, memory: Memory):
        """
        Initializes the memory manager.

        Args:
        - memory (Memory): The memory of the agent.
        """
        self.memory = memory
        self.core_memory = CoreMemory()
        self.self_editing_memory = SelfEditingMemory()
        self.logger = logging.getLogger(__name__)

    def update_non_stationary_drift_index(self, drift_index: float) -> None:
        """
        Updates the non-stationary drift index in the core memory.

        Args:
        - drift_index (float): The new drift index.

        Raises:
        - Exception: If the update fails.
        """
        try:
            self.core_memory.update('non_stationary_drift_index', drift_index)
            self.logger.info('Updated non-stationary drift index')
        except Exception as e:
            self.logger.error(f'Failed to update non-stationary drift index: {e}')

    def stochastic_regime_switch(self, regime: str) -> None:
        """
        Switches the stochastic regime in the self-editing memory.

        Args:
        - regime (str): The new regime.

        Raises:
        - Exception: If the switch fails.
        """
        try:
            self.self_editing_memory.edit('stochastic_regime', regime)
            self.logger.info(f'Switched to {regime} regime')
        except Exception as e:
            self.logger.error(f'Failed to switch regime: {e}')

    def recall_memory(self, key: str) -> Dict:
        """
        Recalls a memory block from the core memory.

        Args:
        - key (str): The key of the memory block.

        Returns:
        - Dict: The recalled memory block.

        Raises:
        - Exception: If the recall fails.
        """
        try:
            return self.core_memory.recall(key)
        except Exception as e:
            self.logger.error(f'Failed to recall memory: {e}')
            return {}

    def archive_memory(self, key: str, value: Dict) -> None:
        """
        Archives a memory block to the archival memory.

        Args:
        - key (str): The key of the memory block.
        - value (Dict): The value of the memory block.

        Raises:
        - Exception: If the archiving fails.
        """
        try:
            self.memory.archive(key, value)
            self.logger.info(f'Archived {key} memory block')
        except Exception as e:
            self.logger.error(f'Failed to archive memory: {e}')

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    memory = Memory()
    manager = FencingMemoryManager(memory)
    manager.update_non_stationary_drift_index(0.5)
    manager.stochastic_regime_switch('regime1')
    recalled_memory = manager.recall_memory('memory_block1')
    print(recalled_memory)
    manager.archive_memory('memory_block2', {'value': 'archived'})
",
        "commit_message": "feat: implement specialized memory logic"
    }
}
```