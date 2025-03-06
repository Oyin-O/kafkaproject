from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError

broker = 'localhost/9092'
topic_name = 'fraud_transactions'


def create_kafka_topic():
    admin_client = KafkaAdminClient(bootstrap_servers=broker, client_id='admin-client')
    topic = NewTopic(name=topic_name, num_partitions=1, replication_factor=1)

    try:
        admin_client.create_topics([topic])
        print(f'Topic {topic} created successfully')
    except TopicAlreadyExistsError:
        print(f'Topic {topic} already exists')
    except Exception as e:
        print(f'Error creating a topic {e}')
    finally:
        admin_client.close()


if __name__ == '__main__':
    create_kafka_topic()
