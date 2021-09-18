from _imports import *
from _constants import *

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("MQTT_Producer")
client.connect(mqttBroker)

## Generate Customers
consumers_arr = get_all_consumers()

while True:
    ## Generate next iter data
    for consumer in get_next_data(consumers_arr):
        client.publish(MQTT_TOPIC_NAME, json.dumps(consumer))
        print("Just published " + str(consumer) + " to Topic " + MQTT_TOPIC_NAME)
        time.sleep(GENERATE_TIME_INTERVAL_SECS)
