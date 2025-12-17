import requests
import requests
import time
import json
import logging
from kafka import KafkaProducer


def get_weather():
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": 51.5,
            "longitude": -0.11,
            "current": "temperature_2m",
        },
    )
    return response.json()

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    api_version=(0, 10, 1),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = 'weather_data_demo'

def main():
    while True:
        weather_data = get_weather()
        producer.send(topic_name, weather_data)
        print(f"Sent weather data: {weather_data}")
        time.sleep(10)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
