import subprocess
import time
import socket
import sys

KAFKA_BASE = r"C:\kafka"
KAFKA_CMD = (
    f'cd /d "{KAFKA_BASE}" && '
    r'bin\windows\kafka-server-start.bat config\kraft\server.properties'
)

BROKER_HOST = "localhost"
BROKER_PORT = 9092
STARTUP_TIMEOUT = 60  # seconds


def is_port_open(host, port):
    try:
        with socket.create_connection((host, port), timeout=2):
            return True
    except OSError:
        return False


def start_kafka():
    print("🚀 Starting Kafka KRaft broker...\n")

    process = subprocess.Popen(
        KAFKA_CMD,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )

    start_time = time.time()

    while True:
        if time.time() - start_time > STARTUP_TIMEOUT:
            print("\n❌ Kafka startup timed out")
            process.terminate()
            sys.exit(1)

        line = process.stdout.readline()
        if line:
            print(f"Kafka: {line.strip()}")

            # ✅ THIS is the only real readiness signal
            if "KafkaServer" in line and "started" in line:
                break

    # Extra safety: ensure port is actually listening
    print("\n⏳ Verifying broker port...")
    for _ in range(10):
        if is_port_open(BROKER_HOST, BROKER_PORT):
            print("✅ Kafka broker is READY on localhost:9092")
            return process
        time.sleep(1)

    print("❌ Kafka started but port 9092 is not open")
    process.terminate()
    sys.exit(1)


if __name__ == "__main__":
    kafka_process = start_kafka()

    try:
        print("\n🟢 Kafka is running. Press CTRL+C to stop.")
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n🛑 Shutting down Kafka...")
        kafka_process.terminate()
        kafka_process.wait()
        print("✅ Kafka stopped cleanly")
