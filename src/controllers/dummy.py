import json

import pydash as py_

import src.constants as Consts
from src.extensions import socketio
from kafka import KafkaConsumer, KafkaProducer


class Dummy(object):
    def __init__(self, namespace=None):
        self.namespace = namespace
        self.kafka_producer = KafkaProducer(bootstrap_servers=Consts.KAFKA_SERVER, value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        socketio.start_background_task(self.listen_kafka)

    def listen_kafka(self):
        self.kafka_consumer_pending = KafkaConsumer(
            Consts.TOPIC_DUMMY,
            bootstrap_servers=[Consts.KAFKA_SERVER],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: json.loads(x.decode('utf8'))
        )
        for message in self.kafka_consumer_pending:
            message_data = message.value
            # TODO: handle logic here
            socketio.emit("message", message_data, namespace=self.namespace, to="public")
        return
