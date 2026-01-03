from src.world import AnarchicSystem
import numpy as np

# Initialize Waltz's World
world = AnarchicSystem()

print("GENESIS:", world.get_distribution_of_capabilities())

# Simulate 10 steps of random anarchy
for t in range(10):
    # Random actions: 0=Grow, 1=Attack Agent 0, 2=Attack Agent 1...
    random_actions = np.random.randint(0, 4, size=4)
    world.step(random_actions)
    print(f"Year {t}: {world.get_distribution_of_capabilities()}")