import random


def should_generate_anomaly(probability: float = 0.05) -> bool:
    """
    Generate an anomaly with the given probability.
    Default: 5%.
    """
    return random.random() < probability