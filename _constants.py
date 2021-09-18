from _global_constants import *
## Server Info
KAFKA_SERVER_PORT=KAFKA_SERVER + ':' + str(KAFKA_PORT)
WEBAPP_SERVER_PORT=WEBAPP_SERVER + ':' + str(WEBAPP_PORT)

## Topic constants
MQTT_TOPIC_NAME=TOPIC_PREFIX + '-mqtt-topic'
KAFKA_TOPIC_NAME=TOPIC_PREFIX + '-kafka-topic'

## Simulator constants
GENERATE_TIME_INTERVAL_SECS=5

## Webpage
LAST_N_MESSAGES=5
