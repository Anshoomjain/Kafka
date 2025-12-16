# Kafka
Learning Apache Kafka 



# Kafka Weather Data Pipeline

A simple end-to-end pipeline using Kafka to fetch, publish, and consume real-time weather data.

---

## Overview

This project demonstrates:
- Starting a Kafka KRaft broker locally on Windows.
- Producing weather data from the Open-Meteo API to a Kafka topic.
- Consuming and displaying weather data from Kafka.

---

## Prerequisites

- Python 3.x
- Kafka installed at `C:\kafka` (Windows)
- Internet access for the Open-Meteo API

---

## Scripts

### 1. Kafka Broker Startup (`start_kafka.py`)
Starts a Kafka KRaft broker and ensures it's ready for connections.

#### Features
- Uses `subprocess` to run Kafka server startup.
- Monitors logs for readiness confirmation.
- Checks if port 9092 is open.
- Handles timeouts and clean shutdown.

#### Usage



---

### 2. Weather Data Producer (`weather_producer.py`)
Fetches real-time weather data and sends it to Kafka.

#### Features
- Uses Open-Meteo API to get current weather.
- Sends data as JSON to the `weather_data_demo` topic.
- Runs in a loop, sending data every 10 seconds.

#### Usage



---

### 3. Kafka Consumer (`weather_consumer.py`)
Reads weather data from Kafka and displays it.

#### Features
- Consumes messages from the `weather_data_demo` topic.
- Processes batches of messages.
- Prints each message's key, value, and offset.
- Gracefully handles interruption.

#### Usage


---

## Running the Pipeline

1. **Start Kafka**

2. **Run the Producer**

3. **Run the Consumer**

---

## Notes

- Kafka must be installed at `C:\kafka` on Windows.
- The Kafka topic used is `weather_data_demo`.
- The Open-Meteo API is free and requires no authentication for basic usage.
- Kafka consumer uses `group_id` for message group management.

---

## License

MIT License

