from faker import Faker
import random
import json

fake = Faker()


def generate_transaction():
    """Generate a fake transaction."""
    transaction = {
        'transaction_id': fake.uuid4(),
        'user_id': fake.uuid4(),
        'amount': round(random.uniform(5.0, 1000.0), 2),
        'transaction_type': random.choice(['purchase', 'refund']),
        'timestamp': fake.date_this_year().isoformat(),
        'merchant': fake.company(),
        'location': fake.city(),
        'fraudulent': random.choice([True, False])
    }
    return json.dumps(transaction)
