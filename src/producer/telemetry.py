import random
import uuid
from datetime import datetime, timezone


def generate_telemetry(server_id: str, anomaly: bool = False) -> dict:

    if anomaly:
        cpu = random.uniform(90, 100)
        memory = random.uniform(80, 98)
        temperature = random.uniform(75, 90)
        power = random.uniform(400, 550)
        fan_speed = random.uniform(20, 45)

    else:
        cpu = random.uniform(20, 80)
        memory = random.uniform(30, 75)
        temperature = 35 + (cpu * 0.35) + random.uniform(-2, 2)
        fan_speed = 30 + (cpu * 0.6)
        power = 120 + (cpu * 3) + random.uniform(-10, 10)

    return {
        "event_id": str(uuid.uuid4()),
        "server_id": server_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cpu_usage": round(cpu, 2),
        "memory_usage": round(memory, 2),
        "temperature": round(temperature, 2),
        "power_consumption": round(power, 2),
        "network_traffic": round(random.uniform(100, 1000), 2),
        "fan_speed": round(fan_speed, 2),
    }