import os
from dotenv import load_dotenv
load_dotenv()

KAFKA_SERVER = os.getenv('KAFKA_SERVER')
TOPIC_DUMMY = 'dummy'

