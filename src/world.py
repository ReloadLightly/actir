import numpy as np
from .config import WaltzConfig
from .unit import State

class AnarchicSystem:
    def __init__(self):
        self.states = [State(i) for i in range(WaltzConfig.NUM_AGENTS)]
        self.steps = 0
        
    def get_distribution_of_capabilities(self):
        return [s.capability for s in self.states]

    def get_history(self):
        """
        Returns the full timeline of power for all agents.
        Shape: (Num_Agents, Time_Steps)
        """
        # Transpose list of lists so we can plot easy lines
        return [s.history for s in self.states]

    def step(self, actions: list[int]):
        """
        The Transition Function T(s, a) -> s'
        """
        self.steps += 1
        attacks = []
        
        # 1. Parse Actions
        for i, agent in enumerate(self.states):
            if not agent.alive:
                # Still need to step dead agents so they record '0' in history
                agent.step(0, self.states)
                continue
                
            act = actions[i]
            if act > 0: # Attack Logic
                target_idx = act - 1
                if target_idx != i:
                    attacks.append((i, target_idx))
            
            # Execute Internal Logic (Growth/Maintenance)
            agent.step(0 if act > 0 else 0, self.states)

        # 2. Resolve Wars
        self._resolve_conflicts(attacks)

    def _resolve_conflicts(self, attacks):
        np.random.shuffle(attacks)
        for att_idx, def_idx in attacks:
            attacker = self.states[att_idx]
            defender = self.states[def_idx]
            
            if not attacker.alive or not defender.alive:
                continue

            total_power = attacker.capability + defender.capability
            prob_win = attacker.capability / (total_power + 1e-9)
            
            # War Friction
            attacker.capability -= WaltzConfig.WAR_COST_FIXED
            defender.capability -= WaltzConfig.WAR_COST_FIXED
            
            if np.random.random() < prob_win:
                loot = defender.capability * WaltzConfig.WAR_LOOT_FRACTION
                attacker.capability += loot
                defender.capability -= loot
            else:
                attacker.capability -= (attacker.capability * 0.05)