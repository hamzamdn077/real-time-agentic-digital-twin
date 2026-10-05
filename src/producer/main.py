import json
import time

from producer.telemetry import generate_telemetry
from producer.anomalies import generate_anomaly_type


SERVERS = [
    "server-001",
    "server-002",
    "server-003",
    "server-004",
    "server-005",
]


def main():
    while True:
        for server_id in SERVERS:

            anomaly_type = generate_anomaly_type()

            event = generate_telemetry(
                server_id=server_id,
                anomaly_type=anomaly_type,
            )

            print(json.dumps(event))

        time.sleep(5)


if __name__ == "__main__":
    main()