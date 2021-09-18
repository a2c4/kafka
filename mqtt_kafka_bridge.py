from _imports import *
from _constants import *

mqtt_broker = 'mqtt.eclipseprojects.io'
mqtt_client = mqtt.Client(client_id='MQTTBridge',protocol=MQTTv311)
mqtt_client.connect(mqtt_broker)

kafka_client = KafkaClient(hosts=KAFKA_SERVER_PORT)
kafka_topic = kafka_client.topics[KAFKA_TOPIC_NAME]
kafka_producer = kafka_topic.get_sync_producer()

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe(MQTT_TOPIC_NAME)  # Subscribe to the topic “digitest/test1”, receive any messages published on it

def on_message(client, userdata, message):
    msg_payload = json.loads(message.payload)
    print('Received MQTT message', msg_payload)
    kafka_producer.produce(message.payload)
    print('KAFKA: Just published ' + str(msg_payload) + ' to topic ' + KAFKA_TOPIC_NAME)
    time.sleep(.5)

mqtt_client.loop_start()
#mqtt_client.subscribe('mqtt-drive-topic')
mqtt_client.on_connect = on_connect  # Define callback function for successful connection
mqtt_client.on_message = on_message
time.sleep(300)
mqtt_client.loop_start()
