from kafka import KafkaProducer
import json
import time
from faker import Faker
import random
from ..utils.data_generator import generate_transaction

fake = Faker()

# kafka configuration
broker = 'localhost:9092'
topic_name = 'fraud_transactions'

# initialise Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=broker,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


def send_transactions():
    """Send transactions to kafka continously"""
    while True:
        print('sending transactions')
        transactions = generate_transaction()
        producer.send(topic=topic_name, value=transactions)
        print(f'sent:{transactions}')
        time.sleep(2)


if __name__ == "__main__":
    send_transactions()
