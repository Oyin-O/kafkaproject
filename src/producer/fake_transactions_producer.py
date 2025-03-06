from kafka import KafkaProducer
import json
import time
from faker import Faker
import random
from src.utils.data_generator import generate_transaction
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[logging.FileHandler('producer.log')])

fake = Faker()

# kafka configuration
broker = 'localhost:9092'
topic_name = 'fraud-transactions'

# initialise Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=broker,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


def send_transactions():
    """Send transactions to kafka continuously"""
    while True:
        transactions = generate_transaction()
        try:
            producer.send(topic=topic_name, value=transactions)
            logging.info(f'sent:{transactions}')
        except Exception as e:
            logging.error(f"Error sending transaction: {transactions}. Error: {str(e)}")
        time.sleep(2)


if __name__ == "__main__":
    send_transactions()
