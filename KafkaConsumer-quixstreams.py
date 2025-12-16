import json
from quixstreams import Application


def main():
    app = Application(
        broker_address = "localhost:9092",
        loglevel="DEBUG",
        consumer_group = "weather_reader",
        auto_offset_reset="earliest"
    )

    with app.get_consumer() as consumer:
        consumer.subscribe(["weather_data_demo"])

    while True:
        msg = consumer.poll(1)

        if msg is not None:
            print("Waiting for data")
        elif msg.error() is not None:
            print(f"Error occurred: {msg.error().str()}")
        else:
            key = msg.key().decode('utf-8')
            value = json.loads(msg.value())
            offest = msg.offset()
            print(f"Received message: key={key}, value={value}, offset={offest}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
