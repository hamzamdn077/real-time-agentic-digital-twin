import random
import uuid
from datetime import datetime, timezone


def generate_telemetry(
    server_id: str,
    anomaly_type: str | None = None,
) -> dict:

    # Normal conditions
    cpu = random.uniform(20, 80)
    memory = random.uniform(30, 75)

    temperature = 35 + (cpu * 0.35) + random.uniform(-2, 2)
    fan_speed = 30 + (cpu * 0.6)
    power = 120 + (cpu * 3) + random.uniform(-10, 10)

    # Anomaly: overheating
    if anomaly_type == "overheating":
        temperature = random.uniform(80, 95)
        fan_speed = random.uniform(60, 90)

    # Anomaly: CPU overload
    elif anomaly_type == "cpu_overload":
        cpu = random.uniform(90, 100)
        memory = random.uniform(75, 95)
        temperature = random.uniform(70, 85)
        power = random.uniform(400, 550)
        fan_speed = random.uniform(70, 100)

    # Anomaly: cooling failure
    elif anomaly_type == "cooling_failure":
        temperature = random.uniform(75, 90)
        fan_speed = random.uniform(10, 30)

    # Anomaly: abnormal power consumption
    elif anomaly_type == "power_anomaly":
        power = random.uniform(500, 700)

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
        "anomaly_type": anomaly_type,
    }