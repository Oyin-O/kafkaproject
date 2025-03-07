import psycopg2


def store_fraud_transaction(transaction):
    try:
        # Establish the connection
        conn = psycopg2.connect(dbname="fraud_transactions", user="postgres", password="mysecretpassword",
                                host="localhost", port="5432")
        cursor = conn.cursor()

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
        print(f"Fraud transaction {transaction['transaction_id']} saved to database.")

    except Exception as e:
        print(f"Error saving transaction: {e}")

# CREATE TABLE transactions (
#     id SERIAL PRIMARY KEY,
#     transaction_id VARCHAR(255),
#     transaction_type VARCHAR(16),
#     amount DECIMAL,
#     user_id VARCHAR(255),
#     timestamp TIMESTAMP,
#     location VARCHAR(255),
#     merchant VARCHAR(255),
#     is_fraud BOOLEAN
# );
