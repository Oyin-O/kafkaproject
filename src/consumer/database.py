import psycopg2
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[logging.FileHandler('consumer.log')])

load_dotenv()


def store_fraud_transaction(transaction):
    try:
        # Establish the connection
        conn = psycopg2.connect(
            dbname=os.getenv('POSTGRES_DB'),
            user="root",
            password=os.getenv('POSTGRES_PASSWORD'),
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id SERIAL PRIMARY KEY,
                transaction_id varchar(255),
                transaction_type varchar(255),
                amount DECIMAL(10,2),
                user_id varchar(255),
                timestamp TIMESTAMP,
                location varchar(255),
                merchant varchar(255),
                is_fraud BOOLEAN
            )
        """)

        # Insert the transaction into the database
        cursor.execute("""
            INSERT INTO transactions (transaction_id, transaction_type, amount, user_id, timestamp, location, merchant,
            is_fraud)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (transaction['transaction_id'], transaction['transaction_type'], transaction['amount'],
              transaction['user_id'], transaction['timestamp'], transaction['location'], transaction['merchant'],
              transaction['fraudulent']))

        # Commit and close
        conn.commit()
        cursor.close()
        conn.close()
        logging.info(f"Fraud transaction {transaction['transaction_id']} saved to database.")

    except Exception as e:
        logging.error(f"Error saving transaction: {e}")

