from producer.telemetry import generate_telemetry


def test_normal_telemetry():

    event = generate_telemetry(
        "server-test",
        anomaly=False,
    )

    assert event["server_id"] == "server-test"
    assert 0 <= event["cpu_usage"] <= 100
    assert 0 <= event["memory_usage"] <= 100
    assert event["temperature"] > 0


def test_anomaly_telemetry():

    event = generate_telemetry(
        "server-test",
        anomaly=True,
    )

    assert event["cpu_usage"] > 90
    assert event["temperature"] > 75