# ACTIR: A Computational Theory of International Relations

**Status:** Active Development (Pre-Alpha)
**Author:** Roland Nikolaus Loechli, PhD

## Overview
ACTIR is a Multi-Agent Reinforcement Learning (MARL) environment designed to operationalize the "Third Image" of International Relations theory: **Structural Realism**.

Unlike standard game-theoretic models (Diplomacy, Risk) which rely on fixed turns and victory points, ACTIR models the international system as a continuous, anarchic process defined by:
1.  **Survival** as the primary objective.
2.  **The Security Dilemma** (defensive moves are perceived as offensive).
3.  **The Stopping Power of Water** (geographic constraints on hegemony).

## Core Architecture
* **`src/world.py`**: The physics engine of Anarchy. Enforces the "Self-Help" system constraints.
* **`src/unit.py`**: The "Like-Units" (Waltz, 1979). Agents distinguished only by material capabilities.
* **`waltz_baseline.ipynb`**: Simulation of a pure Waltzian world without learning (Random Walk).

## Research Goals
* **Phase 1 (Current):** Establish a Waltzian baseline where anarchy produces suboptimal outcomes (war) despite rational survival goals.
* **Phase 2:** Implement "Constructivist" agents (Wendt) that evolve identity via NLP.
* **Phase 3:** Simulate the "Unipolar to Multipolar" transition (2017-Present) to identify tipping points in the East China Sea security architecture.

## Initial Results
Baseline simulation of 5 agents under Structural Realism constraints (Random Policy).
Demonstrates the inevitable emergence of Hegemony (Unipolarity) without active balancing strategies.
![Baseline Simulation](simulation_baseline.png)