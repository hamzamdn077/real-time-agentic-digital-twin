import json
import time

from producer.telemetry import generate_telemetry
from producer.anomalies import should_generate_anomaly


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

            anomaly = should_generate_anomaly()

            event = generate_telemetry(
                server_id=server_id,
                anomaly=anomaly,
            )

            print(json.dumps(event))

        time.sleep(5)


if __name__ == "__main__":
    main()