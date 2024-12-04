import click
import uuid
from confluent_kafka import Producer, Consumer, KafkaError, KafkaException
from confluent_kafka.admin import NewTopic, AdminClient

def produce_message(kafka_server, topic, message):
    producer = Producer({'bootstrap.servers': kafka_server})
    
    def on_delivery(err, msg):
        if err:
            print(f"Failed to deliver message: {err}")
        else:
            print(f"Message '{msg.value().decode('utf-8')}' sent to {msg.topic()}")

    try:
        producer.produce(topic, value=message, callback=on_delivery)
        producer.flush()
    except Exception as e:
        print(f"Failed to produce message: {e}")

def create_topic(kafka_server, topic):
    conf = {'bootstrap.servers': kafka_server}
    admin_client = AdminClient(conf)
    metadata = admin_client.list_topics(timeout=10)
    
    if topic not in metadata.topics:
        new_topic = NewTopic(topic, num_partitions=1, replication_factor=1)
        try:
            admin_client.create_topics([new_topic])
            print(f"Topic '{topic}' created successfully.")
        except Exception as e:
            print(f"Error creating topic '{topic}': {e}")
            raise

def consume_messages(kafka_server, topic):
    create_topic(kafka_server, topic)
    consumer = Consumer({
        'bootstrap.servers': kafka_server,
        'group.id': 'python_consumer_group_' + str(uuid.uuid4()),
        'auto.offset.reset': 'earliest',
    })
    consumer.subscribe([topic])
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                #print("No messages received in this poll cycle.")
                continue  
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"Reached end of partition: {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
                    continue
                else:
                    raise KafkaException(msg.error())
            print(f"Received message: {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        print("Stopping consumer...")
    finally:
        consumer.close()


@click.group()
def cli():
    pass

@cli.command()
@click.option('--message', required=True, help='Message to produce')
@click.option('--topic', required=True, help='Kafka topic')
@click.option('--kafka', required=True, help='Kafka server (ip:port)')
def produce(message, topic, kafka):
    produce_message(kafka, topic, message)

@cli.command()
@click.option('--topic', required=True, help='Kafka topic')
@click.option('--kafka', required=True, help='Kafka server (ip:port)')
def consume(topic, kafka):
    consume_messages(kafka, topic)

if __name__ == "__main__":
    cli()

