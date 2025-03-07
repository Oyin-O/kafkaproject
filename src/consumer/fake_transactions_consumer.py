from kafka import KafkaConsumer
from database import store_fraud_transaction
import json
import logging
logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('consumer.log')])


def is_fraud(transaction_dict):
    amount = transaction_dict.get('amount', 0)
    return amount > 800


consumer = KafkaConsumer(
    'fraud-transactions',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

logging.info('Listening for messages')
for message in consumer:
    transaction = json.loads(message.value)
    transaction['fraudulent'] = is_fraud(transaction)
    if transaction["fraudulent"]:
        store_fraud_transaction(transaction)
        logging.info(f"⚠️ FRAUD DETECTED: {transaction}")
    # else:
    #     logging.info(f"✅ Transaction OK: {transaction}")
    # consumer.commit()
