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

## One can you QUIXSTREAMS opensource library for the same
## some common terms using with Kafka

| Term           | Definition                                                                     |
| -------------- | ------------------------------------------------------------------------------ |
| Producer       | Application that sends messages to Kafka topicsinstaclustr+2​.                 |
| Consumer       | Application that reads messages from Kafka topicsinstaclustr+2​.               |
| Topic          | Category or feed name to which messages are publishedgeeksforgeeks+2​.         |
| Partition      | Sub-division of a topic for parallel processinggeeksforgeeks+2​.               |
| Broker         | Kafka server that stores and manages messagesinstaclustr+2​.                   |
| Consumer Group | Set of consumers working together to consume a topicconfluent+2​.              |
| Offset         | Unique position of a message within a partitionconfluent+1​.                   |
| Replication    | Copies of partitions for fault toleranceredhat+1​.                             |
| Leader         | Broker responsible for reads/writes for a partitionredhat+1​.                  |
| Follower       | Broker that copies data from the leader for redundancyredhat+1​.               |
| ZooKeeper      | Service that coordinates brokers and manages cluster statedata-flair+1​.       |
| Cluster        | Group of brokers working togetherdata-flair+1​.                                |
| Message        | Data sent from producer to consumerdata-flair+1​.                              |
| API            | Interfaces for interacting with Kafka (Producer, Consumer, Admin)confluent+1​. |

