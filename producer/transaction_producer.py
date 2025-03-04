from kafka import KafkaProducer
import json
import time
from faker import Faker
import random

fake = Faker()

# kafka configuration
broker = 'localhost:9092'
topic_name = 'fraud_transactions'

# initialise Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=broker,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


# generate fake transactions
def transaction_generator():
    """Generate fake transaction data"""

    return {
        'transaction_id': fake.uuid4(),
        'user_id': fake.random_int(min=100, max=999),
        'amount': round(random.uniform(10, 1000), 2),
        'timestamp': fake.date_time_this_year().isoformat(),
        'is_false': random.choice(['True', 'False'])
    }


def send_transactions():
    """Send transactions to kafka continously"""
    while True:
        print('sending transactions')
        transactions = transaction_generator()
        producer.send(topic=topic_name, value=transactions)
        print(f'sent:{transactions}')
        time.sleep(2)


if __name__ == "__main__":
    send_transactions()
