from kafka import KafkaConsumer
import os

broker = os.getenv('KAFKA_BROKER', 'kafka1:9092,kafka2:9093,kafka3:9094')
topic = os.getenv('TOPIC', 'topico')
group_id = os.getenv('GROUP_ID', 'python-consumer-group')

consumer = KafkaConsumer(topic, group_id=group_id, bootstrap_servers=broker)
for message in consumer:
    print(f"Consumed message: {message.value.decode()}")
