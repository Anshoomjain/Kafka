import json
from kafka import KafkaConsumer

def fixed_kafka_consumer():
    
    topic = "weather_data_demo"
    
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        api_version=(0, 10, 1),
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        group_id='weather-consumer-group'
    )
    
    print(f"Consuming from topic: {topic}")
    
    try:
        while True:
            # poll() returns dict: {TopicPartition: [messages]}
            message_batch = consumer.poll(timeout_ms=1000)
            
            if not message_batch:
                print("Waiting for data...")
                continue
            
            # Process messages from all partitions
            for topic_partition, messages in message_batch.items():
                for msg in messages:
                    # Get key (may be None)
                    key = msg.key.decode('utf-8') if msg.key else None
                    value = msg.value
                    offset = msg.offset
                    
                    print(f"Received: key={key}, offset={offset}")
                    print(f"Value: {value}")
                    print("-" * 50)
                    
    except KeyboardInterrupt:
        print("Stopping consumer...")
    finally:
        consumer.close()
