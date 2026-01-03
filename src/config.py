from dataclasses import dataclass

@dataclass
class WaltzConfig:
    """
    Configuration for the Waltzian Structural Realist Environment.
    """
    # System Dimensions
    NUM_AGENTS: int = 5
    MAX_STEPS: int = 200
    
    # Survival Thresholds
    MIN_CAPABILITY: float = 0.1  # State Failure threshold
    INITIAL_CAPABILITY: float = 0.5 # <--- This was missing!
    
    # "Guns vs Butter" Dynamics
    GROWTH_RATE: float = 0.03    # Economic compound growth
    MILITARY_COST: float = 0.01  # Upkeep cost of standing army
    WAR_COST_FIXED: float = 0.1  # Immediate destruction from conflict
    WAR_LOOT_FRACTION: float = 0.15 # What the winner takes