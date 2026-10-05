import random


ANOMALY_TYPES = [
    "overheating",
    "cpu_overload",
    "cooling_failure",
    "power_anomaly",
]


def generate_anomaly_type(probability: float = 0.05) -> str | None:
    if random.random() >= probability:
        return None

    return random.choice(ANOMALY_TYPES)