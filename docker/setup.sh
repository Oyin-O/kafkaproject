TOPIC_NAME="fraud_transactions"
BROKER="localhost:9092"
KAFKA_CONTAINER="kafka"  # Update this if your Kafka container has a different name

echo "⏳ Waiting for Kafka to be ready..."
sleep 10  # Give Kafka some time to start

echo "🚀 Creating Kafka topic: $TOPIC_NAME..."
docker exec -it $KAFKA_CONTAINER kafka-topics \
  --create --topic $TOPIC_NAME \
  --bootstrap-server $BROKER \
  --partitions 1 \
  --replication-factor 1

echo "✅ Kafka topic '$TOPIC_NAME' created!"
