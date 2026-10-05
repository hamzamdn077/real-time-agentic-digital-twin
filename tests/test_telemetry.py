from producer.telemetry import generate_telemetry


def test_normal_telemetry():

    event = generate_telemetry(
        "server-test",
        anomaly_type=None,
    )

    assert event["server_id"] == "server-test"
    assert 0 <= event["cpu_usage"] <= 100
    assert 0 <= event["memory_usage"] <= 100
    assert event["temperature"] > 0
    assert event["power_consumption"] > 0
    assert event["anomaly_type"] is None


def test_overheating():

    event = generate_telemetry(
        "server-test",
        anomaly_type="overheating",
    )

    assert event["temperature"] > 80


def test_cpu_overload():

    event = generate_telemetry(
        "server-test",
        anomaly_type="cpu_overload",
    )

    assert event["cpu_usage"] > 90


def test_cooling_failure():

    event = generate_telemetry(
        "server-test",
        anomaly_type="cooling_failure",
    )

    assert event["temperature"] > 75
    assert event["fan_speed"] < 30


def test_power_anomaly():

    event = generate_telemetry(
        "server-test",
        anomaly_type="power_anomaly",
    )

    assert event["power_consumption"] > 500