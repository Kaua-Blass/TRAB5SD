from kafka import KafkaProducer
import os

broker = os.getenv('KAFKA_BROKER', 'kafka1:9092,kafka2:9093,kafka3:9094')
topic = os.getenv('TOPIC', 'topico')

producer = KafkaProducer(bootstrap_servers=broker)
for i in range(10):
    producer.send(topic, value=f"Message {i}".encode())
producer.flush()
producer.close()
