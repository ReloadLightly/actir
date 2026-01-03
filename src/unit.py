import numpy as np
from .config import WaltzConfig

class State:
    def __init__(self, uid: int):
        self.id = uid
        self.capability = WaltzConfig.INITIAL_CAPABILITY
        self.alive = True
        self.history = [] # <--- CRITICAL: Stores the timeline for the graph

    def step(self, action: int, others: list['State']):
        """
        Execute state logic.
        Action Map:
        0: Internal Balancing (Grow Economy)
        1..N: Attack Agent N
        """
        # Record current state before changing it (for t=0)
        # Or record after. Let's record after update.
        
        if not self.alive:
            self.history.append(0)
            return

        # 1. Passive Costs (Entropy/Maintenance)
        self.capability -= WaltzConfig.MILITARY_COST

        # 2. Action Logic
        if action == 0:
            # Invest in Economy
            self.capability += (self.capability * WaltzConfig.GROWTH_RATE)
        
        # Attacks are handled by the World class

        # 3. Survival Check
        if self.capability < WaltzConfig.MIN_CAPABILITY:
            self.alive = False
            self.capability = 0
            print(f"State {self.id} has collapsed (Death of the State).")
            
        self.history.append(self.capability)

    def get_state_vector(self):
        return np.array([self.capability])